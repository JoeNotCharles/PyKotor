# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/dialogs/instance/creature.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 122)
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
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
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.bearingSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.bearingSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.bearingSpin.setDecimals(6)
        self.bearingSpin.setMinimum(-1000000.0)
        self.bearingSpin.setMaximum(1000000.0)
        self.bearingSpin.setObjectName("bearingSpin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bearingSpin)
        self.verticalLayout.addLayout(self.formLayout)
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
        Dialog.setWindowTitle(_translate("Dialog", "Edit Creature"))
        self.label.setText(_translate("Dialog", "ResRef:"))
        self.label_2.setText(_translate("Dialog", "Position:"))
        self.label_3.setText(_translate("Dialog", "Rotation:"))

from toolset.rcc import resources_rc_pyqt5
