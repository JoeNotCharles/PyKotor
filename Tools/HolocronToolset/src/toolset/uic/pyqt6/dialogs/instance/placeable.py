# Form implementation generated from reading ui file '..\ui\dialogs\instance\placeable.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 151)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.resrefEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.resrefEdit.setMaximumSize(QtCore.QSize(187, 16777215))
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.resrefEdit)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xPosSpin = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.xPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.xPosSpin.setDecimals(6)
        self.xPosSpin.setMinimum(-1000000.0)
        self.xPosSpin.setMaximum(1000000.0)
        self.xPosSpin.setObjectName("xPosSpin")
        self.horizontalLayout.addWidget(self.xPosSpin)
        self.yPosSpin = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.yPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.yPosSpin.setDecimals(6)
        self.yPosSpin.setMinimum(-1000000.0)
        self.yPosSpin.setMaximum(1000000.0)
        self.yPosSpin.setObjectName("yPosSpin")
        self.horizontalLayout.addWidget(self.yPosSpin)
        self.zPosSpin = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.zPosSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.zPosSpin.setDecimals(6)
        self.zPosSpin.setMinimum(-1000000.0)
        self.zPosSpin.setMaximum(1000000.0)
        self.zPosSpin.setObjectName("zPosSpin")
        self.horizontalLayout.addWidget(self.zPosSpin)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.bearingSpin = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.bearingSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.bearingSpin.setDecimals(6)
        self.bearingSpin.setMinimum(-1000000.0)
        self.bearingSpin.setMaximum(1000000.0)
        self.bearingSpin.setObjectName("bearingSpin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bearingSpin)
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.color = QtWidgets.QLabel(parent=Dialog)
        self.color.setMinimumSize(QtCore.QSize(16, 16))
        self.color.setMaximumSize(QtCore.QSize(16, 16))
        self.color.setStyleSheet("background: black;")
        self.color.setText("")
        self.color.setObjectName("color")
        self.horizontalLayout_9.addWidget(self.color)
        self.colorSpin = LongSpinBox(parent=Dialog)
        self.colorSpin.setMinimumSize(QtCore.QSize(90, 0))
        self.colorSpin.setMaximumSize(QtCore.QSize(90, 16777215))
        self.colorSpin.setObjectName("colorSpin")
        self.horizontalLayout_9.addWidget(self.colorSpin)
        self.colorButton = QtWidgets.QPushButton(parent=Dialog)
        self.colorButton.setMaximumSize(QtCore.QSize(24, 20))
        self.colorButton.setObjectName("colorButton")
        self.horizontalLayout_9.addWidget(self.colorButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.formLayout)
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
        Dialog.setWindowTitle(_translate("Dialog", "Edit Placeable"))
        self.label.setText(_translate("Dialog", "ResRef:"))
        self.label_2.setText(_translate("Dialog", "Position:"))
        self.label_3.setText(_translate("Dialog", "Bearing:"))
        self.label_4.setText(_translate("Dialog", "Tweak Color:"))
        self.colorButton.setText(_translate("Dialog", "..."))
from toolset.gui.widgets.long_spinbox import LongSpinBox

from toolset.rcc import resources_rc_pyqt6
