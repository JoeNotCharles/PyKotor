# Form implementation generated from reading ui file '../ui/editors/uti.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 323)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.nameEdit = LocalizedStringLineEdit(parent=self.tab)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_18.addWidget(self.nameEdit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_18)
        self.label_14 = QtWidgets.QLabel(parent=self.tab)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.tagEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.tagEdit.setObjectName("tagEdit")
        self.horizontalLayout_19.addWidget(self.tagEdit)
        self.tagGenerateButton = QtWidgets.QPushButton(parent=self.tab)
        self.tagGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.tagGenerateButton.setObjectName("tagGenerateButton")
        self.horizontalLayout_19.addWidget(self.tagGenerateButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_19)
        self.label_38 = QtWidgets.QLabel(parent=self.tab)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_38)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.resrefEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.horizontalLayout_20.addWidget(self.resrefEdit)
        self.resrefGenerateButton = QtWidgets.QPushButton(parent=self.tab)
        self.resrefGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.resrefGenerateButton.setObjectName("resrefGenerateButton")
        self.horizontalLayout_20.addWidget(self.resrefGenerateButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_20)
        self.label_53 = QtWidgets.QLabel(parent=self.tab)
        self.label_53.setObjectName("label_53")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_53)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.descEdit = LocalizedStringLineEdit(parent=self.tab)
        self.descEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.descEdit.setObjectName("descEdit")
        self.horizontalLayout_21.addWidget(self.descEdit)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_21)
        self.label_39 = QtWidgets.QLabel(parent=self.tab)
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_39)
        self.baseSelect = ComboBox2DA(parent=self.tab)
        self.baseSelect.setObjectName("baseSelect")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.baseSelect)
        self.label_40 = QtWidgets.QLabel(parent=self.tab)
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_40)
        self.costSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.costSpin.setMaximum(1000000)
        self.costSpin.setObjectName("costSpin")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.costSpin)
        self.label_41 = QtWidgets.QLabel(parent=self.tab)
        self.label_41.setObjectName("label_41")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_41)
        self.additionalCostSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.additionalCostSpin.setMaximum(1000000)
        self.additionalCostSpin.setObjectName("additionalCostSpin")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.additionalCostSpin)
        self.label_42 = QtWidgets.QLabel(parent=self.tab)
        self.label_42.setObjectName("label_42")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_42)
        self.upgradeSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.upgradeSpin.setMaximum(255)
        self.upgradeSpin.setObjectName("upgradeSpin")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.upgradeSpin)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotCheckbox = QtWidgets.QCheckBox(parent=self.tab)
        self.plotCheckbox.setObjectName("plotCheckbox")
        self.verticalLayout.addWidget(self.plotCheckbox)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_43 = QtWidgets.QLabel(parent=self.tab)
        self.label_43.setObjectName("label_43")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_43)
        self.chargesSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.chargesSpin.setMaximum(255)
        self.chargesSpin.setObjectName("chargesSpin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.chargesSpin)
        self.label_44 = QtWidgets.QLabel(parent=self.tab)
        self.label_44.setObjectName("label_44")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_44)
        self.stackSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.stackSpin.setMaximum(65535)
        self.stackSpin.setObjectName("stackSpin")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.stackSpin)
        self.label_45 = QtWidgets.QLabel(parent=self.tab)
        self.label_45.setObjectName("label_45")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_45)
        self.modelVarSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.modelVarSpin.setMaximum(255)
        self.modelVarSpin.setObjectName("modelVarSpin")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.modelVarSpin)
        self.label_46 = QtWidgets.QLabel(parent=self.tab)
        self.label_46.setObjectName("label_46")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_46)
        self.bodyVarSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.bodyVarSpin.setMaximum(255)
        self.bodyVarSpin.setObjectName("bodyVarSpin")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bodyVarSpin)
        self.label_47 = QtWidgets.QLabel(parent=self.tab)
        self.label_47.setObjectName("label_47")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_47)
        self.textureVarSpin = QtWidgets.QSpinBox(parent=self.tab)
        self.textureVarSpin.setMaximum(255)
        self.textureVarSpin.setObjectName("textureVarSpin")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textureVarSpin)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(84, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.iconLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.iconLabel.setMinimumSize(QtCore.QSize(64, 64))
        self.iconLabel.setMaximumSize(QtCore.QSize(64, 64))
        self.iconLabel.setText("")
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout_3.addWidget(self.iconLabel, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.availablePropertyList = QtWidgets.QTreeWidget(parent=self.tab_2)
        self.availablePropertyList.setObjectName("availablePropertyList")
        self.availablePropertyList.headerItem().setText(0, "1")
        self.availablePropertyList.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.availablePropertyList)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.addPropertyButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.addPropertyButton.setMaximumSize(QtCore.QSize(20, 16777215))
        self.addPropertyButton.setObjectName("addPropertyButton")
        self.verticalLayout_2.addWidget(self.addPropertyButton)
        self.removePropertyButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.removePropertyButton.setMaximumSize(QtCore.QSize(20, 16777215))
        self.removePropertyButton.setObjectName("removePropertyButton")
        self.verticalLayout_2.addWidget(self.removePropertyButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.assignedPropertiesList = QtWidgets.QListWidget(parent=self.tab_2)
        self.assignedPropertiesList.setObjectName("assignedPropertiesList")
        self.verticalLayout_4.addWidget(self.assignedPropertiesList)
        self.editPropertyButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.editPropertyButton.setObjectName("editPropertyButton")
        self.verticalLayout_4.addWidget(self.editPropertyButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 22))
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
        self.label_53.setText(_translate("MainWindow", "Description:"))
        self.label_39.setText(_translate("MainWindow", "Base Item:"))
        self.label_40.setText(_translate("MainWindow", "Cost:"))
        self.label_41.setText(_translate("MainWindow", "Additional Cost:"))
        self.label_42.setText(_translate("MainWindow", "Upgrade Level:"))
        self.plotCheckbox.setText(_translate("MainWindow", "Plot"))
        self.label_43.setText(_translate("MainWindow", "Charges:"))
        self.label_44.setText(_translate("MainWindow", "Stack Size:"))
        self.label_45.setText(_translate("MainWindow", "Model Variation:"))
        self.label_46.setText(_translate("MainWindow", "Body Variation:"))
        self.label_47.setText(_translate("MainWindow", "Texture Variation:"))
        self.groupBox.setTitle(_translate("MainWindow", "Icon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General"))
        self.label.setText(_translate("MainWindow", "Available Properties"))
        self.addPropertyButton.setText(_translate("MainWindow", "->"))
        self.removePropertyButton.setText(_translate("MainWindow", "<-"))
        self.label_2.setText(_translate("MainWindow", "Assigned Properties"))
        self.editPropertyButton.setText(_translate("MainWindow", "Edit Property"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Properties"))
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

from toolset.rcc import resources_rc_pyqt6
