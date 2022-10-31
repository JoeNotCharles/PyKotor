from configparser import ConfigParser
from typing import Dict, Optional

from pykotor.resource.formats.tlk import TLK, read_tlk
from pykotor.tslpatcher.config import PatcherConfig
from pykotor.tslpatcher.mods.tlk import ModifyTLK
from pykotor.tslpatcher.mods.twoda import Modify2DA, ChangeRow2DA, Target, TargetType, WarningException, AddRow2DA, \
    CopyRow2DA, AddColumn2DA, Modifications2DA, RowValue2DAMemory, RowValueTLKMemory, RowValueHigh, RowValueRowIndex, \
    RowValueRowLabel, RowValueConstant, RowValueRowCell


class ConfigReader:
    def __init__(self, ini: ConfigParser, append: TLK) -> None:
        self.ini = ini
        self.append: TLK = append

        self.config: Optional[PatcherConfig] = None

    def load(self, config: PatcherConfig) -> PatcherConfig:
        #self.ini.optionxform = str
        #self.ini.read(config.input_path + "/changes.ini")
        #self.append: TLK = read_tlk(config.input_path + "/append.tlk")

        self.config = config

        self.load_stringref()
        self.load_2da()

        return self.config

    def load_stringref(self) -> None:
        if "TLKList" not in self.ini:
            return

        stringrefs = dict(self.ini["TLKList"].items())

        for name, value in stringrefs.items():
            token_id = int(name[6:])
            append_index = int(value)
            entry = self.append.get(append_index)

            modifier = ModifyTLK(token_id, entry.text, entry.voiceover)
            self.config.patches_tlk.modifiers.append(modifier)

    def load_2da(self) -> None:
        if "2DAList" not in self.ini:
            return

        files = dict(self.ini["2DAList"].items())

        for file in files.values():
            modification_ids = dict(self.ini[file].items())

            modificaitons = Modifications2DA(file)
            self.config.patches_2da.append(modificaitons)

            for key, modification_id in modification_ids.items():
                manipulation = self.discern_2da(key, modification_id, dict(self.ini[modification_id].items()))
                modificaitons.modifiers.append(manipulation)

    def discern_2da(self, key: str, identifier: str, modifiers: Dict[str, str]) -> Modify2DA:
        if key.startswith("ChangeRow"):
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
                raise WarningException("No line set to be modified for '{}'.".format(identifier))

            cells = {}
            store_2da = {}
            store_tlk = {}

            for modifier, value in modifiers.items():
                is_store_2da = modifier.startswith("2DAMEMORY")
                is_store_tlk = modifier.startswith("StrRef")
                is_row_label = modifier == "RowLabel" or modifier == "NewRowLabel"

                if value.startswith("2DAMEMORY"):
                    token_id = int(value[9:])
                    row_value = RowValue2DAMemory(token_id)
                elif value.startswith("StrRef"):
                    token_id = int(value[6:])
                    row_value = RowValueTLKMemory(token_id)
                elif value == "high()":
                    row_value = RowValueHigh(None) if modifier == "RowLabel" else RowValueHigh(value)
                elif value == "RowIndex":
                    row_value = RowValueRowIndex()
                elif value == "RowLabel":
                    row_value = RowValueRowLabel()
                elif is_store_2da or is_store_tlk:
                    row_value = RowValueRowCell(value)
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

            manipulation = ChangeRow2DA(identifier, target, cells, store_2da, store_tlk)
        else:
            raise WarningException()
        '''elif key.startswith("AddRow"):
            manipulation = AddRow2DA()
            manipulation.identifier = identifier
            manipulation.exclusive_column = modifiers.pop("ExclusiveColumn", None)
            manipulation.modifiers = modifiers
        elif key.startswith("CopyRow"):
            manipulation = CopyRow2DA()
            manipulation.identifier = identifier
            manipulation.target = self.target_2da(modifiers)
            manipulation.exclusive_column = modifiers.pop("ExclusiveColumn", None)
            manipulation.modifiers = modifiers
        elif key.startswith("AddColumn"):
            manipulation = AddColumn2DA()
            manipulation.identifier = identifier
            manipulation.header = modifiers.pop("ColumnLabel")
            manipulation.default = modifiers.pop("DefaultValue")
            for modifier in modifiers:
                if modifier.startswith("I"):
                    manipulation.index_insert[int(modifier[1:])] = modifiers[modifier]
                elif modifier.startswith("L"):
                    manipulation.label_insert[modifier[1:]] = modifiers[modifier]
                elif modifier.startswith("2DAMEMORY"):
                    memory_index = int(modifier.replace("2DAMEMORY", ""))
                    manipulation.memory_saves[memory_index] = modifiers[modifier]'''

        return manipulation

    def target_2da(self, modifiers: Dict[str, str]) -> Target:
        if "RowIndex" in modifiers:
            target = Target(TargetType.ROW_INDEX, int(modifiers.pop("RowIndex")))
        elif "RowLabel" in modifiers:
            target = Target(TargetType.ROW_LABEL, modifiers.pop("RowLabel"))
        elif "LabelIndex" in modifiers:
            target = Target(TargetType.LABEL_COLUMN, modifiers.pop("LabelIndex"))
        else:
            raise WarningException()

        return target
