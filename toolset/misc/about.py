from PyQt5.QtWidgets import QDialog, QWidget

from config import PROGRAM_VERSION


class About(QDialog):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        from misc import ui_about
        self.ui = ui_about.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.closeButton.clicked.connect(self.close)

        self.ui.aboutLabel.setText(self.ui.aboutLabel.text().replace("X.X.X", PROGRAM_VERSION))
