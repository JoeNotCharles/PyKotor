# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\dialogs\search.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 391)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.installationSelect = QtWidgets.QComboBox(self.groupBox)
        self.installationSelect.setObjectName("installationSelect")
        self.gridLayout.addWidget(self.installationSelect, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.searchTextEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.searchTextEdit.setObjectName("searchTextEdit")
        self.gridLayout_2.addWidget(self.searchTextEdit, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.coreCheck = QtWidgets.QCheckBox(self.groupBox_4)
        self.coreCheck.setChecked(True)
        self.coreCheck.setObjectName("coreCheck")
        self.verticalLayout_2.addWidget(self.coreCheck)
        self.modulesCheck = QtWidgets.QCheckBox(self.groupBox_4)
        self.modulesCheck.setChecked(True)
        self.modulesCheck.setObjectName("modulesCheck")
        self.verticalLayout_2.addWidget(self.modulesCheck)
        self.overrideCheck = QtWidgets.QCheckBox(self.groupBox_4)
        self.overrideCheck.setChecked(True)
        self.overrideCheck.setObjectName("overrideCheck")
        self.verticalLayout_2.addWidget(self.overrideCheck)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.caseInsensitiveRadio = QtWidgets.QRadioButton(self.groupBox_3)
        self.caseInsensitiveRadio.setObjectName("caseInsensitiveRadio")
        self.verticalLayout.addWidget(self.caseInsensitiveRadio)
        self.caseSensitiveRadio = QtWidgets.QRadioButton(self.groupBox_3)
        self.caseSensitiveRadio.setChecked(True)
        self.caseSensitiveRadio.setObjectName("caseSensitiveRadio")
        self.verticalLayout.addWidget(self.caseSensitiveRadio)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.filenamesOnlyCheck = QtWidgets.QCheckBox(self.groupBox_6)
        self.filenamesOnlyCheck.setChecked(False)
        self.filenamesOnlyCheck.setObjectName("filenamesOnlyCheck")
        self.gridLayout_3.addWidget(self.filenamesOnlyCheck, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.typeARECheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeARECheck.setChecked(True)
        self.typeARECheck.setObjectName("typeARECheck")
        self.verticalLayout_4.addWidget(self.typeARECheck)
        self.typeGITCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeGITCheck.setChecked(True)
        self.typeGITCheck.setObjectName("typeGITCheck")
        self.verticalLayout_4.addWidget(self.typeGITCheck)
        self.typeIFOCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeIFOCheck.setChecked(True)
        self.typeIFOCheck.setObjectName("typeIFOCheck")
        self.verticalLayout_4.addWidget(self.typeIFOCheck)
        self.typeDLGCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeDLGCheck.setChecked(True)
        self.typeDLGCheck.setObjectName("typeDLGCheck")
        self.verticalLayout_4.addWidget(self.typeDLGCheck)
        self.typeJRLCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeJRLCheck.setChecked(True)
        self.typeJRLCheck.setObjectName("typeJRLCheck")
        self.verticalLayout_4.addWidget(self.typeJRLCheck)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.typeUTCCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTCCheck.setChecked(True)
        self.typeUTCCheck.setObjectName("typeUTCCheck")
        self.verticalLayout_5.addWidget(self.typeUTCCheck)
        self.typeUTDCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTDCheck.setChecked(True)
        self.typeUTDCheck.setObjectName("typeUTDCheck")
        self.verticalLayout_5.addWidget(self.typeUTDCheck)
        self.typeUTECheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTECheck.setChecked(True)
        self.typeUTECheck.setObjectName("typeUTECheck")
        self.verticalLayout_5.addWidget(self.typeUTECheck)
        self.typeUTICheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTICheck.setChecked(True)
        self.typeUTICheck.setObjectName("typeUTICheck")
        self.verticalLayout_5.addWidget(self.typeUTICheck)
        self.typeUTPCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTPCheck.setChecked(True)
        self.typeUTPCheck.setObjectName("typeUTPCheck")
        self.verticalLayout_5.addWidget(self.typeUTPCheck)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.typeUTMCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTMCheck.setChecked(True)
        self.typeUTMCheck.setObjectName("typeUTMCheck")
        self.verticalLayout_6.addWidget(self.typeUTMCheck)
        self.typeUTWCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTWCheck.setChecked(True)
        self.typeUTWCheck.setObjectName("typeUTWCheck")
        self.verticalLayout_6.addWidget(self.typeUTWCheck)
        self.typeUTSCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTSCheck.setChecked(True)
        self.typeUTSCheck.setObjectName("typeUTSCheck")
        self.verticalLayout_6.addWidget(self.typeUTSCheck)
        self.typeUTTCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeUTTCheck.setChecked(True)
        self.typeUTTCheck.setObjectName("typeUTTCheck")
        self.verticalLayout_6.addWidget(self.typeUTTCheck)
        self.type2DACheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.type2DACheck.setChecked(True)
        self.type2DACheck.setObjectName("type2DACheck")
        self.verticalLayout_6.addWidget(self.type2DACheck)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.typeNSSCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeNSSCheck.setChecked(True)
        self.typeNSSCheck.setObjectName("typeNSSCheck")
        self.verticalLayout_7.addWidget(self.typeNSSCheck)
        self.typeNCSCheck = QtWidgets.QCheckBox(self.groupBox_5)
        self.typeNCSCheck.setChecked(True)
        self.typeNCSCheck.setObjectName("typeNCSCheck")
        self.verticalLayout_7.addWidget(self.typeNCSCheck)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_8.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "File Search"))
        self.groupBox.setTitle(_translate("Dialog", "Search within"))
        self.groupBox_2.setTitle(_translate("Dialog", "String to look for"))
        self.groupBox_4.setTitle(_translate("Dialog", "Search in"))
        self.coreCheck.setText(_translate("Dialog", "Core"))
        self.modulesCheck.setText(_translate("Dialog", "Modules"))
        self.overrideCheck.setText(_translate("Dialog", "Override"))
        self.groupBox_3.setTitle(_translate("Dialog", "Case"))
        self.caseInsensitiveRadio.setText(_translate("Dialog", "Sensitive"))
        self.caseSensitiveRadio.setText(_translate("Dialog", "Insensitive"))
        self.groupBox_6.setTitle(_translate("Dialog", "Options"))
        self.filenamesOnlyCheck.setText(_translate("Dialog", "Filenames only"))
        self.groupBox_5.setTitle(_translate("Dialog", "File types to search in"))
        self.typeARECheck.setText(_translate("Dialog", "ARE"))
        self.typeGITCheck.setText(_translate("Dialog", "GIT"))
        self.typeIFOCheck.setText(_translate("Dialog", "IFO"))
        self.typeDLGCheck.setText(_translate("Dialog", "DLG"))
        self.typeJRLCheck.setText(_translate("Dialog", "JRL"))
        self.typeUTCCheck.setText(_translate("Dialog", "UTC"))
        self.typeUTDCheck.setText(_translate("Dialog", "UTD"))
        self.typeUTECheck.setText(_translate("Dialog", "UTE"))
        self.typeUTICheck.setText(_translate("Dialog", "UTI"))
        self.typeUTPCheck.setText(_translate("Dialog", "UTP"))
        self.typeUTMCheck.setText(_translate("Dialog", "UTM"))
        self.typeUTWCheck.setText(_translate("Dialog", "UTW"))
        self.typeUTSCheck.setText(_translate("Dialog", "UTS"))
        self.typeUTTCheck.setText(_translate("Dialog", "UTT"))
        self.type2DACheck.setText(_translate("Dialog", "2DA"))
        self.typeNSSCheck.setText(_translate("Dialog", "NSS"))
        self.typeNCSCheck.setText(_translate("Dialog", "NCS"))