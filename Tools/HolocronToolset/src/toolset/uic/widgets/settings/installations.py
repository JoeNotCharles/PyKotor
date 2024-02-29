# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\ui\widgets\settings\installations.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 243)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pathList = QtWidgets.QListView(Form)
        self.pathList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pathList.setObjectName("pathList")
        self.verticalLayout_2.addWidget(self.pathList)
        self.addPathButton = QtWidgets.QPushButton(Form)
        self.addPathButton.setObjectName("addPathButton")
        self.verticalLayout_2.addWidget(self.addPathButton)
        self.removePathButton = QtWidgets.QPushButton(Form)
        self.removePathButton.setObjectName("removePathButton")
        self.verticalLayout_2.addWidget(self.removePathButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pathFrame = QtWidgets.QFrame(Form)
        self.pathFrame.setEnabled(False)
        self.pathFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pathFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pathFrame.setObjectName("pathFrame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.pathFrame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_11 = QtWidgets.QLabel(self.pathFrame)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.pathNameEdit = QtWidgets.QLineEdit(self.pathFrame)
        self.pathNameEdit.setObjectName("pathNameEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pathNameEdit)
        self.label_12 = QtWidgets.QLabel(self.pathFrame)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.pathDirEdit = QtWidgets.QLineEdit(self.pathFrame)
        self.pathDirEdit.setObjectName("pathDirEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pathDirEdit)
        self.label_13 = QtWidgets.QLabel(self.pathFrame)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.pathTslCheckbox = QtWidgets.QCheckBox(self.pathFrame)
        self.pathTslCheckbox.setText("")
        self.pathTslCheckbox.setObjectName("pathTslCheckbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pathTslCheckbox)
        self.horizontalLayout.addWidget(self.pathFrame)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addPathButton.setText(_translate("Form", "Add"))
        self.removePathButton.setText(_translate("Form", "Remove"))
        self.label_11.setText(_translate("Form", "Name:"))
        self.label_12.setText(_translate("Form", "Path:"))
        self.label_13.setText(_translate("Form", "TSL:"))
