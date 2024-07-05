# Form implementation generated from reading ui file '..\ui\editors\ltr.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tabSingles = QtWidgets.QWidget()
        self.tabSingles.setObjectName("tabSingles")
        self.verticalLayoutSingles = QtWidgets.QVBoxLayout(self.tabSingles)
        self.verticalLayoutSingles.setObjectName("verticalLayoutSingles")
        self.horizontalLayoutSingleSelection = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSingleSelection.setObjectName("horizontalLayoutSingleSelection")
        self.labelSingleChar = QtWidgets.QLabel(parent=self.tabSingles)
        self.labelSingleChar.setObjectName("labelSingleChar")
        self.horizontalLayoutSingleSelection.addWidget(self.labelSingleChar)
        self.comboBoxSingleChar = QtWidgets.QComboBox(parent=self.tabSingles)
        self.comboBoxSingleChar.setObjectName("comboBoxSingleChar")
        self.horizontalLayoutSingleSelection.addWidget(self.comboBoxSingleChar)
        self.labelSingleStart = QtWidgets.QLabel(parent=self.tabSingles)
        self.labelSingleStart.setObjectName("labelSingleStart")
        self.horizontalLayoutSingleSelection.addWidget(self.labelSingleStart)
        self.spinBoxSingleStart = QtWidgets.QDoubleSpinBox(parent=self.tabSingles)
        self.spinBoxSingleStart.setMinimum(0.0)
        self.spinBoxSingleStart.setMaximum(1.0)
        self.spinBoxSingleStart.setSingleStep(0.01)
        self.spinBoxSingleStart.setObjectName("spinBoxSingleStart")
        self.horizontalLayoutSingleSelection.addWidget(self.spinBoxSingleStart)
        self.labelSingleMiddle = QtWidgets.QLabel(parent=self.tabSingles)
        self.labelSingleMiddle.setObjectName("labelSingleMiddle")
        self.horizontalLayoutSingleSelection.addWidget(self.labelSingleMiddle)
        self.spinBoxSingleMiddle = QtWidgets.QDoubleSpinBox(parent=self.tabSingles)
        self.spinBoxSingleMiddle.setMinimum(0.0)
        self.spinBoxSingleMiddle.setMaximum(1.0)
        self.spinBoxSingleMiddle.setSingleStep(0.01)
        self.spinBoxSingleMiddle.setObjectName("spinBoxSingleMiddle")
        self.horizontalLayoutSingleSelection.addWidget(self.spinBoxSingleMiddle)
        self.labelSingleEnd = QtWidgets.QLabel(parent=self.tabSingles)
        self.labelSingleEnd.setObjectName("labelSingleEnd")
        self.horizontalLayoutSingleSelection.addWidget(self.labelSingleEnd)
        self.spinBoxSingleEnd = QtWidgets.QDoubleSpinBox(parent=self.tabSingles)
        self.spinBoxSingleEnd.setMinimum(0.0)
        self.spinBoxSingleEnd.setMaximum(1.0)
        self.spinBoxSingleEnd.setSingleStep(0.01)
        self.spinBoxSingleEnd.setObjectName("spinBoxSingleEnd")
        self.horizontalLayoutSingleSelection.addWidget(self.spinBoxSingleEnd)
        self.verticalLayoutSingles.addLayout(self.horizontalLayoutSingleSelection)
        self.buttonSetSingle = QtWidgets.QPushButton(parent=self.tabSingles)
        self.buttonSetSingle.setObjectName("buttonSetSingle")
        self.verticalLayoutSingles.addWidget(self.buttonSetSingle)
        self.tableSingles = QtWidgets.QTableWidget(parent=self.tabSingles)
        self.tableSingles.setObjectName("tableSingles")
        self.tableSingles.setColumnCount(4)
        self.tableSingles.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSingles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSingles.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSingles.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSingles.setHorizontalHeaderItem(3, item)
        self.verticalLayoutSingles.addWidget(self.tableSingles)
        self.buttonAddSingle = QtWidgets.QPushButton(parent=self.tabSingles)
        self.buttonAddSingle.setObjectName("buttonAddSingle")
        self.verticalLayoutSingles.addWidget(self.buttonAddSingle)
        self.buttonRemoveSingle = QtWidgets.QPushButton(parent=self.tabSingles)
        self.buttonRemoveSingle.setObjectName("buttonRemoveSingle")
        self.verticalLayoutSingles.addWidget(self.buttonRemoveSingle)
        self.tabWidget.addTab(self.tabSingles, "")
        self.tabDoubles = QtWidgets.QWidget()
        self.tabDoubles.setObjectName("tabDoubles")
        self.verticalLayoutDoubles = QtWidgets.QVBoxLayout(self.tabDoubles)
        self.verticalLayoutDoubles.setObjectName("verticalLayoutDoubles")
        self.horizontalLayoutDoubleSelection = QtWidgets.QHBoxLayout()
        self.horizontalLayoutDoubleSelection.setObjectName("horizontalLayoutDoubleSelection")
        self.labelDoublePrevChar = QtWidgets.QLabel(parent=self.tabDoubles)
        self.labelDoublePrevChar.setObjectName("labelDoublePrevChar")
        self.horizontalLayoutDoubleSelection.addWidget(self.labelDoublePrevChar)
        self.comboBoxDoublePrevChar = QtWidgets.QComboBox(parent=self.tabDoubles)
        self.comboBoxDoublePrevChar.setObjectName("comboBoxDoublePrevChar")
        self.horizontalLayoutDoubleSelection.addWidget(self.comboBoxDoublePrevChar)
        self.labelDoubleChar = QtWidgets.QLabel(parent=self.tabDoubles)
        self.labelDoubleChar.setObjectName("labelDoubleChar")
        self.horizontalLayoutDoubleSelection.addWidget(self.labelDoubleChar)
        self.comboBoxDoubleChar = QtWidgets.QComboBox(parent=self.tabDoubles)
        self.comboBoxDoubleChar.setObjectName("comboBoxDoubleChar")
        self.horizontalLayoutDoubleSelection.addWidget(self.comboBoxDoubleChar)
        self.labelDoubleStart = QtWidgets.QLabel(parent=self.tabDoubles)
        self.labelDoubleStart.setObjectName("labelDoubleStart")
        self.horizontalLayoutDoubleSelection.addWidget(self.labelDoubleStart)
        self.spinBoxDoubleStart = QtWidgets.QDoubleSpinBox(parent=self.tabDoubles)
        self.spinBoxDoubleStart.setMinimum(0.0)
        self.spinBoxDoubleStart.setMaximum(1.0)
        self.spinBoxDoubleStart.setSingleStep(0.01)
        self.spinBoxDoubleStart.setObjectName("spinBoxDoubleStart")
        self.horizontalLayoutDoubleSelection.addWidget(self.spinBoxDoubleStart)
        self.labelDoubleMiddle = QtWidgets.QLabel(parent=self.tabDoubles)
        self.labelDoubleMiddle.setObjectName("labelDoubleMiddle")
        self.horizontalLayoutDoubleSelection.addWidget(self.labelDoubleMiddle)
        self.spinBoxDoubleMiddle = QtWidgets.QDoubleSpinBox(parent=self.tabDoubles)
        self.spinBoxDoubleMiddle.setMinimum(0.0)
        self.spinBoxDoubleMiddle.setMaximum(1.0)
        self.spinBoxDoubleMiddle.setSingleStep(0.01)
        self.spinBoxDoubleMiddle.setObjectName("spinBoxDoubleMiddle")
        self.horizontalLayoutDoubleSelection.addWidget(self.spinBoxDoubleMiddle)
        self.labelDoubleEnd = QtWidgets.QLabel(parent=self.tabDoubles)
        self.labelDoubleEnd.setObjectName("labelDoubleEnd")
        self.horizontalLayoutDoubleSelection.addWidget(self.labelDoubleEnd)
        self.spinBoxDoubleEnd = QtWidgets.QDoubleSpinBox(parent=self.tabDoubles)
        self.spinBoxDoubleEnd.setMinimum(0.0)
        self.spinBoxDoubleEnd.setMaximum(1.0)
        self.spinBoxDoubleEnd.setSingleStep(0.01)
        self.spinBoxDoubleEnd.setObjectName("spinBoxDoubleEnd")
        self.horizontalLayoutDoubleSelection.addWidget(self.spinBoxDoubleEnd)
        self.verticalLayoutDoubles.addLayout(self.horizontalLayoutDoubleSelection)
        self.buttonSetDouble = QtWidgets.QPushButton(parent=self.tabDoubles)
        self.buttonSetDouble.setObjectName("buttonSetDouble")
        self.verticalLayoutDoubles.addWidget(self.buttonSetDouble)
        self.tableDoubles = QtWidgets.QTableWidget(parent=self.tabDoubles)
        self.tableDoubles.setObjectName("tableDoubles")
        self.tableDoubles.setColumnCount(5)
        self.tableDoubles.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDoubles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDoubles.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDoubles.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDoubles.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDoubles.setHorizontalHeaderItem(4, item)
        self.verticalLayoutDoubles.addWidget(self.tableDoubles)
        self.buttonAddDouble = QtWidgets.QPushButton(parent=self.tabDoubles)
        self.buttonAddDouble.setObjectName("buttonAddDouble")
        self.verticalLayoutDoubles.addWidget(self.buttonAddDouble)
        self.buttonRemoveDouble = QtWidgets.QPushButton(parent=self.tabDoubles)
        self.buttonRemoveDouble.setObjectName("buttonRemoveDouble")
        self.verticalLayoutDoubles.addWidget(self.buttonRemoveDouble)
        self.tabWidget.addTab(self.tabDoubles, "")
        self.tabTriples = QtWidgets.QWidget()
        self.tabTriples.setObjectName("tabTriples")
        self.verticalLayoutTriples = QtWidgets.QVBoxLayout(self.tabTriples)
        self.verticalLayoutTriples.setObjectName("verticalLayoutTriples")
        self.horizontalLayoutTripleSelection = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTripleSelection.setObjectName("horizontalLayoutTripleSelection")
        self.labelTriplePrev2Char = QtWidgets.QLabel(parent=self.tabTriples)
        self.labelTriplePrev2Char.setObjectName("labelTriplePrev2Char")
        self.horizontalLayoutTripleSelection.addWidget(self.labelTriplePrev2Char)
        self.comboBoxTriplePrev2Char = QtWidgets.QComboBox(parent=self.tabTriples)
        self.comboBoxTriplePrev2Char.setObjectName("comboBoxTriplePrev2Char")
        self.horizontalLayoutTripleSelection.addWidget(self.comboBoxTriplePrev2Char)
        self.labelTriplePrev1Char = QtWidgets.QLabel(parent=self.tabTriples)
        self.labelTriplePrev1Char.setObjectName("labelTriplePrev1Char")
        self.horizontalLayoutTripleSelection.addWidget(self.labelTriplePrev1Char)
        self.comboBoxTriplePrev1Char = QtWidgets.QComboBox(parent=self.tabTriples)
        self.comboBoxTriplePrev1Char.setObjectName("comboBoxTriplePrev1Char")
        self.horizontalLayoutTripleSelection.addWidget(self.comboBoxTriplePrev1Char)
        self.labelTripleChar = QtWidgets.QLabel(parent=self.tabTriples)
        self.labelTripleChar.setObjectName("labelTripleChar")
        self.horizontalLayoutTripleSelection.addWidget(self.labelTripleChar)
        self.comboBoxTripleChar = QtWidgets.QComboBox(parent=self.tabTriples)
        self.comboBoxTripleChar.setObjectName("comboBoxTripleChar")
        self.horizontalLayoutTripleSelection.addWidget(self.comboBoxTripleChar)
        self.labelTripleStart = QtWidgets.QLabel(parent=self.tabTriples)
        self.labelTripleStart.setObjectName("labelTripleStart")
        self.horizontalLayoutTripleSelection.addWidget(self.labelTripleStart)
        self.spinBoxTripleStart = QtWidgets.QDoubleSpinBox(parent=self.tabTriples)
        self.spinBoxTripleStart.setMinimum(0.0)
        self.spinBoxTripleStart.setMaximum(1.0)
        self.spinBoxTripleStart.setSingleStep(0.01)
        self.spinBoxTripleStart.setObjectName("spinBoxTripleStart")
        self.horizontalLayoutTripleSelection.addWidget(self.spinBoxTripleStart)
        self.labelTripleMiddle = QtWidgets.QLabel(parent=self.tabTriples)
        self.labelTripleMiddle.setObjectName("labelTripleMiddle")
        self.horizontalLayoutTripleSelection.addWidget(self.labelTripleMiddle)
        self.spinBoxTripleMiddle = QtWidgets.QDoubleSpinBox(parent=self.tabTriples)
        self.spinBoxTripleMiddle.setMinimum(0.0)
        self.spinBoxTripleMiddle.setMaximum(1.0)
        self.spinBoxTripleMiddle.setSingleStep(0.01)
        self.spinBoxTripleMiddle.setObjectName("spinBoxTripleMiddle")
        self.horizontalLayoutTripleSelection.addWidget(self.spinBoxTripleMiddle)
        self.labelTripleEnd = QtWidgets.QLabel(parent=self.tabTriples)
        self.labelTripleEnd.setObjectName("labelTripleEnd")
        self.horizontalLayoutTripleSelection.addWidget(self.labelTripleEnd)
        self.spinBoxTripleEnd = QtWidgets.QDoubleSpinBox(parent=self.tabTriples)
        self.spinBoxTripleEnd.setMinimum(0.0)
        self.spinBoxTripleEnd.setMaximum(1.0)
        self.spinBoxTripleEnd.setSingleStep(0.01)
        self.spinBoxTripleEnd.setObjectName("spinBoxTripleEnd")
        self.horizontalLayoutTripleSelection.addWidget(self.spinBoxTripleEnd)
        self.verticalLayoutTriples.addLayout(self.horizontalLayoutTripleSelection)
        self.buttonSetTriple = QtWidgets.QPushButton(parent=self.tabTriples)
        self.buttonSetTriple.setObjectName("buttonSetTriple")
        self.verticalLayoutTriples.addWidget(self.buttonSetTriple)
        self.tableTriples = QtWidgets.QTableWidget(parent=self.tabTriples)
        self.tableTriples.setObjectName("tableTriples")
        self.tableTriples.setColumnCount(6)
        self.tableTriples.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTriples.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTriples.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTriples.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTriples.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTriples.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTriples.setHorizontalHeaderItem(5, item)
        self.verticalLayoutTriples.addWidget(self.tableTriples)
        self.buttonAddTriple = QtWidgets.QPushButton(parent=self.tabTriples)
        self.buttonAddTriple.setObjectName("buttonAddTriple")
        self.verticalLayoutTriples.addWidget(self.buttonAddTriple)
        self.buttonRemoveTriple = QtWidgets.QPushButton(parent=self.tabTriples)
        self.buttonRemoveTriple.setObjectName("buttonRemoveTriple")
        self.verticalLayoutTriples.addWidget(self.buttonRemoveTriple)
        self.tabWidget.addTab(self.tabTriples, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonGenerate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.verticalLayout.addWidget(self.buttonGenerate)
        self.lineEditGeneratedName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditGeneratedName.setObjectName("lineEditGeneratedName")
        self.verticalLayout.addWidget(self.lineEditGeneratedName)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFormat = QtWidgets.QMenu(parent=self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRevert = QtGui.QAction(parent=MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRevert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LTR Editor"))
        self.labelSingleChar.setText(_translate("MainWindow", "Character"))
        self.labelSingleStart.setText(_translate("MainWindow", "Start"))
        self.labelSingleMiddle.setText(_translate("MainWindow", "Middle"))
        self.labelSingleEnd.setText(_translate("MainWindow", "End"))
        self.buttonSetSingle.setText(_translate("MainWindow", "Set Single Character"))
        item = self.tableSingles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Character"))
        item = self.tableSingles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Start"))
        item = self.tableSingles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Middle"))
        item = self.tableSingles.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "End"))
        self.buttonAddSingle.setText(_translate("MainWindow", "Add Row"))
        self.buttonRemoveSingle.setText(_translate("MainWindow", "Remove Selected Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSingles), _translate("MainWindow", "Singles"))
        self.labelDoublePrevChar.setText(_translate("MainWindow", "Previous Character"))
        self.labelDoubleChar.setText(_translate("MainWindow", "Character"))
        self.labelDoubleStart.setText(_translate("MainWindow", "Start"))
        self.labelDoubleMiddle.setText(_translate("MainWindow", "Middle"))
        self.labelDoubleEnd.setText(_translate("MainWindow", "End"))
        self.buttonSetDouble.setText(_translate("MainWindow", "Set Double Character"))
        item = self.tableDoubles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Previous Character"))
        item = self.tableDoubles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Character"))
        item = self.tableDoubles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Start"))
        item = self.tableDoubles.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Middle"))
        item = self.tableDoubles.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "End"))
        self.buttonAddDouble.setText(_translate("MainWindow", "Add Row"))
        self.buttonRemoveDouble.setText(_translate("MainWindow", "Remove Selected Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDoubles), _translate("MainWindow", "Doubles"))
        self.labelTriplePrev2Char.setText(_translate("MainWindow", "Previous Character 2"))
        self.labelTriplePrev1Char.setText(_translate("MainWindow", "Previous Character 1"))
        self.labelTripleChar.setText(_translate("MainWindow", "Character"))
        self.labelTripleStart.setText(_translate("MainWindow", "Start"))
        self.labelTripleMiddle.setText(_translate("MainWindow", "Middle"))
        self.labelTripleEnd.setText(_translate("MainWindow", "End"))
        self.buttonSetTriple.setText(_translate("MainWindow", "Set Triple Character"))
        item = self.tableTriples.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Previous Character 2"))
        item = self.tableTriples.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Previous Character 1"))
        item = self.tableTriples.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Character"))
        item = self.tableTriples.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Start"))
        item = self.tableTriples.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Middle"))
        item = self.tableTriples.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "End"))
        self.buttonAddTriple.setText(_translate("MainWindow", "Add Row"))
        self.buttonRemoveTriple.setText(_translate("MainWindow", "Remove Selected Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTriples), _translate("MainWindow", "Triples"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generate Name"))
        self.lineEditGeneratedName.setPlaceholderText(_translate("MainWindow", "Generated Name"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFormat.setTitle(_translate("MainWindow", "View"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

from toolset.rcc import resources_rc_pyqt6
