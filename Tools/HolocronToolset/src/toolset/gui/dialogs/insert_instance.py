from __future__ import annotations

from typing import TYPE_CHECKING

import qtpy

from qtpy import QtCore
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QDialog, QDialogButtonBox, QListWidgetItem, QMessageBox

from pykotor.common.misc import ResRef
from pykotor.common.stream import BinaryWriter
from pykotor.resource.formats.erf import read_erf, write_erf
from pykotor.resource.formats.rim import read_rim, write_rim
from pykotor.resource.generics.utc import UTC, bytes_utc
from pykotor.resource.generics.utd import UTD, bytes_utd
from pykotor.resource.generics.ute import UTE, bytes_ute
from pykotor.resource.generics.utm import UTM, bytes_utm
from pykotor.resource.generics.utp import UTP, bytes_utp
from pykotor.resource.generics.uts import UTS, bytes_uts
from pykotor.resource.generics.utt import UTT, bytes_utt
from pykotor.resource.generics.utw import UTW, bytes_utw
from pykotor.resource.type import ResourceType
from pykotor.tools.misc import is_any_erf_type_file, is_rim_file
from toolset.gui.helpers.callback import BetterMessageBox
from toolset.gui.widgets.settings.installations import GlobalSettings
from utility.system.path import Path

if TYPE_CHECKING:
    from qtpy.QtWidgets import QWidget

    from pykotor.common.module import Module
    from pykotor.extract.file import FileResource
    from toolset.data.installation import HTInstallation


