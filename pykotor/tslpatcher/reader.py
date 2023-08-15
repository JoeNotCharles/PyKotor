from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Literal

from chardet import UniversalDetector

from pykotor.common.geometry import Vector3, Vector4
from pykotor.common.language import LocalizedString
from pykotor.common.misc import ResRef
from pykotor.common.stream import BinaryReader
from pykotor.resource.formats.gff import GFFFieldType, GFFList, GFFStruct
from pykotor.resource.formats.ssf import SSFSound
from pykotor.resource.formats.tlk import TLK, read_tlk
from pykotor.tools.misc import is_float, is_int
from pykotor.tslpatcher.config import PatcherConfig, PatcherNamespace
from pykotor.tslpatcher.memory import NoTokenUsage, TokenUsage2DA, TokenUsageTLK
from pykotor.tslpatcher.mods.gff import (
    AddFieldGFF,
    FieldValue,
    FieldValue2DAMemory,
    FieldValueConstant,
    FieldValueTLKMemory,
    LocalizedStringDelta,
    ModificationsGFF,
    ModifyFieldGFF,
    ModifyGFF,
)
from pykotor.tslpatcher.mods.install import InstallFile, InstallFolder
from pykotor.tslpatcher.mods.nss import ModificationsNSS
from pykotor.tslpatcher.mods.ssf import ModificationsSSF, ModifySSF
from pykotor.tslpatcher.mods.tlk import ModifyTLK
from pykotor.tslpatcher.mods.twoda import (
    AddColumn2DA,
    AddRow2DA,
    ChangeRow2DA,
    CopyRow2DA,
    Modifications2DA,
    Modify2DA,
    RowValue,
    RowValue2DAMemory,
    RowValueConstant,
    RowValueHigh,
    RowValueRowCell,
    RowValueRowIndex,
    RowValueRowLabel,
    RowValueTLKMemory,
    Target,
    TargetType,
    WarningException,
)

if TYPE_CHECKING:
    from pykotor.resource.formats.tlk.tlk_data import TLKEntry


