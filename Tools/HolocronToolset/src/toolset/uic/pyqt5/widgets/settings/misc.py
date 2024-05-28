# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\widgets\settings\misc.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 334)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 314))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.saveRimCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.saveRimCheck.setObjectName("saveRimCheck")
        self.verticalLayout.addWidget(self.saveRimCheck)
        self.useBetaChannel = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.useBetaChannel.setObjectName("useBetaChannel")
        self.verticalLayout.addWidget(self.useBetaChannel)
        self.hBoxLayoutForSubOption = QtWidgets.QHBoxLayout()
        self.hBoxLayoutForSubOption.setContentsMargins(20, -1, -1, -1)
        self.hBoxLayoutForSubOption.setObjectName("hBoxLayoutForSubOption")
        self.alsoCheckReleaseVersion = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.alsoCheckReleaseVersion.setEnabled(True)
        self.alsoCheckReleaseVersion.setObjectName("alsoCheckReleaseVersion")
        self.hBoxLayoutForSubOption.addWidget(self.alsoCheckReleaseVersion)
        self.verticalLayout.addLayout(self.hBoxLayoutForSubOption)
        self.mergeRimCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.mergeRimCheck.setObjectName("mergeRimCheck")
        self.verticalLayout.addWidget(self.mergeRimCheck)
        self.attemptKeepOldGFFFields = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.attemptKeepOldGFFFields.setObjectName("attemptKeepOldGFFFields")
        self.verticalLayout.addWidget(self.attemptKeepOldGFFFields)
        self.moduleSortOptionComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.moduleSortOptionComboBox.setEditable(False)
        self.moduleSortOptionComboBox.setObjectName("moduleSortOptionComboBox")
        self.moduleSortOptionComboBox.addItem("")
        self.moduleSortOptionComboBox.addItem("")
        self.moduleSortOptionComboBox.addItem("")
        self.verticalLayout.addWidget(self.moduleSortOptionComboBox)
        self.greyRimCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.greyRimCheck.setObjectName("greyRimCheck")
        self.verticalLayout.addWidget(self.greyRimCheck)
        self.showPreviewUTCCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.showPreviewUTCCheck.setObjectName("showPreviewUTCCheck")
        self.verticalLayout.addWidget(self.showPreviewUTCCheck)
        self.showPreviewUTPCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.showPreviewUTPCheck.setObjectName("showPreviewUTPCheck")
        self.verticalLayout.addWidget(self.showPreviewUTPCheck)
        self.showPreviewUTDCheck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.showPreviewUTDCheck.setObjectName("showPreviewUTDCheck")
        self.verticalLayout.addWidget(self.showPreviewUTDCheck)
        self.profileToolset = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.profileToolset.setObjectName("profileToolset")
        self.verticalLayout.addWidget(self.profileToolset)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tempDirEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.tempDirEdit.setObjectName("tempDirEdit")
        self.horizontalLayout.addWidget(self.tempDirEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.gffEditorCombo = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.gffEditorCombo.setObjectName("gffEditorCombo")
        self.gffEditorCombo.addItem("")
        self.gffEditorCombo.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gffEditorCombo)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nssCompEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nssCompEdit.setEnabled(True)
        self.nssCompEdit.setObjectName("nssCompEdit")
        self.horizontalLayout_4.addWidget(self.nssCompEdit)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ncsToolEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ncsToolEdit.setEnabled(True)
        self.ncsToolEdit.setObjectName("ncsToolEdit")
        self.horizontalLayout_8.addWidget(self.ncsToolEdit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(17, 139, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveRimCheck.setText(_translate("Form", "Allow saving resources to RIM files."))
        self.useBetaChannel.setText(_translate("Form", "Check for beta updates and take me to their download link when they\'re available."))
        self.alsoCheckReleaseVersion.setText(_translate("Form", "Also check release version if it is newer than beta version."))
        self.mergeRimCheck.setText(_translate("Form", "Merge secondary ERF/RIM\'s in the Modules tab of the Main Window (i.e. \'_s.rim\' and \'_dlg.erf\')."))
        self.attemptKeepOldGFFFields.setText(_translate("Form", "Attempts to keep any pre-existing GFF fields when saving the editor. Required for save editing."))
        self.moduleSortOptionComboBox.setItemText(0, _translate("Form", "Sort by filename"))
        self.moduleSortOptionComboBox.setItemText(1, _translate("Form", "Sort by humanized area name"))
        self.moduleSortOptionComboBox.setItemText(2, _translate("Form", "Sort by area name"))
        self.greyRimCheck.setText(_translate("Form", "Set RIM files to have grey text in the Modules tab of the Main Window."))
        self.showPreviewUTCCheck.setText(_translate("Form", "Show 3D Preview in UTC Editor"))
        self.showPreviewUTPCheck.setText(_translate("Form", "Show 3D Preview in UTP Editor"))
        self.showPreviewUTDCheck.setText(_translate("Form", "Show 3D Preview in UTD Editor"))
        self.profileToolset.setText(_translate("Form", "Profile various subroutines of the toolset."))
        self.label.setText(_translate("Form", "Temp Directory:"))
        self.label_5.setText(_translate("Form", "GFF Files:"))
        self.gffEditorCombo.setItemText(0, _translate("Form", "GFF Editor"))
        self.gffEditorCombo.setItemText(1, _translate("Form", "Specialized Editor"))
        self.label_4.setText(_translate("Form", "NSS Compiler:"))
        self.label_10.setText(_translate("Form", "NCS Decompiler:"))

from toolset.rcc import resources_rc_pyqt5
