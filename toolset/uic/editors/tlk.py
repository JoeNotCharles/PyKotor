# Form implementation generated from reading ui file 'editors\tlk.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchBox = QtWidgets.QGroupBox(self.widget)
        self.searchBox.setObjectName("searchBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searchBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchEdit = QtWidgets.QLineEdit(self.searchBox)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_2.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(self.searchBox)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.horizontalLayout_3.addWidget(self.searchBox)
        self.jumpBox = QtWidgets.QGroupBox(self.widget)
        self.jumpBox.setObjectName("jumpBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.jumpBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.jumpSpinbox = QtWidgets.QSpinBox(self.jumpBox)
        self.jumpSpinbox.setObjectName("jumpSpinbox")
        self.horizontalLayout_4.addWidget(self.jumpSpinbox)
        self.jumpButton = QtWidgets.QPushButton(self.jumpBox)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_4.addWidget(self.jumpButton)
        self.horizontalLayout_3.addWidget(self.jumpBox)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.talkTable = QtWidgets.QTableView(self.widget)
        self.talkTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.talkTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.talkTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.talkTable.setObjectName("talkTable")
        self.talkTable.horizontalHeader().setVisible(False)
        self.talkTable.horizontalHeader().setHighlightSections(False)
        self.talkTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.talkTable)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QPlainTextEdit(self.widget1)
        self.textEdit.setEnabled(False)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.soundEdit = QtWidgets.QLineEdit(self.widget1)
        self.soundEdit.setEnabled(False)
        self.soundEdit.setMaxLength(16)
        self.soundEdit.setObjectName("soundEdit")
        self.horizontalLayout.addWidget(self.soundEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 21))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.actionGoTo = QtWidgets.QAction(MainWindow)
        self.actionGoTo.setObjectName("actionGoTo")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
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
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionInsert = QtWidgets.QAction(MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        self.menuView.addAction(self.actionGoTo)
        self.menuView.addAction(self.actionFind)
        self.menuView.addAction(self.actionInsert)
        self.menuFIle.addAction(self.actionNew)
        self.menuFIle.addAction(self.actionOpen)
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addAction(self.actionSaveAs)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionRevert)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionClose)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchBox.setTitle(_translate("MainWindow", "Search"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.jumpBox.setTitle(_translate("MainWindow", "Go To Line"))
        self.jumpButton.setText(_translate("MainWindow", "Jump"))
        self.label.setText(_translate("MainWindow", "Sound ResRef:"))
        self.menuView.setTitle(_translate("MainWindow", "Tools"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.actionGoTo.setText(_translate("MainWindow", "Go to"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionClose.setText(_translate("MainWindow", "Exit"))
        self.actionInsert.setText(_translate("MainWindow", "Insert"))
