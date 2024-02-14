# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\ui\editors\utt.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 296)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.nameEdit = LocalizedStringLineEdit(self.tab)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_15.addWidget(self.nameEdit)
        self.formLayout_10.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tagEdit = QtWidgets.QLineEdit(self.tab)
        self.tagEdit.setObjectName("tagEdit")
        self.horizontalLayout_16.addWidget(self.tagEdit)
        self.tagGenerateButton = QtWidgets.QPushButton(self.tab)
        self.tagGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.tagGenerateButton.setObjectName("tagGenerateButton")
        self.horizontalLayout_16.addWidget(self.tagGenerateButton)
        self.formLayout_10.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_16)
        self.label_38 = QtWidgets.QLabel(self.tab)
        self.label_38.setObjectName("label_38")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.resrefEdit = QtWidgets.QLineEdit(self.tab)
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.horizontalLayout_17.addWidget(self.resrefEdit)
        self.resrefGenerateButton = QtWidgets.QPushButton(self.tab)
        self.resrefGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.resrefGenerateButton.setObjectName("resrefGenerateButton")
        self.horizontalLayout_17.addWidget(self.resrefGenerateButton)
        self.formLayout_10.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_17)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.typeSelect = QtWidgets.QComboBox(self.tab)
        self.typeSelect.setObjectName("typeSelect")
        self.typeSelect.addItem("")
        self.typeSelect.addItem("")
        self.typeSelect.addItem("")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.typeSelect)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cursorSelect = ComboBox2DA(self.tab)
        self.cursorSelect.setObjectName("cursorSelect")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cursorSelect)
        self.verticalLayout.addLayout(self.formLayout_10)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.autoRemoveKeyCheckbox = QtWidgets.QCheckBox(self.tab_5)
        self.autoRemoveKeyCheckbox.setObjectName("autoRemoveKeyCheckbox")
        self.verticalLayout_4.addWidget(self.autoRemoveKeyCheckbox)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.keyEdit = QtWidgets.QLineEdit(self.tab_5)
        self.keyEdit.setObjectName("keyEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.keyEdit)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.line = QtWidgets.QFrame(self.tab_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.factionSelect = ComboBox2DA(self.tab_5)
        self.factionSelect.setObjectName("factionSelect")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.factionSelect)
        self.highlightHeightSpin = QtWidgets.QDoubleSpinBox(self.tab_5)
        self.highlightHeightSpin.setObjectName("highlightHeightSpin")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.highlightHeightSpin)
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.isTrapCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.isTrapCheckbox.setObjectName("isTrapCheckbox")
        self.verticalLayout_2.addWidget(self.isTrapCheckbox)
        self.activateOnceCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.activateOnceCheckbox.setObjectName("activateOnceCheckbox")
        self.verticalLayout_2.addWidget(self.activateOnceCheckbox)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.trapSelect = ComboBox2DA(self.tab_2)
        self.trapSelect.setObjectName("trapSelect")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.trapSelect)
        self.verticalLayout_2.addLayout(self.formLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.detectableCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.detectableCheckbox.setObjectName("detectableCheckbox")
        self.verticalLayout_3.addWidget(self.detectableCheckbox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.detectDcSpin = QtWidgets.QSpinBox(self.tab_2)
        self.detectDcSpin.setObjectName("detectDcSpin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.detectDcSpin)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.disarmableCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.disarmableCheckbox.setObjectName("disarmableCheckbox")
        self.verticalLayout_3.addWidget(self.disarmableCheckbox)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.disarmDcSpin = QtWidgets.QSpinBox(self.tab_2)
        self.disarmDcSpin.setObjectName("disarmDcSpin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.disarmDcSpin)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.onHeartbeatEdit = QtWidgets.QLineEdit(self.tab_4)
        self.onHeartbeatEdit.setMaxLength(16)
        self.onHeartbeatEdit.setObjectName("onHeartbeatEdit")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.onHeartbeatEdit)
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.onExitEdit = QtWidgets.QLineEdit(self.tab_4)
        self.onExitEdit.setMaxLength(16)
        self.onExitEdit.setObjectName("onExitEdit")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.onExitEdit)
        self.onEnterEdit = QtWidgets.QLineEdit(self.tab_4)
        self.onEnterEdit.setMaxLength(16)
        self.onEnterEdit.setObjectName("onEnterEdit")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.onEnterEdit)
        self.onUserDefinedEdit = QtWidgets.QLineEdit(self.tab_4)
        self.onUserDefinedEdit.setMaxLength(16)
        self.onUserDefinedEdit.setObjectName("onUserDefinedEdit")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.onUserDefinedEdit)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.onTrapTriggeredEdit = QtWidgets.QLineEdit(self.tab_4)
        self.onTrapTriggeredEdit.setMaxLength(16)
        self.onTrapTriggeredEdit.setObjectName("onTrapTriggeredEdit")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.onTrapTriggeredEdit)
        self.onDisarmEdit = QtWidgets.QLineEdit(self.tab_4)
        self.onDisarmEdit.setMaxLength(16)
        self.onDisarmEdit.setObjectName("onDisarmEdit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.onDisarmEdit)
        self.onClickEdit = QtWidgets.QLineEdit(self.tab_4)
        self.onClickEdit.setMaxLength(16)
        self.onClickEdit.setObjectName("onClickEdit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.onClickEdit)
        self.verticalLayout_5.addLayout(self.formLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.commentsEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.commentsEdit.setObjectName("commentsEdit")
        self.gridLayout_2.addWidget(self.commentsEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionRevert = QtWidgets.QAction(MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionRevert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Name:"))
        self.label_14.setText(_translate("MainWindow", "Tag:"))
        self.tagGenerateButton.setText(_translate("MainWindow", "-"))
        self.label_38.setText(_translate("MainWindow", "ResRef:"))
        self.resrefGenerateButton.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "Type:"))
        self.typeSelect.setItemText(0, _translate("MainWindow", "Generic"))
        self.typeSelect.setItemText(1, _translate("MainWindow", "Transition"))
        self.typeSelect.setItemText(2, _translate("MainWindow", "Trap"))
        self.label_3.setText(_translate("MainWindow", "Cursor:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.autoRemoveKeyCheckbox.setText(_translate("MainWindow", "Auto Remove Key"))
        self.label_8.setText(_translate("MainWindow", "Key Name:"))
        self.label.setText(_translate("MainWindow", "Faction:"))
        self.label_7.setText(_translate("MainWindow", "Hightlight Height:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Advanced"))
        self.isTrapCheckbox.setText(_translate("MainWindow", "Is a trap"))
        self.activateOnceCheckbox.setText(_translate("MainWindow", "Activate Once"))
        self.label_17.setText(_translate("MainWindow", "Trap Type:"))
        self.detectableCheckbox.setText(_translate("MainWindow", "Detectable"))
        self.label_4.setText(_translate("MainWindow", "Detect DC:"))
        self.disarmableCheckbox.setText(_translate("MainWindow", "Disarmable"))
        self.label_5.setText(_translate("MainWindow", "Disarm DC:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Trap"))
        self.label_9.setText(_translate("MainWindow", "OnHeartbeat:"))
        self.label_10.setText(_translate("MainWindow", "OnExit:"))
        self.label_11.setText(_translate("MainWindow", "OnEnter:"))
        self.label_12.setText(_translate("MainWindow", "OnUserDefined:"))
        self.label_13.setText(_translate("MainWindow", "OnClick:"))
        self.label_15.setText(_translate("MainWindow", "OnDisarm:"))
        self.label_16.setText(_translate("MainWindow", "OnTrapTriggered:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Scripts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Comments"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from toolset.gui.widgets.edit.combobox_2da import ComboBox2DA
from toolset.gui.widgets.edit.locstring import LocalizedStringLineEdit