class ConfigReader:
    def __init__(self, ini: ConfigParser, mod_path: Path | str) -> None:
        self.ini = ini
        self.mod_path: Path = Path(mod_path)
        self.config: PatcherConfig

    @classmethod
    def from_filepath(cls, path: str) -> PatcherConfig:
        ini_file_bytes = BinaryReader.load_file(path)

        detector = UniversalDetector()
        detector.feed(ini_file_bytes)
        detector.close()
        encoding = detector.result["encoding"]

        ini_text = ini_file_bytes.decode(encoding)

        ini = ConfigParser(
            delimiters=("="),
            allow_no_value=True,
            strict=False,
            interpolation=None,
        )
        ini.optionxform = str  # type: ignore[reportGeneralTypeIssues]  # use case sensitive keys
        ini.read_string(ini_text)

        config = PatcherConfig()
        return ConfigReader(ini, path).load(config)

    def load(self, config: PatcherConfig) -> PatcherConfig:
        self.config: PatcherConfig = config

        self.load_settings()
        print("Parsing file list from [InstallList]")
        self.load_filelist()
        print("Parsing stringrefs from [TLKList]")
        self.load_tlk_list()
        print("Parsing 2da from [2DAList]")
        self.load_2da()
        print("Parsing SSF from [SSFList]")
        self.load_ssf()
        print("Parsing GFF from [GFFList]")
        self.load_gff()
        print("Parsing NSS from [NSSList]")
        self.load_nss()

        return self.config

    def load_settings(self) -> None:
        self.config.window_title = self.ini.get(
            "Settings",
            "WindowCaption",
            fallback="",
        )
        self.config.confirm_message = self.ini.get(
            "Settings",
            "ConfirmMessage",
            fallback="",
        )
        # Try to get the value and convert it to an integer
        lookup_game_number = self.ini.get("Settings", "LookupGameNumber", fallback=None)
        if lookup_game_number is not None:
            try:
                self.config.game_number = int(lookup_game_number)
            except ValueError:
                # Handle invalid integer conversion here if needed
                print(f"Invalid game number: {lookup_game_number}")
        else:
            self.config.game_number = None
        self.config.required_file = self.ini.get("Settings", "Required", fallback=None)
        self.config.required_message = self.ini.get("Settings", "Required", fallback="")

    def load_filelist(self) -> None:
        if "InstallList" not in self.ini:
            return

        folders_ini = dict(self.ini["InstallList"].items())
        for key, foldername in folders_ini.items():
            folder_install = InstallFolder(foldername)
            self.config.install_list.append(folder_install)

            files_ini = dict(self.ini[key].items())
            for key2, filename in files_ini.items():
                replace_existing = key2.lower().startswith("replace")
                file_install = InstallFile(filename, replace_existing)
                folder_install.files.append(file_install)

    def load_tlk_list(self) -> None:
        if "TLKList" not in self.ini:
            return

        tlk_list_edits = dict(self.ini["TLKList"].items())
        modifier_dict: dict[int, dict[str, str | ResRef]] = {}
        append_tlk_edits = None

        def load_tlk(tlk_path: Path) -> TLK:
            return read_tlk(tlk_path) if tlk_path.exists() else TLK()

        range_delims = [":", "-", "to"]

        def extract_range_parts(range_str) -> tuple[int, int | None]:
            if range_str.lower().startswith("strref") or range_str.lower().startswith(
                "ignore",
            ):
                range_str = range_str[6:]
            for delim in range_delims:
                if delim in range_str:
                    parts = range_str.split(delim)
                    start = int(parts[0].strip()) if parts[0].strip() else 0
                    end = int(parts[1].strip()) if parts[1].strip() else None
                    return start, end
            return int(range_str), None

        def parse_range(range_str: str, max_value: int) -> range:
            start, end = extract_range_parts(range_str)
            if end is None:
                return range(int(range_str), int(range_str) + 1)
            if end < start:
                msg = f"start of range {start} must be less than end of range {end}"
                raise ValueError(msg)
            return range(start, end + 1)

        tlk_list_ignored_indices: set[int] = set()

        def process_tlk_entries(
            tlk_data: TLK,
            modifications_ini_keys,
            modifications_ini_values,
            is_replacement,
        ):
            def append_modifier(token_id, text, voiceover, is_replacement):
                modifier = ModifyTLK(token_id, text, voiceover, is_replacement)
                self.config.patches_tlk.modifiers.append(modifier)

            for mod_key, mod_value in zip(
                modifications_ini_keys,
                modifications_ini_values,
            ):
                change_indices = (
                    parse_range(str(mod_key), len(tlk_data))
                    if not isinstance(mod_key, range)
                    else mod_key
                )
                value_range = (
                    parse_range(str(mod_value), len(tlk_data))
                    if not isinstance(mod_value, range) and mod_value != ""
                    else mod_key
                )

                for mod_index, token_id in zip(change_indices, value_range):
                    if mod_index in tlk_list_ignored_indices:
                        continue
                    entry: TLKEntry = tlk_data[mod_index]
                    append_modifier(
                        token_id,
                        entry.text,
                        entry.voiceover,
                        is_replacement,
                    )

        for i in tlk_list_edits:
            if i.lower().startswith("ignore"):
                # load append.tlk only if it's needed.
                if append_tlk_edits is None:
                    append_tlk_edits = load_tlk(self.mod_path / "append.tlk")
                tlk_list_ignored_indices.update(
                    parse_range(i[6:], len(append_tlk_edits)),
                )

        for key, value in tlk_list_edits.items():
            key: str = key.lower()
            if key.startswith("ignore"):
                continue
            if key.startswith("strref"):
                # load append.tlk only if it's needed.
                if append_tlk_edits is None:
                    append_tlk_edits = load_tlk(self.mod_path / "append.tlk")
                strref_range = parse_range(key, len(append_tlk_edits))
                token_id_range = parse_range(value, len(append_tlk_edits))
                process_tlk_entries(
                    append_tlk_edits,
                    strref_range,
                    token_id_range,
                    is_replacement=False,
                )
            elif key.startswith("file"):
                tlk_modifications_path: Path = self.mod_path / value
                if value not in self.ini:
                    msg = f"INI header for '{value}' referenced in TLKList key '{key}' not found."
                    raise KeyError(msg)
                tlk_ini_edits = dict(self.ini[value].items())
                modifications_tlk_data: TLK = load_tlk(tlk_modifications_path)
                process_tlk_entries(
                    modifications_tlk_data,
                    tlk_ini_edits.keys(),
                    tlk_ini_edits.values(),
                    is_replacement=True,
                )
            elif "\\" in key or "/" in key:
                delimiter: Literal["\\", "/"] = "\\" if "\\" in key else "/"
                token_id_str, property_name = key.split(delimiter)
                token_id = int(token_id_str)

                if token_id not in modifier_dict:
                    modifier_dict[token_id] = {
                        "text": "",
                        "voiceover": "",
                    }

                if property_name == "text":
                    modifier_dict[token_id]["text"] = value
                elif property_name == "sound":
                    modifier_dict[token_id]["voiceover"] = ResRef(value)
                else:
                    msg = f"Invalid TLKList syntax for key '{key}' value '{value}'"
                    raise KeyError(msg)

                text = modifier_dict[token_id].get("text")
                voiceover = modifier_dict[token_id].get("voiceover")

                # TODO(th3w1zard1): replace modifier_dict with ModifyTLK and allow optional text and voiceover properties.
                # EDIT: looked into the above todo, would require a large restructure of the way TLK is stored.
                if isinstance(text, str) and isinstance(voiceover, ResRef):
                    modifier = ModifyTLK(token_id, text, voiceover, is_replacement=True)
                    self.config.patches_tlk.modifiers.append(modifier)
            else:
                msg = f"Invalid key in TLKList: '{key}'"
                raise KeyError(msg)

    def load_2da(self) -> None:
        if "2DAList" not in self.ini:
            return

        files = dict(self.ini["2DAList"].items())

        for file in files.values():
            modification_ids = dict(self.ini[file].items())

            modifications = Modifications2DA(file)
            self.config.patches_2da.append(modifications)

            for key, modification_id in modification_ids.items():
                manipulation = self.discern_2da(
                    key,
                    modification_id,
                    dict(self.ini[modification_id].items()),
                )
                modifications.modifiers.append(manipulation)

    def load_ssf(self) -> None:
        if "SSFList" not in self.ini:
            return

        configstr_to_ssfsound: dict[str, SSFSound] = {
            "Battlecry 1": SSFSound.BATTLE_CRY_1,
            "Battlecry 2": SSFSound.BATTLE_CRY_2,
            "Battlecry 3": SSFSound.BATTLE_CRY_3,
            "Battlecry 4": SSFSound.BATTLE_CRY_4,
            "Battlecry 5": SSFSound.BATTLE_CRY_5,
            "Battlecry 6": SSFSound.BATTLE_CRY_6,
            "Selected 1": SSFSound.SELECT_1,
            "Selected 2": SSFSound.SELECT_2,
            "Selected 3": SSFSound.SELECT_3,
            "Attack 1": SSFSound.ATTACK_GRUNT_1,
            "Attack 2": SSFSound.ATTACK_GRUNT_2,
            "Attack 3": SSFSound.ATTACK_GRUNT_3,
            "Pain 1": SSFSound.PAIN_GRUNT_1,
            "Pain 2": SSFSound.PAIN_GRUNT_2,
            "Low health": SSFSound.LOW_HEALTH,
            "Death": SSFSound.DEAD,
            "Critical hit": SSFSound.CRITICAL_HIT,
            "Target immune": SSFSound.TARGET_IMMUNE,
            "Place mine": SSFSound.LAY_MINE,
            "Disarm mine": SSFSound.DISARM_MINE,
            "Stealth on": SSFSound.BEGIN_STEALTH,
            "Search": SSFSound.BEGIN_SEARCH,
            "Pick lock start": SSFSound.BEGIN_UNLOCK,
            "Pick lock fail": SSFSound.UNLOCK_FAILED,
            "Pick lock done": SSFSound.UNLOCK_SUCCESS,
            "Leave party": SSFSound.SEPARATED_FROM_PARTY,
            "Rejoin party": SSFSound.REJOINED_PARTY,
            "Poisoned": SSFSound.POISONED,
        }

        files = dict(self.ini["SSFList"].items())

        for identifier, file in files.items():
            modifications_ini = dict(self.ini[file].items())
            replace = identifier.startswith("Replace")

            modifications = ModificationsSSF(file, replace)
            self.config.patches_ssf.append(modifications)

            for name, value in modifications_ini.items():
                if value.startswith("2DAMEMORY"):
                    token_id = int(value[9:])
                    value = TokenUsage2DA(token_id)
                elif value.startswith("StrRef"):
                    token_id = int(value[6:])
                    value = TokenUsageTLK(token_id)
                else:
                    value = NoTokenUsage(int(value))

                sound = configstr_to_ssfsound[name]
                modifier = ModifySSF(sound, value)
                modifications.modifiers.append(modifier)

    def load_gff(self) -> None:
        if "GFFList" not in self.ini:
            return

        files = dict(self.ini["GFFList"].items())

        for identifier, file in files.items():
            modifications_ini = dict(self.ini[file].items())
            replace = identifier.startswith("Replace")

            modifications = ModificationsGFF(file, replace)
            self.config.patches_gff.append(modifications)

            for name, value in modifications_ini.items():
                lowercase_name = name.lower()
                if lowercase_name == "!destination":
                    modifications.destination = value
                elif lowercase_name == "!replacefile":
                    modifications.replace_file = bool(int(value))
                elif lowercase_name in ["!filename", "!saveas"]:
                    modifications.filename = value
                elif lowercase_name.startswith("addfield"):
                    modifier = self.add_field_gff(value, dict(self.ini[value]))
                    modifications.modifiers.append(modifier)
                else:
                    modifier = self.modify_field_gff(name, value)
                    modifications.modifiers.append(modifier)

    def load_nss(self) -> None:
        if "CompileList" not in self.ini:
            return

        files = dict(self.ini["CompileList"].items())
        destination = files.pop("!destination", None)

        for identifier, file in files.items():
            replace = identifier.lower().startswith("replace")
            modifications = ModificationsNSS(file, replace)
            self.config.patches_nss.append(modifications)

            if destination is not None:
                modifications.destination = destination
        print("Parsing NSS files done!")

    #################

    def field_value_gff(self, raw_value: str) -> FieldValue:
        if raw_value.startswith("StrRef"):
            token_id = int(raw_value[6:])
            return FieldValueTLKMemory(token_id)
        if raw_value.startswith("2DAMEMORY"):
            token_id = int(raw_value[9:])
            return FieldValueTLKMemory(token_id)
        return FieldValueConstant(int(raw_value))

    def modify_field_gff(self, name: str, string_value: str) -> ModifyFieldGFF:
        if string_value.startswith("2DAMEMORY"):
            token_id = int(string_value[9:])
            value = FieldValue2DAMemory(token_id)
        elif string_value.startswith("StrRef"):
            token_id = int(string_value[6:])
            value = FieldValueTLKMemory(token_id)
        elif is_int(string_value):
            value = FieldValueConstant(int(string_value))
        elif is_float(string_value):
            value = FieldValueConstant(float(string_value))
        elif string_value.count("|") == 2:
            components = string_value.split("|")
            value = FieldValueConstant(Vector3(*[float(x) for x in components]))
        elif string_value.count("|") == 3:
            components = string_value.split("|")
            value = FieldValueConstant(Vector4(*[float(x) for x in components]))
        else:
            value = FieldValueConstant(
                string_value.replace("<#LF#>", "\n").replace("<#CR#>", "\r"),
            )

        if "(strref)" in name:
            value = FieldValueConstant(LocalizedStringDelta(value))
            name = name[: name.index("(strref)")]
        elif "(lang" in name:
            substring_id = int(name[name.index("(lang") + 5 : -1])
            language, gender = LocalizedString.substring_pair(substring_id)
            locstring = LocalizedStringDelta()
            locstring.set(language, gender, string_value)
            value = FieldValueConstant(locstring)
            name = name[: name.index("(lang")]

        return ModifyFieldGFF(name, value)

    def add_field_gff(
        self,
        identifier: str,
        ini_data: dict[str, str],
        inside_list: bool = False,
    ) -> AddFieldGFF:
        fieldname_to_fieldtype = {
            "Byte": GFFFieldType.UInt8,
            "Char": GFFFieldType.Int8,
            "Word": GFFFieldType.UInt16,
            "Short": GFFFieldType.Int16,
            "DWORD": GFFFieldType.UInt32,
            "Int": GFFFieldType.Int32,
            "Int64": GFFFieldType.Int64,
            "Float": GFFFieldType.Single,
            "Double": GFFFieldType.Double,
            "ExoString": GFFFieldType.String,
            "ResRef": GFFFieldType.ResRef,
            "ExoLocString": GFFFieldType.LocalizedString,
            "Position": GFFFieldType.Vector3,
            "Orientation": GFFFieldType.Vector4,
            "Struct": GFFFieldType.Struct,
            "List": GFFFieldType.List,
        }

        field_type = fieldname_to_fieldtype[ini_data["FieldType"]]
        path = ini_data.get("Path", "")
        label = ini_data["Label"]
        raw_value = ini_data.get("Value")
        if raw_value is None:
            if field_type.return_type() == LocalizedString:
                stringref = self.field_value_gff(ini_data["StrRef"])

                value = LocalizedStringDelta(stringref)
                for substring, text in ini_data.items():
                    if not substring.startswith("lang"):
                        continue
                    substring_id = int(substring[4:])
                    language, gender = value.substring_pair(substring_id)
                    value.set(language, gender, text)
                value = FieldValueConstant(value)
            elif field_type.return_type() == GFFList:
                value = FieldValueConstant(GFFList())
            elif field_type.return_type() == GFFStruct:
                struct_id = int(ini_data["TypeId"])
                value = FieldValueConstant(GFFStruct(struct_id))
            else:
                raise ValueError(field_type)
        elif raw_value.startswith("2DAMEMORY"):
            token_id = int(raw_value[9:])
            value = FieldValue2DAMemory(token_id)
        elif raw_value.endswith("StrRef"):
            token_id = int(raw_value[6:])
            value = FieldValueTLKMemory(token_id)

        elif field_type.return_type() == int:
            value = FieldValueConstant(int(raw_value))
        elif field_type.return_type() == float:
            # Replace comma with dot for decimal separator to match TSLPatcher syntax.
            float_val = raw_value.replace(",", ".")
            value = FieldValueConstant(float(float_val))
        elif field_type.return_type() == str:
            value = FieldValueConstant(
                raw_value.replace("<#LF#>", "\n").replace("<#CR#>", "\r"),
            )
        elif field_type.return_type() == ResRef:
            value = FieldValueConstant(ResRef(raw_value))
        elif field_type.return_type() == Vector3:
            components = [
                float(axis.replace(",", ".")) for axis in raw_value.split("|")
            ]
            value = FieldValueConstant(Vector3(*components))
        elif field_type.return_type() == Vector4:
            components = [
                float(axis.replace(",", ".")) for axis in raw_value.split("|")
            ]
            value = FieldValueConstant(Vector4(*components))
        else:
            raise ValueError(field_type)

        # Get nested fields/struct
        nested_modifiers: list[ModifyGFF] = []
        for key, x in ini_data.items():
            if not key.startswith("AddField"):
                continue

            is_list = field_type.return_type() == GFFList
            modifier = self.add_field_gff(x, dict(self.ini[x].items()), is_list)
            nested_modifiers.append(modifier)

        index_in_list_token = None
        for key, memvalue in ini_data.items():
            if (
                key.startswith("2DAMEMORY")
                and memvalue == "ListIndex"
                and field_type.return_type() != GFFStruct
            ):
                index_in_list_token = int(key[9:])

        return AddFieldGFF(
            identifier,
            label,
            field_type,
            value,
            path,
            nested_modifiers,
            index_in_list_token,
        )

    #################
    def discern_2da(
        self,
        key: str,
        identifier: str,
        modifiers: dict[str, str],
    ) -> Modify2DA:
        if key.startswith("ChangeRow"):
            target = self.target_2da(identifier, modifiers)
            cells, store_2da, store_tlk = self.cells_2da(identifier, modifiers)
            modification = ChangeRow2DA(identifier, target, cells, store_2da, store_tlk)
        elif key.startswith("AddRow"):
            exclusive_column = self.exclusive_column_2da(modifiers)
            row_label = self.row_label_2da(identifier, modifiers)
            cells, store_2da, store_tlk = self.cells_2da(identifier, modifiers)
            modification = AddRow2DA(
                identifier,
                exclusive_column,
                row_label,
                cells,
                store_2da,
                store_tlk,
            )
        elif key.startswith("CopyRow"):
            target = self.target_2da(identifier, modifiers)
            exclusive_column = self.exclusive_column_2da(modifiers)
            row_label = self.row_label_2da(identifier, modifiers)
            cells, store_2da, store_tlk = self.cells_2da(identifier, modifiers)
            modification = CopyRow2DA(
                identifier,
                target,
                exclusive_column,
                row_label,
                cells,
                store_2da,
                store_tlk,
            )
        elif key.startswith("AddColumn"):
            header = modifiers.pop("ColumnLabel")
            default = modifiers.pop("DefaultValue")
            default = default if default != "****" else ""
            index_insert, label_insert, store_2da = self.column_inserts_2da(
                identifier,
                modifiers,
            )
            modification = AddColumn2DA(
                identifier,
                header,
                default,
                index_insert,
                label_insert,
                store_2da,
            )
        else:
            raise WarningException

        return modification

    def target_2da(self, identifier: str, modifiers: dict[str, str]) -> Target:
        if "RowIndex" in modifiers:
            target = Target(TargetType.ROW_INDEX, int(modifiers["RowIndex"]))
            modifiers.pop("RowIndex")
        elif "RowLabel" in modifiers:
            target = Target(TargetType.ROW_LABEL, modifiers["RowLabel"])
            modifiers.pop("RowLabel")
        elif "LabelIndex" in modifiers:
            target = Target(TargetType.LABEL_COLUMN, modifiers["LabelIndex"])
            modifiers.pop("LabelIndex")
        else:
            msg = f"No line set to be modified for '{identifier}'."
            raise WarningException(msg)

        return target

    def exclusive_column_2da(self, modifiers: dict[str, str]) -> str | None:
        if "ExclusiveColumn" in modifiers:
            return modifiers.pop("ExclusiveColumn")
        return None

    def cells_2da(
        self,
        identifier: str,
        modifiers: dict[str, str],
    ) -> tuple[dict[str, RowValue], dict[int, RowValue], dict[int, RowValue]]:
        cells: dict[str, RowValue] = {}
        store_2da: dict[int, RowValue] = {}
        store_tlk: dict[int, RowValue] = {}

        for modifier, value in modifiers.items():
            is_store_2da = modifier.startswith("2DAMEMORY")
            is_store_tlk = modifier.startswith("StrRef")
            is_row_label = modifier in ["RowLabel", "NewRowLabel"]

            if value.startswith("2DAMEMORY"):
                token_id = int(value[9:])
                row_value = RowValue2DAMemory(token_id)
            elif value.startswith("StrRef"):
                token_id = int(value[6:])
                row_value = RowValueTLKMemory(token_id)
            elif value == "high()":
                row_value = (
                    RowValueHigh(None)
                    if modifier == "RowLabel"
                    else RowValueHigh(value)
                )
            elif value == "RowIndex":
                row_value = RowValueRowIndex()
            elif value == "RowLabel":
                row_value = RowValueRowLabel()
            elif is_store_2da or is_store_tlk:
                row_value = RowValueRowCell(value)
            elif value == "****":
                row_value = RowValueConstant("")
            else:
                row_value = RowValueConstant(value)

            if is_store_2da or is_store_tlk:
                token_id = int(modifier[9:]) if is_store_2da else int(modifier[6:])
                store = store_2da if is_store_2da else store_tlk
                store[token_id] = row_value
            elif is_row_label:
                ...
            else:
                cells[modifier] = row_value

        return cells, store_2da, store_tlk

    def row_label_2da(self, identifier: str, modifiers: dict[str, str]) -> str | None:
        if "RowLabel" in modifiers:
            return modifiers.pop("RowLabel")
        if "NewRowLabel" in modifiers:
            return modifiers.pop("NewRowLabel")
        return None

    def column_inserts_2da(
        self,
        identifier: str,
        modifiers: dict[str, str],
    ) -> tuple[dict[int, RowValue], dict[str, RowValue], dict[int, str]]:
        index_insert: dict[int, RowValue] = {}
        label_insert: dict[str, RowValue] = {}
        store_2da: dict[int, str] = {}

        for modifier, value in modifiers.items():
            is_store_2da = value.startswith("2DAMEMORY")
            is_store_tlk = value.startswith("StrRef")

            if is_store_2da:
                token_id = int(value[9:])
                row_value = RowValue2DAMemory(token_id)
            elif is_store_tlk:
                token_id = int(value[6:])
                row_value = RowValueTLKMemory(token_id)
            else:
                row_value = RowValueConstant(value)

            if modifier.startswith("I"):
                index = int(modifier[1:])
                index_insert[index] = row_value
            elif modifier.startswith("L"):
                label = modifier[1:]
                label_insert[label] = row_value
            elif modifier.startswith("2DAMEMORY"):
                token_id = int(modifier[9:])
                store_2da[token_id] = value

        return index_insert, label_insert, store_2da


