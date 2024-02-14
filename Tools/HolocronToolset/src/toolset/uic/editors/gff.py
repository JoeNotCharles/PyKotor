# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\ui\editors\gff.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 486)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeView = QtWidgets.QTreeView(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.treeView.setFont(font)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(False)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fieldBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.fieldBox.setEnabled(False)
        self.fieldBox.setTitle("")
        self.fieldBox.setObjectName("fieldBox")
        self.formLayout = QtWidgets.QFormLayout(self.fieldBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.fieldBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.labelEdit = QtWidgets.QLineEdit(self.fieldBox)
        self.labelEdit.setMaxLength(16)
        self.labelEdit.setObjectName("labelEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelEdit)
        self.label_2 = QtWidgets.QLabel(self.fieldBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.typeCombo = QtWidgets.QComboBox(self.fieldBox)
        self.typeCombo.setObjectName("typeCombo")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.typeCombo.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.typeCombo)
        self.verticalLayout.addWidget(self.fieldBox)
        self.pages = QtWidgets.QStackedWidget(self.layoutWidget)
        self.pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pages.setObjectName("pages")
        self.linePage = QtWidgets.QWidget()
        self.linePage.setObjectName("linePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.linePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.linePage)
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pages.addWidget(self.linePage)
        self.intPage = QtWidgets.QWidget()
        self.intPage.setObjectName("intPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.intPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.intSpin = LongSpinBox(self.intPage)
        self.intSpin.setObjectName("intSpin")
        self.verticalLayout_5.addWidget(self.intSpin)
        spacerItem1 = QtWidgets.QSpacerItem(20, 280, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.pages.addWidget(self.intPage)
        self.blankPage = QtWidgets.QWidget()
        self.blankPage.setObjectName("blankPage")
        self.pages.addWidget(self.blankPage)
        self.floatPage = QtWidgets.QWidget()
        self.floatPage.setObjectName("floatPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.floatPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.floatSpin = QtWidgets.QDoubleSpinBox(self.floatPage)
        self.floatSpin.setDecimals(6)
        self.floatSpin.setMinimum(-1e+22)
        self.floatSpin.setMaximum(1e+23)
        self.floatSpin.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.floatSpin.setObjectName("floatSpin")
        self.verticalLayout_4.addWidget(self.floatSpin)
        spacerItem2 = QtWidgets.QSpacerItem(20, 280, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.pages.addWidget(self.floatPage)
        self.vector3Page = QtWidgets.QWidget()
        self.vector3Page.setObjectName("vector3Page")
        self.formLayout_3 = QtWidgets.QFormLayout(self.vector3Page)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.vector3Page)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.xVec3Spin = QtWidgets.QDoubleSpinBox(self.vector3Page)
        self.xVec3Spin.setDecimals(6)
        self.xVec3Spin.setMinimum(-1e+29)
        self.xVec3Spin.setMaximum(1e+26)
        self.xVec3Spin.setObjectName("xVec3Spin")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xVec3Spin)
        self.label_4 = QtWidgets.QLabel(self.vector3Page)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.yVec3Spin = QtWidgets.QDoubleSpinBox(self.vector3Page)
        self.yVec3Spin.setDecimals(6)
        self.yVec3Spin.setMinimum(-1e+29)
        self.yVec3Spin.setMaximum(1e+26)
        self.yVec3Spin.setObjectName("yVec3Spin")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.yVec3Spin)
        self.label_5 = QtWidgets.QLabel(self.vector3Page)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.zVec3Spin = QtWidgets.QDoubleSpinBox(self.vector3Page)
        self.zVec3Spin.setDecimals(6)
        self.zVec3Spin.setMinimum(-1e+29)
        self.zVec3Spin.setMaximum(1e+26)
        self.zVec3Spin.setObjectName("zVec3Spin")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zVec3Spin)
        self.pages.addWidget(self.vector3Page)
        self.vector4Page = QtWidgets.QWidget()
        self.vector4Page.setObjectName("vector4Page")
        self.formLayout_2 = QtWidgets.QFormLayout(self.vector4Page)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.vector4Page)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.xVec4Spin = QtWidgets.QDoubleSpinBox(self.vector4Page)
        self.xVec4Spin.setDecimals(8)
        self.xVec4Spin.setMinimum(-1e+28)
        self.xVec4Spin.setMaximum(1e+29)
        self.xVec4Spin.setObjectName("xVec4Spin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xVec4Spin)
        self.label_8 = QtWidgets.QLabel(self.vector4Page)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.yVec4Spin = QtWidgets.QDoubleSpinBox(self.vector4Page)
        self.yVec4Spin.setDecimals(8)
        self.yVec4Spin.setMinimum(-1e+28)
        self.yVec4Spin.setMaximum(1e+29)
        self.yVec4Spin.setObjectName("yVec4Spin")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.yVec4Spin)
        self.label_9 = QtWidgets.QLabel(self.vector4Page)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_7 = QtWidgets.QLabel(self.vector4Page)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.zVec4Spin = QtWidgets.QDoubleSpinBox(self.vector4Page)
        self.zVec4Spin.setDecimals(8)
        self.zVec4Spin.setMinimum(-1e+28)
        self.zVec4Spin.setMaximum(1e+29)
        self.zVec4Spin.setObjectName("zVec4Spin")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zVec4Spin)
        self.wVec4Spin = QtWidgets.QDoubleSpinBox(self.vector4Page)
        self.wVec4Spin.setDecimals(8)
        self.wVec4Spin.setMinimum(-1e+28)
        self.wVec4Spin.setMaximum(1e+29)
        self.wVec4Spin.setObjectName("wVec4Spin")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wVec4Spin)
        self.pages.addWidget(self.vector4Page)
        self.textPage = QtWidgets.QWidget()
        self.textPage.setObjectName("textPage")
        self.gridLayout = QtWidgets.QGridLayout(self.textPage)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QPlainTextEdit(self.textPage)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.pages.addWidget(self.textPage)
        self.substringPage = QtWidgets.QWidget()
        self.substringPage.setObjectName("substringPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.substringPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.substringPage)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.stringrefSpin = QtWidgets.QSpinBox(self.substringPage)
        self.stringrefSpin.setMinimum(-1)
        self.stringrefSpin.setMaximum(999999999)
        self.stringrefSpin.setObjectName("stringrefSpin")
        self.horizontalLayout_3.addWidget(self.stringrefSpin)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tlkTextEdit = QtWidgets.QPlainTextEdit(self.substringPage)
        self.tlkTextEdit.setEnabled(False)
        self.tlkTextEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.tlkTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tlkTextEdit.setReadOnly(True)
        self.tlkTextEdit.setObjectName("tlkTextEdit")
        self.verticalLayout_3.addWidget(self.tlkTextEdit)
        self.line = QtWidgets.QFrame(self.substringPage)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.substringLangCombo = QtWidgets.QComboBox(self.substringPage)
        self.substringLangCombo.setObjectName("substringLangCombo")
        self.substringLangCombo.addItem("")
        self.substringLangCombo.addItem("")
        self.substringLangCombo.addItem("")
        self.substringLangCombo.addItem("")
        self.substringLangCombo.addItem("")
        self.substringLangCombo.addItem("")
        self.horizontalLayout_2.addWidget(self.substringLangCombo)
        self.substringGenderCombo = QtWidgets.QComboBox(self.substringPage)
        self.substringGenderCombo.setObjectName("substringGenderCombo")
        self.substringGenderCombo.addItem("")
        self.substringGenderCombo.addItem("")
        self.horizontalLayout_2.addWidget(self.substringGenderCombo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addSubstringButton = QtWidgets.QPushButton(self.substringPage)
        self.addSubstringButton.setObjectName("addSubstringButton")
        self.horizontalLayout_4.addWidget(self.addSubstringButton)
        self.removeSubstringButton = QtWidgets.QPushButton(self.substringPage)
        self.removeSubstringButton.setObjectName("removeSubstringButton")
        self.horizontalLayout_4.addWidget(self.removeSubstringButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.substringPage)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.substringList = QtWidgets.QListWidget(self.substringPage)
        self.substringList.setMaximumSize(QtCore.QSize(16777215, 100))
        self.substringList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.substringList.setObjectName("substringList")
        self.verticalLayout_3.addWidget(self.substringList)
        self.substringEdit = QtWidgets.QPlainTextEdit(self.substringPage)
        self.substringEdit.setObjectName("substringEdit")
        self.verticalLayout_3.addWidget(self.substringEdit)
        self.pages.addWidget(self.substringPage)
        self.verticalLayout.addWidget(self.pages)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRevert = QtWidgets.QAction(MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSetTLK = QtWidgets.QAction(MainWindow)
        self.actionSetTLK.setObjectName("actionSetTLK")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRevert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionSetTLK)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Label:"))
        self.label_2.setText(_translate("MainWindow", "Type:"))
        self.typeCombo.setItemText(0, _translate("MainWindow", "UInt8"))
        self.typeCombo.setItemText(1, _translate("MainWindow", "Int8"))
        self.typeCombo.setItemText(2, _translate("MainWindow", "UInt16"))
        self.typeCombo.setItemText(3, _translate("MainWindow", "Int16"))
        self.typeCombo.setItemText(4, _translate("MainWindow", "UInt32"))
        self.typeCombo.setItemText(5, _translate("MainWindow", "Int32"))
        self.typeCombo.setItemText(6, _translate("MainWindow", "UInt64"))
        self.typeCombo.setItemText(7, _translate("MainWindow", "Int64"))
        self.typeCombo.setItemText(8, _translate("MainWindow", "Single"))
        self.typeCombo.setItemText(9, _translate("MainWindow", "Double"))
        self.typeCombo.setItemText(10, _translate("MainWindow", "String"))
        self.typeCombo.setItemText(11, _translate("MainWindow", "ResRef"))
        self.typeCombo.setItemText(12, _translate("MainWindow", "LocalizedString"))
        self.typeCombo.setItemText(13, _translate("MainWindow", "Binary"))
        self.typeCombo.setItemText(14, _translate("MainWindow", "Struct"))
        self.typeCombo.setItemText(15, _translate("MainWindow", "List"))
        self.typeCombo.setItemText(16, _translate("MainWindow", "Vector4"))
        self.typeCombo.setItemText(17, _translate("MainWindow", "Vector3"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", "Z"))
        self.label_10.setText(_translate("MainWindow", "X"))
        self.label_8.setText(_translate("MainWindow", "Y"))
        self.label_9.setText(_translate("MainWindow", "Z"))
        self.label_7.setText(_translate("MainWindow", "W"))
        self.label_6.setText(_translate("MainWindow", "StringRef:"))
        self.substringLangCombo.setItemText(0, _translate("MainWindow", "English"))
        self.substringLangCombo.setItemText(1, _translate("MainWindow", "French"))
        self.substringLangCombo.setItemText(2, _translate("MainWindow", "German"))
        self.substringLangCombo.setItemText(3, _translate("MainWindow", "Italian"))
        self.substringLangCombo.setItemText(4, _translate("MainWindow", "Spanish"))
        self.substringLangCombo.setItemText(5, _translate("MainWindow", "Polish"))
        self.substringGenderCombo.setItemText(0, _translate("MainWindow", "Male"))
        self.substringGenderCombo.setItemText(1, _translate("MainWindow", "Female"))
        self.addSubstringButton.setText(_translate("MainWindow", "Add"))
        self.removeSubstringButton.setText(_translate("MainWindow", "Remove"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSetTLK.setText(_translate("MainWindow", "Set TLK"))
from toolset.gui.widgets.long_spinbox import LongSpinBox
