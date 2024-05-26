# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\dialogs\insert_instance.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 447)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.resrefEdit = QtWidgets.QLineEdit(Dialog)
        self.resrefEdit.setEnabled(False)
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.resrefEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.locationSelect = QtWidgets.QComboBox(Dialog)
        self.locationSelect.setObjectName("locationSelect")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.locationSelect)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.reuseResourceRadio = QtWidgets.QRadioButton(Dialog)
        self.reuseResourceRadio.setChecked(True)
        self.reuseResourceRadio.setObjectName("reuseResourceRadio")
        self.horizontalLayout_2.addWidget(self.reuseResourceRadio)
        self.copyResourceRadio = QtWidgets.QRadioButton(Dialog)
        self.copyResourceRadio.setObjectName("copyResourceRadio")
        self.horizontalLayout_2.addWidget(self.copyResourceRadio)
        self.createResourceRadio = QtWidgets.QRadioButton(Dialog)
        self.createResourceRadio.setObjectName("createResourceRadio")
        self.horizontalLayout_2.addWidget(self.createResourceRadio)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resourceFilter = QtWidgets.QLineEdit(self.groupBox)
        self.resourceFilter.setObjectName("resourceFilter")
        self.verticalLayout_2.addWidget(self.resourceFilter)
        self.resourceList = QtWidgets.QListWidget(self.groupBox)
        self.resourceList.setObjectName("resourceList")
        self.verticalLayout_2.addWidget(self.resourceList)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insert Instance"))
        self.label.setText(_translate("Dialog", "ResRef:"))
        self.label_2.setText(_translate("Dialog", "Location:"))
        self.reuseResourceRadio.setText(_translate("Dialog", "Reuse Resource"))
        self.copyResourceRadio.setText(_translate("Dialog", "Copy Resource"))
        self.createResourceRadio.setText(_translate("Dialog", "Create Resource"))
        self.resourceFilter.setPlaceholderText(_translate("Dialog", "search..."))
        self.resourceList.setSortingEnabled(True)

from toolset.rcc import resources_rc_pyqt5
