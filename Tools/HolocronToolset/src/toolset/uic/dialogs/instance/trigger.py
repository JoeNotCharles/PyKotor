# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\ui\dialogs\instance\trigger.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(352, 241)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.resrefEdit = QtWidgets.QLineEdit(Dialog)
        self.resrefEdit.setMaximumSize(QtCore.QSize(187, 16777215))
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.resrefEdit)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.tagEdit = QtWidgets.QLineEdit(Dialog)
        self.tagEdit.setMaximumSize(QtCore.QSize(187, 16777215))
        self.tagEdit.setObjectName("tagEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tagEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xPosSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.xPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.xPosSpin.setDecimals(6)
        self.xPosSpin.setMinimum(-1000000.0)
        self.xPosSpin.setMaximum(1000000.0)
        self.xPosSpin.setObjectName("xPosSpin")
        self.horizontalLayout.addWidget(self.xPosSpin)
        self.yPosSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.yPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.yPosSpin.setDecimals(6)
        self.yPosSpin.setMinimum(-1000000.0)
        self.yPosSpin.setMaximum(1000000.0)
        self.yPosSpin.setObjectName("yPosSpin")
        self.horizontalLayout.addWidget(self.yPosSpin)
        self.zPosSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.zPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.zPosSpin.setDecimals(6)
        self.zPosSpin.setMinimum(-1000000.0)
        self.zPosSpin.setMaximum(1000000.0)
        self.zPosSpin.setObjectName("zPosSpin")
        self.horizontalLayout.addWidget(self.zPosSpin)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.noTransCheck = QtWidgets.QRadioButton(Dialog)
        self.noTransCheck.setObjectName("noTransCheck")
        self.horizontalLayout_2.addWidget(self.noTransCheck)
        self.toDoorCheck = QtWidgets.QRadioButton(Dialog)
        self.toDoorCheck.setObjectName("toDoorCheck")
        self.horizontalLayout_2.addWidget(self.toDoorCheck)
        self.toWaypointCheck = QtWidgets.QRadioButton(Dialog)
        self.toWaypointCheck.setObjectName("toWaypointCheck")
        self.horizontalLayout_2.addWidget(self.toWaypointCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.linkToModuleEdit = QtWidgets.QLineEdit(Dialog)
        self.linkToModuleEdit.setMaximumSize(QtCore.QSize(187, 16777215))
        self.linkToModuleEdit.setMaxLength(16)
        self.linkToModuleEdit.setObjectName("linkToModuleEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.linkToModuleEdit)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.linkToTagEdit = QtWidgets.QLineEdit(Dialog)
        self.linkToTagEdit.setMaximumSize(QtCore.QSize(187, 16777215))
        self.linkToTagEdit.setObjectName("linkToTagEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.linkToTagEdit)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.transNameEdit = LocalizedStringLineEdit(Dialog)
        self.transNameEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.transNameEdit.setMaximumSize(QtCore.QSize(219, 16777215))
        self.transNameEdit.setObjectName("transNameEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.transNameEdit)
        self.verticalLayout.addLayout(self.formLayout_2)
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
        Dialog.setWindowTitle(_translate("Dialog", "Edit Trigger"))
        self.label.setText(_translate("Dialog", "ResRef:"))
        self.label_8.setText(_translate("Dialog", "Tag:"))
        self.label_2.setText(_translate("Dialog", "Position:"))
        self.noTransCheck.setText(_translate("Dialog", "No Transition"))
        self.toDoorCheck.setText(_translate("Dialog", "Links to Door"))
        self.toWaypointCheck.setText(_translate("Dialog", "Links to Waypoint"))
        self.label_5.setText(_translate("Dialog", "Link To Module:"))
        self.label_6.setText(_translate("Dialog", "Link To Tag:"))
        self.label_7.setText(_translate("Dialog", "Transition Name:"))
from toolset.gui.widgets.edit.locstring import LocalizedStringLineEdit
