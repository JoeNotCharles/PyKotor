# Form implementation generated from reading ui file '..\ui\dialogs\locstring.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 214)
        Dialog.setMinimumSize(QtCore.QSize(300, 150))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.stringrefSpin = QtWidgets.QSpinBox(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stringrefSpin.sizePolicy().hasHeightForWidth())
        self.stringrefSpin.setSizePolicy(sizePolicy)
        self.stringrefSpin.setMinimum(-1)
        self.stringrefSpin.setMaximum(999999999)
        self.stringrefSpin.setObjectName("stringrefSpin")
        self.horizontalLayout_2.addWidget(self.stringrefSpin)
        self.stringrefNewButton = QtWidgets.QPushButton(parent=self.frame)
        self.stringrefNewButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.stringrefNewButton.setObjectName("stringrefNewButton")
        self.horizontalLayout_2.addWidget(self.stringrefNewButton)
        self.stringrefNoneButton = QtWidgets.QPushButton(parent=self.frame)
        self.stringrefNoneButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.stringrefNoneButton.setObjectName("stringrefNoneButton")
        self.horizontalLayout_2.addWidget(self.stringrefNoneButton)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.substringFrame = QtWidgets.QFrame(parent=Dialog)
        self.substringFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.substringFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.substringFrame.setObjectName("substringFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.substringFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.languageSelect = QtWidgets.QComboBox(parent=self.substringFrame)
        self.languageSelect.setMinimumSize(QtCore.QSize(160, 0))
        self.languageSelect.setObjectName("languageSelect")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.languageSelect.addItem("")
        self.horizontalLayout.addWidget(self.languageSelect)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.maleRadio = QtWidgets.QRadioButton(parent=self.substringFrame)
        self.maleRadio.setChecked(True)
        self.maleRadio.setObjectName("maleRadio")
        self.horizontalLayout.addWidget(self.maleRadio)
        self.femaleRadio = QtWidgets.QRadioButton(parent=self.substringFrame)
        self.femaleRadio.setObjectName("femaleRadio")
        self.horizontalLayout.addWidget(self.femaleRadio)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addWidget(self.substringFrame)
        self.stringEdit = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.stringEdit.setObjectName("stringEdit")
        self.verticalLayout.addWidget(self.stringEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Localized String"))
        self.label_2.setText(_translate("Dialog", "StringRef:"))
        self.stringrefNewButton.setText(_translate("Dialog", "New"))
        self.stringrefNoneButton.setText(_translate("Dialog", "None"))
        self.languageSelect.setItemText(0, _translate("Dialog", "English"))
        self.languageSelect.setItemText(1, _translate("Dialog", "French"))
        self.languageSelect.setItemText(2, _translate("Dialog", "German"))
        self.languageSelect.setItemText(3, _translate("Dialog", "Italian"))
        self.languageSelect.setItemText(4, _translate("Dialog", "Spanish"))
        self.languageSelect.setItemText(5, _translate("Dialog", "Polish"))
        self.maleRadio.setText(_translate("Dialog", "Male"))
        self.femaleRadio.setText(_translate("Dialog", "Female"))
