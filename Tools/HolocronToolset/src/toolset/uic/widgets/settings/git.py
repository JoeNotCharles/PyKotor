# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\ui\widgets\settings\git.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(466, 773)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 920))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.controlsResetButton = QtWidgets.QPushButton(self.groupBox)
        self.controlsResetButton.setObjectName("controlsResetButton")
        self.horizontalLayout_3.addWidget(self.controlsResetButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.moveCameraBindEdit = SetBindWidget(self.groupBox)
        self.moveCameraBindEdit.setObjectName("moveCameraBindEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.moveCameraBindEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rotateCameraBindEdit = SetBindWidget(self.groupBox)
        self.rotateCameraBindEdit.setObjectName("rotateCameraBindEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rotateCameraBindEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.zoomCameraBindEdit = SetBindWidget(self.groupBox)
        self.zoomCameraBindEdit.setObjectName("zoomCameraBindEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zoomCameraBindEdit)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.selectUnderneathBindEdit = SetBindWidget(self.groupBox)
        self.selectUnderneathBindEdit.setObjectName("selectUnderneathBindEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.selectUnderneathBindEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.rotateSelectedToPointBindEdit = SetBindWidget(self.groupBox)
        self.rotateSelectedToPointBindEdit.setObjectName("rotateSelectedToPointBindEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rotateSelectedToPointBindEdit)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.deleteSelectedBindEdit = SetBindWidget(self.groupBox)
        self.deleteSelectedBindEdit.setObjectName("deleteSelectedBindEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.deleteSelectedBindEdit)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.duplicateSelectedBindEdit = SetBindWidget(self.groupBox)
        self.duplicateSelectedBindEdit.setObjectName("duplicateSelectedBindEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.duplicateSelectedBindEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.toggleLockInstancesBindEdit = SetBindWidget(self.groupBox)
        self.toggleLockInstancesBindEdit.setObjectName("toggleLockInstancesBindEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.toggleLockInstancesBindEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.undefinedMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.undefinedMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.undefinedMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.undefinedMaterialColourEdit.setObjectName("undefinedMaterialColourEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.undefinedMaterialColourEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setObjectName("label_25")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setObjectName("label_26")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setObjectName("label_28")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setObjectName("label_29")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.dirtMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.dirtMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.dirtMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dirtMaterialColourEdit.setObjectName("dirtMaterialColourEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dirtMaterialColourEdit)
        self.obscuringMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.obscuringMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.obscuringMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.obscuringMaterialColourEdit.setObjectName("obscuringMaterialColourEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.obscuringMaterialColourEdit)
        self.grassMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.grassMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.grassMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.grassMaterialColourEdit.setObjectName("grassMaterialColourEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.grassMaterialColourEdit)
        self.stoneMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.stoneMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.stoneMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.stoneMaterialColourEdit.setObjectName("stoneMaterialColourEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.stoneMaterialColourEdit)
        self.woodMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.woodMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.woodMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.woodMaterialColourEdit.setObjectName("woodMaterialColourEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.woodMaterialColourEdit)
        self.waterMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.waterMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.waterMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.waterMaterialColourEdit.setObjectName("waterMaterialColourEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.waterMaterialColourEdit)
        self.nonWalkMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.nonWalkMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.nonWalkMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nonWalkMaterialColourEdit.setObjectName("nonWalkMaterialColourEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.nonWalkMaterialColourEdit)
        self.transparentMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.transparentMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.transparentMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.transparentMaterialColourEdit.setObjectName("transparentMaterialColourEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.transparentMaterialColourEdit)
        self.carpetMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.carpetMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.carpetMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.carpetMaterialColourEdit.setObjectName("carpetMaterialColourEdit")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.carpetMaterialColourEdit)
        self.metalMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.metalMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.metalMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.metalMaterialColourEdit.setObjectName("metalMaterialColourEdit")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.metalMaterialColourEdit)
        self.puddlesMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.puddlesMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.puddlesMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.puddlesMaterialColourEdit.setObjectName("puddlesMaterialColourEdit")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.puddlesMaterialColourEdit)
        self.swampMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.swampMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.swampMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.swampMaterialColourEdit.setObjectName("swampMaterialColourEdit")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.swampMaterialColourEdit)
        self.mudMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.mudMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.mudMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.mudMaterialColourEdit.setObjectName("mudMaterialColourEdit")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.mudMaterialColourEdit)
        self.leavesMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.leavesMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.leavesMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.leavesMaterialColourEdit.setObjectName("leavesMaterialColourEdit")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.leavesMaterialColourEdit)
        self.lavaMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.lavaMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lavaMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lavaMaterialColourEdit.setObjectName("lavaMaterialColourEdit")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.lavaMaterialColourEdit)
        self.bottomlessPitMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.bottomlessPitMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.bottomlessPitMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.bottomlessPitMaterialColourEdit.setObjectName("bottomlessPitMaterialColourEdit")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.bottomlessPitMaterialColourEdit)
        self.deepWaterMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.deepWaterMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.deepWaterMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.deepWaterMaterialColourEdit.setObjectName("deepWaterMaterialColourEdit")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.deepWaterMaterialColourEdit)
        self.doorMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.doorMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.doorMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.doorMaterialColourEdit.setObjectName("doorMaterialColourEdit")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.doorMaterialColourEdit)
        self.nonWalkGrassMaterialColourEdit = ColorEdit(self.groupBox_2)
        self.nonWalkGrassMaterialColourEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.nonWalkGrassMaterialColourEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nonWalkGrassMaterialColourEdit.setObjectName("nonWalkGrassMaterialColourEdit")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.nonWalkGrassMaterialColourEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.coloursResetButton = QtWidgets.QPushButton(self.groupBox_2)
        self.coloursResetButton.setObjectName("coloursResetButton")
        self.horizontalLayout.addWidget(self.coloursResetButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Controls"))
        self.controlsResetButton.setText(_translate("Form", "Reset"))
        self.label.setText(_translate("Form", "Move Camera:"))
        self.label_2.setText(_translate("Form", "Rotate Camera:"))
        self.label_3.setText(_translate("Form", "Zoom Camera:"))
        self.label_5.setText(_translate("Form", "Select Object:"))
        self.label_4.setText(_translate("Form", "Rotate Object:"))
        self.label_6.setText(_translate("Form", "Delete Object:"))
        self.label_7.setText(_translate("Form", "Duplicate Object:"))
        self.label_8.setText(_translate("Form", "Toggle Instance Lock:"))
        self.groupBox_2.setTitle(_translate("Form", "Walkmesh Colours"))
        self.label_10.setText(_translate("Form", "Undefined:"))
        self.label_11.setText(_translate("Form", "Dirt:"))
        self.label_12.setText(_translate("Form", "Leaves:"))
        self.label_13.setText(_translate("Form", "Mud:"))
        self.label_14.setText(_translate("Form", "Swamp:"))
        self.label_15.setText(_translate("Form", "Puddles:"))
        self.label_16.setText(_translate("Form", "Metal:"))
        self.label_17.setText(_translate("Form", "Carpet:"))
        self.label_18.setText(_translate("Form", "Transparent:"))
        self.label_19.setText(_translate("Form", "Non-Walk:"))
        self.label_20.setText(_translate("Form", "Water:"))
        self.label_21.setText(_translate("Form", "Wood:"))
        self.label_22.setText(_translate("Form", "Stone:"))
        self.label_23.setText(_translate("Form", "Grass:"))
        self.label_24.setText(_translate("Form", "Obscuring:"))
        self.label_25.setText(_translate("Form", "Lava:"))
        self.label_26.setText(_translate("Form", "Bottomless Pit:"))
        self.label_27.setText(_translate("Form", "Deep Water:"))
        self.label_28.setText(_translate("Form", "Door:"))
        self.label_29.setText(_translate("Form", "Non-Walk Grass:"))
        self.coloursResetButton.setText(_translate("Form", "Reset"))


from toolset.gui.widgets.edit.color import ColorEdit
from toolset.gui.widgets.set_bind import SetBindWidget
