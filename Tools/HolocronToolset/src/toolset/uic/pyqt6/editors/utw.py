# Form implementation generated from reading ui file '../ui/editors/utw.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 250)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_6 = QtWidgets.QLabel(parent=self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.nameEdit = LocalizedStringLineEdit(parent=self.tab)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_15.addWidget(self.nameEdit)
        self.formLayout_10.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_15)
        self.label_14 = QtWidgets.QLabel(parent=self.tab)
        self.label_14.setObjectName("label_14")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tagEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.tagEdit.setObjectName("tagEdit")
        self.horizontalLayout_16.addWidget(self.tagEdit)
        self.tagGenerateButton = QtWidgets.QPushButton(parent=self.tab)
        self.tagGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.tagGenerateButton.setObjectName("tagGenerateButton")
        self.horizontalLayout_16.addWidget(self.tagGenerateButton)
        self.formLayout_10.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_16)
        self.label_38 = QtWidgets.QLabel(parent=self.tab)
        self.label_38.setObjectName("label_38")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_38)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.resrefEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.horizontalLayout_17.addWidget(self.resrefEdit)
        self.resrefGenerateButton = QtWidgets.QPushButton(parent=self.tab)
        self.resrefGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.resrefGenerateButton.setObjectName("resrefGenerateButton")
        self.horizontalLayout_17.addWidget(self.resrefGenerateButton)
        self.formLayout_10.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_17)
        self.verticalLayout.addLayout(self.formLayout_10)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.isNoteCheckbox = QtWidgets.QCheckBox(parent=self.tab_2)
        self.isNoteCheckbox.setObjectName("isNoteCheckbox")
        self.verticalLayout_2.addWidget(self.isNoteCheckbox)
        self.noteEnabledCheckbox = QtWidgets.QCheckBox(parent=self.tab_2)
        self.noteEnabledCheckbox.setObjectName("noteEnabledCheckbox")
        self.verticalLayout_2.addWidget(self.noteEnabledCheckbox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.noteEdit = QtWidgets.QLineEdit(parent=self.tab_2)
        self.noteEdit.setObjectName("noteEdit")
        self.horizontalLayout_18.addWidget(self.noteEdit)
        self.noteChangeButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.noteChangeButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.noteChangeButton.setObjectName("noteChangeButton")
        self.horizontalLayout_18.addWidget(self.noteChangeButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_18)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(320, 85, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.commentsEdit = QtWidgets.QPlainTextEdit(parent=self.tab_3)
        self.commentsEdit.setObjectName("commentsEdit")
        self.gridLayout_2.addWidget(self.commentsEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.isNoteCheckbox.setText(_translate("MainWindow", "Is a Map Note"))
        self.noteEnabledCheckbox.setText(_translate("MainWindow", "Map Note is Enabled"))
        self.label.setText(_translate("MainWindow", "Map Note:"))
        self.noteChangeButton.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Advanced"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Comments"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from toolset.gui.widgets.edit.locstring import LocalizedStringLineEdit

from toolset.rcc import resources_rc_pyqt6
