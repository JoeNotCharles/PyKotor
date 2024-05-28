# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/dialogs/instance/camera.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 222)
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xPosSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.xPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.xPosSpin.setDecimals(6)
        self.xPosSpin.setMinimum(-100000.0)
        self.xPosSpin.setMaximum(100000.0)
        self.xPosSpin.setObjectName("xPosSpin")
        self.horizontalLayout.addWidget(self.xPosSpin)
        self.yPosSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.yPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.yPosSpin.setDecimals(6)
        self.yPosSpin.setMinimum(-100000.0)
        self.yPosSpin.setMaximum(100000.0)
        self.yPosSpin.setObjectName("yPosSpin")
        self.horizontalLayout.addWidget(self.yPosSpin)
        self.zPosSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.zPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.zPosSpin.setDecimals(6)
        self.zPosSpin.setMinimum(-100000.0)
        self.zPosSpin.setMaximum(100000.0)
        self.zPosSpin.setObjectName("zPosSpin")
        self.horizontalLayout.addWidget(self.zPosSpin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.xOrientSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.xOrientSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.xOrientSpin.setDecimals(6)
        self.xOrientSpin.setMinimum(-1000000.0)
        self.xOrientSpin.setMaximum(1000000.0)
        self.xOrientSpin.setObjectName("xOrientSpin")
        self.horizontalLayout_2.addWidget(self.xOrientSpin)
        self.yOrientSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.yOrientSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.yOrientSpin.setDecimals(6)
        self.yOrientSpin.setMinimum(-1000000.0)
        self.yOrientSpin.setMaximum(1000000.0)
        self.yOrientSpin.setObjectName("yOrientSpin")
        self.horizontalLayout_2.addWidget(self.yOrientSpin)
        self.zOrientSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.zOrientSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.zOrientSpin.setDecimals(6)
        self.zOrientSpin.setMinimum(-1000000.0)
        self.zOrientSpin.setMaximum(1000000.0)
        self.zOrientSpin.setObjectName("zOrientSpin")
        self.horizontalLayout_2.addWidget(self.zOrientSpin)
        self.wOrientSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.wOrientSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.wOrientSpin.setDecimals(6)
        self.wOrientSpin.setMinimum(-1000000.0)
        self.wOrientSpin.setMaximum(1000000.0)
        self.wOrientSpin.setObjectName("wOrientSpin")
        self.horizontalLayout_2.addWidget(self.wOrientSpin)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.cameraIdSpin = QtWidgets.QSpinBox(Dialog)
        self.cameraIdSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.cameraIdSpin.setMaximum(255)
        self.cameraIdSpin.setObjectName("cameraIdSpin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cameraIdSpin)
        self.fovSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.fovSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.fovSpin.setDecimals(6)
        self.fovSpin.setMinimum(20.0)
        self.fovSpin.setMaximum(200.0)
        self.fovSpin.setProperty("value", 50.0)
        self.fovSpin.setObjectName("fovSpin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fovSpin)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.pitchSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.pitchSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pitchSpin.setDecimals(6)
        self.pitchSpin.setMaximum(360.0)
        self.pitchSpin.setObjectName("pitchSpin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pitchSpin)
        self.micRangeSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.micRangeSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.micRangeSpin.setDecimals(6)
        self.micRangeSpin.setMaximum(100000.0)
        self.micRangeSpin.setObjectName("micRangeSpin")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.micRangeSpin)
        self.heightSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.heightSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.heightSpin.setDecimals(6)
        self.heightSpin.setMinimum(-100000.0)
        self.heightSpin.setMaximum(100000.0)
        self.heightSpin.setObjectName("heightSpin")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.heightSpin)
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
        Dialog.setWindowTitle(_translate("Dialog", "Edit Camera"))
        self.label.setText(_translate("Dialog", "Camera ID:"))
        self.label_2.setText(_translate("Dialog", "Position:"))
        self.label_3.setText(_translate("Dialog", "Orientation:"))
        self.label_4.setText(_translate("Dialog", "FOV:"))
        self.label_5.setText(_translate("Dialog", "Pitch:"))
        self.label_6.setText(_translate("Dialog", "Mic Range:"))
        self.label_7.setText(_translate("Dialog", "Height:"))

from toolset.rcc import resources_rc_pyqt5
