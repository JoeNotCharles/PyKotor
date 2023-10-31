import os
from typing import Any, Dict

from data.settings import Settings
from PyQt5 import QtCore
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget

from pykotor.common.misc import Game
from pykotor.tools.path import locate_game_path


class InstallationsWidget(QWidget):
    edited = QtCore.pyqtSignal()

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.installationsModel: QStandardItemModel = QStandardItemModel()
        self.settings = GlobalSettings()

        from toolset.uic.widgets.settings import installations
        self.ui = installations.Ui_Form()
        self.ui.setupUi(self)
        self.setupValues()
        self.setupSignals()

    def setupValues(self) -> None:
        self.installationsModel.clear()
        for installation in self.settings.installations().values():
            item = QStandardItem(installation.name)
            item.setData({"path": installation.path, "tsl": installation.tsl})
            self.installationsModel.appendRow(item)

    def setupSignals(self) -> None:
        self.ui.pathList.setModel(self.installationsModel)

        self.ui.addPathButton.clicked.connect(self.addNewInstallation)
        self.ui.removePathButton.clicked.connect(self.removeSelectedInstallation)
        self.ui.pathNameEdit.textEdited.connect(self.updateInstallation)
        self.ui.pathDirEdit.textEdited.connect(self.updateInstallation)
        self.ui.pathTslCheckbox.stateChanged.connect(self.updateInstallation)
        self.ui.pathList.selectionModel().selectionChanged.connect(self.installationSelected)

    def save(self) -> None:
        installations = {}

        for row in range(self.installationsModel.rowCount()):
            item = self.installationsModel.item(row, 0)
            installations[item.text()] = item.data()
            installations[item.text()]["name"] = item.text()

        self.settings.settings.setValue("installations", installations)

    def addNewInstallation(self) -> None:
        item = QStandardItem("New")
        item.setData({"path": "", "tsl": False})
        self.installationsModel.appendRow(item)
        self.edited.emit()

    def removeSelectedInstallation(self) -> None:
        if len(self.ui.pathList.selectedIndexes()) > 0:
            index = self.ui.pathList.selectedIndexes()[0]
            item = self.installationsModel.itemFromIndex(index)
            self.installationsModel.removeRow(item.row())
            self.edited.emit()

        if len(self.ui.pathList.selectedIndexes()) == 0:
            self.ui.pathFrame.setEnabled(False)

    def updateInstallation(self) -> None:
        index = self.ui.pathList.selectedIndexes()[0]
        item = self.installationsModel.itemFromIndex(index)

        data = item.data()
        data["path"] = self.ui.pathDirEdit.text()
        data["tsl"] = self.ui.pathTslCheckbox.isChecked()
        item.setData(data)

        item.setText(self.ui.pathNameEdit.text())

        self.edited.emit()

    def installationSelected(self) -> None:
        if len(self.ui.pathList.selectedIndexes()) > 0:
            self.ui.pathFrame.setEnabled(True)

            index = self.ui.pathList.selectedIndexes()[0]
            item = self.installationsModel.itemFromIndex(index)

            self.ui.pathNameEdit.setText(item.text())
            self.ui.pathDirEdit.setText(item.data()["path"])
            self.ui.pathTslCheckbox.setChecked(bool(item.data()["tsl"]))


class InstallationConfig:
    def __init__(self, name: str):
        self._settings = QSettings("HolocronToolset", "Global")
        self._name: str = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        installations = self._settings.value("installations", {}, Dict[str, Any])
        installation = installations[self._name]

        del installations[self._name]
        installations[value] = installation
        installations[value]["name"] = value

        self._settings.setValue("installations", installations)
        self._name = value

    @property
    def path(self) -> str:
        installation = self._settings.value("installations", {})[self._name]
        return installation["path"]

    @path.setter
    def path(self, value: str) -> None:
        installations = self._settings.value("installations", {})
        installations[self._name]["path"] = value
        self._settings.setValue("installations", installations)

    @property
    def tsl(self) -> bool:
        installation = self._settings.value("installations", {})[self._name]
        return installation["tsl"]

    @tsl.setter
    def tsl(self, value: bool) -> None:
        installations = self._settings.value("installations", {})
        installations[self._name]["tsl"] = value
        self._settings.setValue("installations", installations)


class GlobalSettings(Settings):
    def __init__(self):
        super().__init__("Global")

    def installations(self) -> Dict[str, InstallationConfig]:
        if self.settings.value("installations", None) is None:
            default_paths = locate_game_path()
            entries = {}
            k1_index = 0
            k2_index = 0
            for game, paths in default_paths.items():
                for path in paths:
                    if not path.exists():
                        continue
                    game_name = "KotOR" if game==Game.K1 else "TSL"
                    if game==Game.K1:
                        if k1_index:
                            game_name += f" ({k1_index})"
                            k1_index += 1
                        k1_index += 1
                    if k2_index and game==Game.K2:
                        if k2_index:
                            game_name += f" ({k2_index})"
                            k2_index += 1
                        k2_index += 1
                    entry = {game_name: {"name": game_name, "path": str(path), "tsl": game==Game.K2}}
                    entries.update(entry)
            self.settings.setValue("installations", entries)

        installations = {}
        for name in self.settings.value("installations", {}):
            installations[name] = InstallationConfig(name)

        return installations

    # region Strings
    extractPath = Settings._addSetting(
        "extractPath",
        "",
    )
    nssCompilerPath = Settings._addSetting(
        "nssCompilerPath",
        "ext/nwnnsscomp.exe" if os.name == "nt" else "ext/nwnnsscomp"
    )
    ncsDecompilerPath = Settings._addSetting(
        "ncsDecompilerPath",
        "",
    )
    # endregion

    # region Bools
    disableRIMSaving = Settings._addSetting(
        "disableRIMSaving",
        True,
    )
    firstTime = Settings._addSetting(
        "firstTime",
        True,
    )
    gff_specializedEditors = Settings._addSetting(
        "gff_specializedEditors",
        True,
    )
    joinRIMsTogether = Settings._addSetting(
        "joinRIMsTogether",
        False,
    )
    greyRIMText = Settings._addSetting(
        "greyRIMText",
        True,
    )
    showPreviewUTC = Settings._addSetting(
        "showPreviewUTC",
        True,
    )
    showPreviewUTP = Settings._addSetting(
        "showPreviewUTP",
        True,
    )
    showPreviewUTD = Settings._addSetting(
        "showPreviewUTD",
        True,
    )
    # endregion


class NoConfigurationSetError(Exception):
    ...