# The `NamespaceReader` class is responsible for reading and loading namespaces from the namespaces.ini file.
class NamespaceReader:
    def __init__(self, ini: ConfigParser):
        self.ini = ini
        self.namespaces: list[PatcherNamespace] = []

    @classmethod
    def from_filepath(cls, path: str) -> list[PatcherNamespace]:
        ini_file_bytes = BinaryReader.load_file(path)

        detector = UniversalDetector()
        detector.feed(ini_file_bytes)
        detector.close()
        encoding = detector.result["encoding"]

        ini_text = ini_file_bytes.decode(encoding)

        ini = ConfigParser(
            delimiters=("="),
            allow_no_value=True,
            strict=False,
            interpolation=None,
        )
        ini.optionxform = str  # type: ignore[reportGeneralTypeIssues]  # use case sensitive keys
        ini.read_string(ini_text)
        return NamespaceReader(ini).load()

    def load(self) -> list[PatcherNamespace]:
        namespace_ids = dict(self.ini["Namespaces"].items()).values()
        self.ini = {key.lower(): value for key, value in self.ini.items()}
        namespaces: list[PatcherNamespace] = []

        for namespace_id in namespace_ids:
            namespace = PatcherNamespace()
            namespace_id = namespace_id.lower()
            namespace.namespace_id = namespace_id
            namespace.ini_filename = self.ini[namespace_id]["IniName"]
            namespace.info_filename = self.ini[namespace_id]["InfoName"]
            namespace.data_folderpath = self.ini[namespace_id].get("DataPath")
            namespace.name = self.ini[namespace_id].get("Name")
            namespace.description = self.ini[namespace_id].get("Description")
            namespaces.append(namespace)

        return namespaces
