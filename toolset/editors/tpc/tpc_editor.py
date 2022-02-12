from typing import Optional

from PyQt5.QtGui import QPixmap, QImage, QTransform, QIcon
from PyQt5.QtWidgets import QWidget
from pykotor.extract.installation import Installation
from pykotor.resource.formats.tpc import load_tpc, TPCTextureFormat, TPC, write_tpc
from pykotor.resource.type import ResourceType, FileFormat

from editors.editor import Editor
from editors.tpc import tpc_editor_ui


class TPCEditor(Editor):
    def __init__(self, parent: QWidget, installation: Optional[Installation] = None):
        super().__init__(parent, "Texture Viewer", [ResourceType.TPC, ResourceType.TGA], [ResourceType.TPC, ResourceType.TGA], installation)

        self.ui = tpc_editor_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self._setup_menus()

        iconVersion = "x" if installation is None else "2" if installation.tsl else "1"
        iconPath = ":/images/icons/k{}/none.png".format(iconVersion)
        self.setWindowIcon(QIcon(QPixmap(iconPath)))

        self._tpc: TPC = TPC()
        self._tpc.set_single(256, 256, bytes([0 for i in range(256*256*4)]), TPCTextureFormat.RGBA)

        self.new()

    def load(self, filepath: str, resref: str, restype: ResourceType, data: bytes) -> None:
        super().load(filepath, resref, restype, data)

        self._tpc = load_tpc(data)
        width, height, rgba = self._tpc.convert(TPCTextureFormat.RGB, 0)

        image = QImage(rgba, width, height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image).transformed(QTransform().scale(1, -1))

        self.ui.textureImage.setPixmap(pixmap)
        self.ui.txiEdit.setPlainText(self._tpc.txi)

    def new(self) -> None:
        super().new()

        self._tpc: TPC = TPC()
        self._tpc.set_single(256, 256, bytes([0 for i in range(256 * 256 * 4)]), TPCTextureFormat.RGBA)
        width, height, rgba = self._tpc.convert(TPCTextureFormat.RGBA, 0)

        image = QImage(rgba, width, height, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(image)
        self.ui.textureImage.setPixmap(pixmap)
        self.ui.txiEdit.setPlainText("")

    def build(self) -> bytes:
        self._tpc.txi = self.ui.txiEdit.toPlainText()

        data = bytearray()
        fileFormat = FileFormat.BINARY
        if self._restype == ResourceType.TGA:
            fileFormat = FileFormat.TGA

        write_tpc(self._tpc, data, fileFormat)
        return data
