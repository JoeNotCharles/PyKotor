# Form implementation generated from reading ui file '..\ui\editors\twoda.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 454)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filterBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.filterBox.setObjectName("filterBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.filterBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterEdit = QtWidgets.QLineEdit(parent=self.filterBox)
        self.filterEdit.setObjectName("filterEdit")
        self.verticalLayout.addWidget(self.filterEdit)
        self.verticalLayout_2.addWidget(self.filterBox)
        self.twodaTable = QtWidgets.QTableView(parent=self.centralwidget)
        self.twodaTable.setStyleSheet("")
        self.twodaTable.setAlternatingRowColors(True)
        self.twodaTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ContiguousSelection)
        self.twodaTable.setObjectName("twodaTable")
        self.verticalLayout_2.addWidget(self.twodaTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSetRowHeader = QtWidgets.QMenu(parent=self.menuView)
        self.menuSetRowHeader.setObjectName("menuSetRowHeader")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtGui.QAction(parent=MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionRevert = QtGui.QAction(parent=MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionToggleFilter = QtGui.QAction(parent=MainWindow)
        self.actionToggleFilter.setObjectName("actionToggleFilter")
        self.actionCopy = QtGui.QAction(parent=MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(parent=MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionInsertRow = QtGui.QAction(parent=MainWindow)
        self.actionInsertRow.setObjectName("actionInsertRow")
        self.actionRemoveRows = QtGui.QAction(parent=MainWindow)
        self.actionRemoveRows.setObjectName("actionRemoveRows")
        self.actionRedoRowLabels = QtGui.QAction(parent=MainWindow)
        self.actionRedoRowLabels.setObjectName("actionRedoRowLabels")
        self.actionDuplicateRow = QtGui.QAction(parent=MainWindow)
        self.actionDuplicateRow.setObjectName("actionDuplicateRow")
        self.actionplaceholder = QtGui.QAction(parent=MainWindow)
        self.actionplaceholder.setObjectName("actionplaceholder")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionRevert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuTools.addAction(self.actionToggleFilter)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionInsertRow)
        self.menuTools.addAction(self.actionDuplicateRow)
        self.menuTools.addAction(self.actionRemoveRows)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionRedoRowLabels)
        self.menuSetRowHeader.addAction(self.actionplaceholder)
        self.menuView.addAction(self.menuSetRowHeader.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filterBox.setTitle(_translate("MainWindow", "Filter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSetRowHeader.setTitle(_translate("MainWindow", "Set Row Header"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionToggleFilter.setText(_translate("MainWindow", "Toggle Filter"))
        self.actionToggleFilter.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionInsertRow.setText(_translate("MainWindow", "Insert Row"))
        self.actionInsertRow.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionRemoveRows.setText(_translate("MainWindow", "Remove Rows"))
        self.actionRemoveRows.setShortcut(_translate("MainWindow", "Ctrl+Del"))
        self.actionRedoRowLabels.setText(_translate("MainWindow", "Redo Row Labels"))
        self.actionRedoRowLabels.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionDuplicateRow.setText(_translate("MainWindow", "Duplicate Row"))
        self.actionDuplicateRow.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionplaceholder.setText(_translate("MainWindow", "placeholder"))
