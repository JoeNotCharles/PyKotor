# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_module.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(336, 373)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filterEdit = QLineEdit(Dialog)
        self.filterEdit.setObjectName(u"filterEdit")

        self.verticalLayout.addWidget(self.filterEdit)

        self.moduleList = QListWidget(Dialog)
        self.moduleList.setObjectName(u"moduleList")

        self.verticalLayout.addWidget(self.moduleList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.browseButton = QPushButton(Dialog)
        self.browseButton.setObjectName(u"browseButton")

        self.horizontalLayout.addWidget(self.browseButton)

        self.openButton = QPushButton(Dialog)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.openButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Open Module", None))
        self.filterEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"filter...", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.browseButton.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.openButton.setText(QCoreApplication.translate("Dialog", u"Open", None))
    # retranslateUi


from toolset.rcc import resources_rc_pyside6
