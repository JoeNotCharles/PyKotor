from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Callable, List

from pykotor.common.language import LocalizedString
from pykotor.common.misc import ResRef
from pykotor.resource.formats.gff import GFF, GFFFieldType, GFFList, GFFStruct
from pykotor.tools.path import CaseAwarePath

if TYPE_CHECKING:
    from pykotor.tslpatcher.logger import PatchLogger
    from pykotor.tslpatcher.memory import PatcherMemory

# TODO(NickHugi): 2DAMEMORY# as field path+label, store+save


class LocalizedStringDelta(LocalizedString):
    def __init__(self, stringref: FieldValue | None = None) -> None:
        super().__init__(0)
        self.stringref: FieldValue | None = stringref

    def apply(self, locstring: LocalizedString, memory: PatcherMemory) -> None:
        if self.stringref is not None:
            locstring.stringref = self.stringref.value(memory, GFFFieldType.UInt32)
        for language, gender, text in self:
            locstring.set(language, gender, text)


# region Value Returners
class FieldValue(ABC):
    @abstractmethod
    def value(self, memory: PatcherMemory, field_type: GFFFieldType) -> Any:
        ...

    def validate(self, value: Any, field_type: GFFFieldType) -> Any:
        if field_type == GFFFieldType.ResRef and not isinstance(value, ResRef):
            value = ResRef(str(value))
        elif field_type == GFFFieldType.String and not isinstance(value, str):
            value = str(value)
        elif field_type.return_type() == int and isinstance(value, str):
            value = int(value)
        elif field_type.return_type() == float and isinstance(value, str):
            value = float(value)
        return value


class FieldValueConstant(FieldValue):
    def __init__(self, value: Any):
        self.stored = value

    def value(self, memory: PatcherMemory, field_type: GFFFieldType) -> Any:
        return self.validate(self.stored, field_type)


class FieldValue2DAMemory(FieldValue):
    def __init__(self, token_id: int):
        self.token_id = token_id

    def value(self, memory: PatcherMemory, field_type: GFFFieldType) -> Any:
        return self.validate(memory.memory_2da[self.token_id], field_type)


class FieldValueTLKMemory(FieldValue):
    def __init__(self, token_id: int):
        self.token_id = token_id

    def value(self, memory: PatcherMemory, field_type: GFFFieldType) -> Any:
        return self.validate(memory.memory_str[self.token_id], field_type)


# endregion


# region Modify GFF
class ModifyGFF(ABC):
    @abstractmethod
    def apply(
        self,
        container: GFFStruct | GFFList,
        memory: PatcherMemory,
        logger: PatchLogger,
    ) -> None:
        ...

    def _navigate_containers(
        self,
        container: GFFStruct | GFFList | None,
        path: CaseAwarePath,
    ) -> GFFList | GFFStruct | None:
        assert isinstance(path, CaseAwarePath)
        for step in path.parts:
            if isinstance(container, GFFStruct):
                container = container.acquire(step, None, (GFFStruct, GFFList))  # type: ignore
            elif isinstance(container, GFFList):
                container = container.at(int(step))

        return container

    def _navigate_to_field(
        self,
        container: GFFStruct | GFFList | None,
        path: CaseAwarePath,
    ) -> GFFList | GFFStruct | None:
        assert isinstance(path, CaseAwarePath)
        label: str = path.parts[-1]

        for step in path.parent.parts:
            if isinstance(container, GFFStruct):
                container = container.acquire(step, None, (GFFStruct, GFFList))  # type: ignore
            elif isinstance(container, GFFList):
                container = container.at(int(step))
            else:
                return None

        return container._fields[label] if isinstance(container, GFFStruct) else None


