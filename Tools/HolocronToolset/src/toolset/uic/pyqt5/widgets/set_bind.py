# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\widgets\set_bind.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(354, 41)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mouseCombo = QtWidgets.QComboBox(Form)
        self.mouseCombo.setMinimumSize(QtCore.QSize(80, 0))
        self.mouseCombo.setObjectName("mouseCombo")
        self.mouseCombo.addItem("")
        self.mouseCombo.addItem("")
        self.mouseCombo.addItem("")
        self.mouseCombo.addItem("")
        self.mouseCombo.addItem("")
        self.horizontalLayout.addWidget(self.mouseCombo)
        self.setKeysEdit = QtWidgets.QLineEdit(Form)
        self.setKeysEdit.setReadOnly(True)
        self.setKeysEdit.setObjectName("setKeysEdit")
        self.horizontalLayout.addWidget(self.setKeysEdit)
        self.setButton = QtWidgets.QPushButton(Form)
        self.setButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.setButton.setObjectName("setButton")
        self.horizontalLayout.addWidget(self.setButton)
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mouseCombo.setItemText(0, _translate("Form", "Left"))
        self.mouseCombo.setItemText(1, _translate("Form", "Middle"))
        self.mouseCombo.setItemText(2, _translate("Form", "Right"))
        self.mouseCombo.setItemText(3, _translate("Form", "Any"))
        self.mouseCombo.setItemText(4, _translate("Form", "None"))
        self.setKeysEdit.setPlaceholderText(_translate("Form", "none"))
        self.setButton.setText(_translate("Form", "Set"))
        self.clearButton.setText(_translate("Form", "Clear"))

from toolset.rcc import resources_rc_pyqt5
