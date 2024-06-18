# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\editors\ute.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setObjectName("label_39")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.difficultySelect = ComboBox2DA(self.tab)
        self.difficultySelect.setObjectName("difficultySelect")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.difficultySelect)
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setObjectName("label_40")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.minCreatureSpin = QtWidgets.QSpinBox(self.tab)
        self.minCreatureSpin.setMinimum(-2147483648)
        self.minCreatureSpin.setMaximum(2147483647)
        self.minCreatureSpin.setObjectName("minCreatureSpin")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.minCreatureSpin)
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setObjectName("label_41")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.maxCreatureSpin = QtWidgets.QSpinBox(self.tab)
        self.maxCreatureSpin.setMinimum(-2147483648)
        self.maxCreatureSpin.setMaximum(2147483647)
        self.maxCreatureSpin.setObjectName("maxCreatureSpin")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.maxCreatureSpin)
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setObjectName("label_42")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.spawnSelect = QtWidgets.QComboBox(self.tab)
        self.spawnSelect.setObjectName("spawnSelect")
        self.spawnSelect.addItem("")
        self.spawnSelect.addItem("")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spawnSelect)
        self.gridLayout_2.addLayout(self.formLayout_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.activeCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.activeCheckbox.setObjectName("activeCheckbox")
        self.verticalLayout.addWidget(self.activeCheckbox)
        self.playerOnlyCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.playerOnlyCheckbox.setObjectName("playerOnlyCheckbox")
        self.verticalLayout.addWidget(self.playerOnlyCheckbox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.factionSelect = ComboBox2DA(self.tab_2)
        self.factionSelect.setObjectName("factionSelect")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.factionSelect)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.respawnsCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.respawnsCheckbox.setObjectName("respawnsCheckbox")
        self.verticalLayout_2.addWidget(self.respawnsCheckbox)
        self.infiniteRespawnCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.infiniteRespawnCheckbox.setObjectName("infiniteRespawnCheckbox")
        self.verticalLayout_2.addWidget(self.infiniteRespawnCheckbox)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.respawnTimeSpin = QtWidgets.QSpinBox(self.tab_2)
        self.respawnTimeSpin.setMinimum(-2147483648)
        self.respawnTimeSpin.setMaximum(2147483647)
        self.respawnTimeSpin.setObjectName("respawnTimeSpin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.respawnTimeSpin)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.respawnCountSpin = QtWidgets.QSpinBox(self.tab_2)
        self.respawnCountSpin.setMinimum(0)
        self.respawnCountSpin.setMaximum(99999)
        self.respawnCountSpin.setObjectName("respawnCountSpin")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.respawnCountSpin)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.creatureTable = QtWidgets.QTableWidget(self.tab_5)
        self.creatureTable.setAlternatingRowColors(True)
        self.creatureTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.creatureTable.setObjectName("creatureTable")
        self.creatureTable.setColumnCount(4)
        self.creatureTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.creatureTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.creatureTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.creatureTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.creatureTable.setHorizontalHeaderItem(3, item)
        self.creatureTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.creatureTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.removeCreatureButton = QtWidgets.QPushButton(self.tab_5)
        self.removeCreatureButton.setObjectName("removeCreatureButton")
        self.horizontalLayout.addWidget(self.removeCreatureButton)
        self.addCreatureButton = QtWidgets.QPushButton(self.tab_5)
        self.addCreatureButton.setObjectName("addCreatureButton")
        self.horizontalLayout.addWidget(self.addCreatureButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.onEnterEdit = FilterComboBox(self.tab_3)
        self.onEnterEdit.setObjectName("onEnterEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.onEnterEdit)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.onExitEdit = FilterComboBox(self.tab_3)
        self.onExitEdit.setObjectName("onExitEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.onExitEdit)
        self.onExhaustedEdit = FilterComboBox(self.tab_3)
        self.onExhaustedEdit.setObjectName("onExhaustedEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.onExhaustedEdit)
        self.onHeartbeatEdit = FilterComboBox(self.tab_3)
        self.onHeartbeatEdit.setObjectName("onHeartbeatEdit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.onHeartbeatEdit)
        self.onUserDefinedEdit = FilterComboBox(self.tab_3)
        self.onUserDefinedEdit.setObjectName("onUserDefinedEdit")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.onUserDefinedEdit)
        self.gridLayout_4.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.commentsEdit = QtWidgets.QPlainTextEdit(self.tab_4)
        self.commentsEdit.setObjectName("commentsEdit")
        self.gridLayout_3.addWidget(self.commentsEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
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
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRevert = QtWidgets.QAction(MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
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
        self.label_39.setText(_translate("MainWindow", "Difficulty:"))
        self.label_40.setText(_translate("MainWindow", "Min Creatures:"))
        self.label_41.setText(_translate("MainWindow", "Max Creatures:"))
        self.label_42.setText(_translate("MainWindow", "Spawn Option:"))
        self.spawnSelect.setItemText(0, _translate("MainWindow", "Single Shot"))
        self.spawnSelect.setItemText(1, _translate("MainWindow", "Continuous"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.activeCheckbox.setText(_translate("MainWindow", "Active"))
        self.playerOnlyCheckbox.setText(_translate("MainWindow", "Player Triggered Only"))
        self.label.setText(_translate("MainWindow", "Faction:"))
        self.respawnsCheckbox.setText(_translate("MainWindow", "Respawns"))
        self.infiniteRespawnCheckbox.setText(_translate("MainWindow", "Infinite Respawns"))
        self.label_2.setText(_translate("MainWindow", "Respawn Time (s):"))
        self.label_3.setText(_translate("MainWindow", "Number of Respawns:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Advanced"))
        item = self.creatureTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SingleSpawn"))
        item = self.creatureTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CR"))
        item = self.creatureTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Appearance"))
        item = self.creatureTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ResRef"))
        self.removeCreatureButton.setText(_translate("MainWindow", "Remove"))
        self.addCreatureButton.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Creatures"))
        self.label_4.setText(_translate("MainWindow", "OnEnter:"))
        self.label_5.setText(_translate("MainWindow", "OnExit:"))
        self.label_7.setText(_translate("MainWindow", "OnExhausted:"))
        self.label_8.setText(_translate("MainWindow", "OnHeartbeat:"))
        self.label_9.setText(_translate("MainWindow", "OnUserDefined:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Scripts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Comments"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from toolset.gui.widgets.edit.combobox import FilterComboBox
from toolset.gui.widgets.edit.combobox_2da import ComboBox2DA
from toolset.gui.widgets.edit.locstring import LocalizedStringLineEdit

from toolset.rcc import resources_rc_pyqt5