class AddStructToListGFF(ModifyGFF):
    def __init__(
        self,
        identifier: str | None,
        struct_id: int,
        index_to_token: int | None = None,
        path: CaseAwarePath | str | None = None,
        modifiers: list[ModifyGFF] | None = None,
        parent_identifier: str | None = None,
    ):
        self.struct_id = struct_id
        self.identifier = identifier or ""
        self.index_to_token = index_to_token
        self.path: CaseAwarePath | None = CaseAwarePath(path) if isinstance(path, str) else path
        if self.path:
            parent_identifier = self.path.parent.name
        self.parent_identifier = parent_identifier
        assert self.parent_identifier or self.struct_id

        self.modifiers: list[ModifyGFF] = [] if modifiers is None else modifiers

    def apply(
        self,
        container: GFFList | GFFStruct,
        memory: PatcherMemory,
        logger: PatchLogger,
    ) -> None:
        new_struct: GFFStruct | None = None
        navigated_container: GFFList | GFFStruct | None = (
            container
            if not self.path
            else self._navigate_containers(container, self.path)
        )
        if isinstance(navigated_container, GFFList):
            struct_id = self.struct_id if self.struct_id is not None else len(container)
            new_struct = navigated_container.add(struct_id)

            # If an index_to_token is provided, store the new struct's index in PatcherMemory
            if self.index_to_token is not None:
                memory.memory_2da[self.index_to_token] = str(struct_id)
        elif isinstance(navigated_container, GFFStruct):
            struct_id = self.struct_id or len(navigated_container.get_list(self.parent_identifier) ) - 1 # type: ignore
            new_struct = GFFStruct(struct_id)
            navigated_container.set_struct(self.identifier, new_struct)

        if new_struct is None:
            logger.add_error(
                f"Failed to add a new struct with struct_id '{self.struct_id}'. Aborting.",
            )
            return

        for add_field in self.modifiers:
            add_field.apply(new_struct, memory, logger)


class AddFieldGFF(ModifyGFF):
    def __init__(
        self,
        identifier: str,
        label: str,
        field_type: GFFFieldType,
        value: FieldValue,
        path: str | CaseAwarePath | None,
        modifiers: list[ModifyGFF] | None = None,
        index_to_list_token: int | None = None,
    ):
        self.identifier: str = identifier
        self.label: str = label
        self.field_type: GFFFieldType = field_type
        self.value: FieldValue = value
        self.path: CaseAwarePath | None = CaseAwarePath(path) if isinstance(path, str) else path
        self.index_to_list_token: int | None = index_to_list_token

        self.modifiers: list[ModifyGFF] = [] if modifiers is None else modifiers

    def apply(
        self,
        container: GFFStruct | GFFList,
        memory: PatcherMemory,
        logger: PatchLogger,
    ) -> None:
        if self.path:
            container = self._navigate_containers(
                container,
                self.path,
            )  # type: ignore
        container_is_correct_type = isinstance(container, (GFFStruct, GFFList))
        if not container_is_correct_type:
            reason: str = "does not exist!" if container is None else "is not an instance of a GFF List/Struct."
            logger.add_error(f"Unable to add new Field '{self.label}'. Parent field at '{self.path}' {reason}")
            return
        assert container_is_correct_type

        value = self.value.value(memory, self.field_type)

        def set_locstring() -> None:
            original = LocalizedString(0)
            value.apply(original, memory)
            assert isinstance(container, GFFStruct)
            container.set_locstring(self.label, original)

        def set_struct() -> GFFStruct | None:
            if isinstance(container, GFFStruct):
                return container.set_struct(self.label, value)
            if isinstance(container, GFFList):
                return container.add(value.struct_id)
            return None

        def set_list() -> GFFList:
            assert isinstance(container, GFFStruct)
            return container.set_list(self.label, value)

        func_map: dict[GFFFieldType, Any] = {
            GFFFieldType.Int8: lambda: container.set_int8(self.label, value),
            GFFFieldType.UInt8: lambda: container.set_uint8(self.label, value),
            GFFFieldType.Int16: lambda: container.set_int16(self.label, value),
            GFFFieldType.UInt16: lambda: container.set_uint16(self.label, value),
            GFFFieldType.Int32: lambda: container.set_int32(self.label, value),
            GFFFieldType.UInt32: lambda: container.set_uint32(self.label, value),
            GFFFieldType.Int64: lambda: container.set_int64(self.label, value),
            GFFFieldType.UInt64: lambda: container.set_uint64(self.label, value),
            GFFFieldType.Single: lambda: container.set_single(self.label, value),
            GFFFieldType.Double: lambda: container.set_double(self.label, value),
            GFFFieldType.String: lambda: container.set_string(self.label, value),
            GFFFieldType.ResRef: lambda: container.set_resref(self.label, value),
            GFFFieldType.LocalizedString: set_locstring,
            GFFFieldType.Vector3: lambda: container.set_vector3(self.label, value),
            GFFFieldType.Vector4: lambda: container.set_vector4(self.label, value),
            GFFFieldType.Struct: set_struct,
            GFFFieldType.List: set_list,
        }
        container = func_map[self.field_type]()

        if self.index_to_list_token is not None and isinstance(container, GFFList):
            memory.memory_2da[self.index_to_list_token] = str(len(container) - 1)

        for add_field in self.modifiers:
            add_field.apply(container, memory, logger)