class InsertInstanceDialog(QDialog):
    def __init__(self, parent: QWidget, installation: HTInstallation, module: Module, restype: ResourceType):
        """Initialize a resource editor dialog.

        Args:
        ----
            parent: QWidget - Parent widget
            installation: HTInstallation - HT installation object
            module: Module - Module object
            restype: ResourceType - Resource type

        Initializes the resource editor dialog:
            - Sets up UI elements
            - Connects signal handlers
            - Populates resource list
            - Initializes location selector.
        """
        super().__init__(parent)

        self._installation: HTInstallation = installation
        self._module: Module = module
        self._restype: ResourceType = restype

        self.resname: str = ""
        self.data: bytes = b""
        self.filepath: Path | None = None

        if qtpy.API_NAME == "PySide2":
            from toolset.uic.pyside2.dialogs.insert_instance import Ui_Dialog  # noqa: PLC0415  # pylint: disable=C0415
        elif qtpy.API_NAME == "PySide6":
            from toolset.uic.pyside6.dialogs.insert_instance import Ui_Dialog  # noqa: PLC0415  # pylint: disable=C0415
        elif qtpy.API_NAME == "PyQt5":
            from toolset.uic.pyqt5.dialogs.insert_instance import Ui_Dialog  # noqa: PLC0415  # pylint: disable=C0415
        elif qtpy.API_NAME == "PyQt6":
            from toolset.uic.pyqt6.dialogs.insert_instance import Ui_Dialog  # noqa: PLC0415  # pylint: disable=C0415
        else:
            raise ImportError(f"Unsupported Qt bindings: {qtpy.API_NAME}")

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._setupSignals()
        self._setupLocationSelect()
        self._setupResourceList()

    def _setupSignals(self):
        self.ui.createResourceRadio.toggled.connect(self.onResourceRadioToggled)
        self.ui.reuseResourceRadio.toggled.connect(self.onResourceRadioToggled)
        self.ui.copyResourceRadio.toggled.connect(self.onResourceRadioToggled)
        self.ui.resrefEdit.textEdited.connect(self.onResRefEdited)
        self.ui.resourceFilter.textChanged.connect(self.onResourceFilterChanged)
        self.ui.resourceList.itemSelectionChanged.connect(self.onResourceSelected)

    def _setupLocationSelect(self):
        self.ui.locationSelect.addItem(str(self._installation.override_path()), self._installation.override_path())
        for capsule in self._module.capsules():
            if is_rim_file(capsule.filepath()) and GlobalSettings().disableRIMSaving:
                continue
            self.ui.locationSelect.addItem(str(capsule.filepath()), capsule.filepath())
        self.ui.locationSelect.setCurrentIndex(self.ui.locationSelect.count() - 1)

    def _setupResourceList(self):
        """Populates a resource list widget with available resources.

        Args:
        ----
            self: The class instance

        Processing Logic:
        ----------------
            - Loops through installation resources and adds matching type
            - Loops through module capsules and nested resources, adding matching type
            - Selects first item if list is populated.
        """
        for resource in self._installation.core_resources():
            if resource.restype() == self._restype:
                item = QListWidgetItem(resource.resname())
                item.setToolTip(str(resource.filepath()))
                item.setData(QtCore.Qt.ItemDataRole.UserRole, resource)
                self.ui.resourceList.addItem(item)

        for capsule in self._module.capsules():
            for resource in (resource for resource in capsule if resource.restype() == self._restype):
                if resource.restype() == self._restype:
                    item = QListWidgetItem(resource.resname())
                    item.setToolTip(str(resource.filepath()))
                    item.setForeground(QColor(30, 30, 30))
                    item.setData(QtCore.Qt.ItemDataRole.UserRole, resource)
                    self.ui.resourceList.addItem(item)

        if self.ui.resourceList.count() > 0:
            self.ui.resourceList.item(0).setSelected(True)

    def accept(self):
        """Accepts resource selection and updates module accordingly.

        Processing Logic:
        ----------------
            - Checks which radio button is selected for reuse, copy or create resource
            - Sets resource name, file path and data based on selection
            - Writes data to file if resource is new
            - Adds resource location to module.
        """
        super().accept()

        new = True
        if not self.ui.resourceList.selectedItems():
            BetterMessageBox("Choose an instance", "You must choose an instance, use the radial buttons to determine where/how to create the GIT instance.", icon=QMessageBox.Critical).exec_()
            return
        resource: FileResource = self.ui.resourceList.selectedItems()[0].data(QtCore.Qt.ItemDataRole.UserRole)

        if self.ui.reuseResourceRadio.isChecked():
            new = False
            self.resname = resource.resname()
            self.filepath = resource.filepath()
            self.data = resource.data()
        elif self.ui.copyResourceRadio.isChecked():
            self.resname = self.ui.resrefEdit.text()
            self.filepath = Path(self.ui.locationSelect.currentData())
            self.data = resource.data()
        elif self.ui.createResourceRadio.isChecked():
            self.resname = self.ui.resrefEdit.text()
            self.filepath = Path(self.ui.locationSelect.currentData())
            if self._restype is ResourceType.UTC:
                self.data = bytes_utc(UTC())
            elif self._restype is ResourceType.UTP:
                self.data = bytes_utp(UTP())
            elif self._restype is ResourceType.UTD:
                self.data = bytes_utd(UTD())
            elif self._restype is ResourceType.UTE:
                self.data = bytes_ute(UTE())
            elif self._restype is ResourceType.UTT:
                self.data = bytes_utt(UTT())
            elif self._restype is ResourceType.UTS:
                self.data = bytes_uts(UTS())
            elif self._restype is ResourceType.UTM:
                self.data = bytes_utm(UTM())
            elif self._restype is ResourceType.UTW:
                self.data = bytes_utw(UTW())
            else:
                self.data = b""

        if new and self.filepath:
            if is_any_erf_type_file(self.filepath.name):
                erf = read_erf(self.filepath)
                erf.set_data(self.resname, self._restype, self.data)
                write_erf(erf, self.filepath)
            elif is_rim_file(self.filepath.name):
                rim = read_rim(self.filepath)
                rim.set_data(self.resname, self._restype, self.data)
                write_rim(rim, self.filepath)
            else:
                self.filepath = Path(self.filepath) / f"{self.resname}.{self._restype.extension}"
                BinaryWriter.dump(self.filepath, self.data)

        assert self.filepath is not None
        self._module.add_locations(self.resname, self._restype, [self.filepath])

    def onResourceRadioToggled(self):
        self.ui.resourceList.setEnabled(not self.ui.createResourceRadio.isChecked())
        self.ui.resourceFilter.setEnabled(not self.ui.createResourceRadio.isChecked())
        self.ui.resrefEdit.setEnabled(not self.ui.reuseResourceRadio.isChecked())

        if self.ui.reuseResourceRadio.isChecked():
            self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(True)

        if self.ui.copyResourceRadio.isChecked():
            self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(self.isValidResref(self.ui.resrefEdit.text()))

        if self.ui.createResourceRadio.isChecked():
            self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(self.isValidResref(self.ui.resrefEdit.text()))

    def onResourceSelected(self):
        """Updates the dynamic text label when a resource is selected."""
        selected_items = self.ui.resourceList.selectedItems()
        if selected_items:
            resource: FileResource = selected_items[0].data(QtCore.Qt.ItemDataRole.UserRole)
            summary_text = self.generateResourceSummary(resource)
            self.ui.dynamicTextLabel.setText(summary_text)
            # pixmap = QPixmap("path/to/your/image.png")  # TODO
            # self.ui.imageLabel.setPixmap(pixmap)

    def generateResourceSummary(self, resource: FileResource) -> str:
        """Generates a summary of the selected resource.

        Args:
        ----
            resource: FileResource - The selected resource.

        Returns:
        -------
            str: Summary text.
        """
        summary = [
            f"Name: {resource.resname()}",
            f"Type: {resource.restype().name}",
            f"Size: {len(resource.data())} bytes",
            f"Path: {resource.filepath().relative_to(self._installation.path())}"
        ]
        return "\n".join(summary)

    def onResRefEdited(self, text: str):
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(self.isValidResref(text))

    def onResourceFilterChanged(self):
        text = self.ui.resourceFilter.text()
        for row in range(self.ui.resourceList.count()):
            item = self.ui.resourceList.item(row)
            item.setHidden(text not in item.text())

    def isValidResref(self, text: str) -> bool:
        return self._module.resource(text, self._restype) is None and ResRef.is_valid(text)