class ModifyFieldGFF(ModifyGFF):
    def __init__(
        self,
        path: str | CaseAwarePath,
        value: FieldValue
    ) -> None:
        self.path: CaseAwarePath = CaseAwarePath(path) if isinstance(path, str) else path
        self.value: FieldValue = value

    def apply(
        self,
        container: GFFStruct | GFFList,
        memory: PatcherMemory,
        logger: PatchLogger,
    ) -> None:
        
        label = self.path.name
        navigated_container: GFFStruct | GFFList | None = self._navigate_containers(container, self.path.parent) or container

        container_is_correct_type = isinstance(container, GFFStruct)
        if not container_is_correct_type:
            logger.add_error(f"Unable to find a field label matching '{label}', skipping...")
            return
        assert isinstance(navigated_container, GFFStruct)

        field_type = navigated_container._fields[label].field_type()
        value = self.value.value(memory, field_type)

        def set_locstring() -> None:
            assert isinstance(value, LocalizedStringDelta)
            if navigated_container.exists(label):
                original: LocalizedString = navigated_container.get_locstring(label)
                value.apply(original, memory)
                navigated_container.set_locstring(label, original)
            else:
                navigated_container.set_locstring(label, value)

        func_map: dict[GFFFieldType, Callable] = {
            GFFFieldType.Int8: lambda: navigated_container.set_int8(label, value),
            GFFFieldType.UInt8: lambda: navigated_container.set_uint8(label, value),
            GFFFieldType.Int16: lambda: navigated_container.set_int16(label, value),
            GFFFieldType.UInt16: lambda: navigated_container.set_uint16(label, value),
            GFFFieldType.Int32: lambda: navigated_container.set_int32(label, value),
            GFFFieldType.UInt32: lambda: navigated_container.set_uint32(label, value),
            GFFFieldType.Int64: lambda: navigated_container.set_int64(label, value),
            GFFFieldType.UInt64: lambda: navigated_container.set_uint64(label, value),
            GFFFieldType.Single: lambda: navigated_container.set_single(label, value),
            GFFFieldType.Double: lambda: navigated_container.set_double(label, value),
            GFFFieldType.String: lambda: navigated_container.set_string(label, value),
            GFFFieldType.ResRef: lambda: navigated_container.set_resref(label, value),
            GFFFieldType.LocalizedString: set_locstring,
            GFFFieldType.Vector3: lambda: navigated_container.set_vector3(label, value),
            GFFFieldType.Vector4: lambda: navigated_container.set_vector4(label, value),
        }
        func_map[field_type]()


# endregion


class ModificationsGFF:
    def __init__(
        self,
        filename: str,
        replace_file: bool,
        modifiers: list[ModifyGFF] | None = None,
        destination: str | CaseAwarePath | None = None,
    ) -> None:
        self.filename: str = filename
        self.replace_file: bool = replace_file
        if destination is None:
            self.destination = CaseAwarePath("Override", filename)
        elif not isinstance(destination, CaseAwarePath):
            self.destination = CaseAwarePath(destination)
        else:
            self.destination = destination

        self.modifiers: list[ModifyGFF] = modifiers if modifiers is not None else []

    def apply(
        self,
        gff: GFF,
        memory: PatcherMemory,
        logger: PatchLogger,
    ) -> None:
        for change_field in self.modifiers:
            change_field.apply(gff.root, memory, logger)
