# Form implementation generated from reading ui file '..\ui\editors\utp.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 498)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewRenderer = ModelRenderer(parent=self.centralwidget)
        self.previewRenderer.setMinimumSize(QtCore.QSize(300, 0))
        self.previewRenderer.setMouseTracking(True)
        self.previewRenderer.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.previewRenderer.setObjectName("previewRenderer")
        self.horizontalLayout_2.addWidget(self.previewRenderer)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_15 = QtWidgets.QGroupBox(parent=self.tab_9)
        self.groupBox_15.setObjectName("groupBox_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_15)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.hasInventoryCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_15)
        self.hasInventoryCheckbox.setObjectName("hasInventoryCheckbox")
        self.verticalLayout_10.addWidget(self.hasInventoryCheckbox)
        self.inventoryButton = QtWidgets.QPushButton(parent=self.groupBox_15)
        self.inventoryButton.setObjectName("inventoryButton")
        self.verticalLayout_10.addWidget(self.inventoryButton)
        self.inventoryCountLabel = QtWidgets.QLabel(parent=self.groupBox_15)
        self.inventoryCountLabel.setEnabled(False)
        self.inventoryCountLabel.setObjectName("inventoryCountLabel")
        self.verticalLayout_10.addWidget(self.inventoryCountLabel)
        self.gridLayout_3.addWidget(self.groupBox_15, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 77, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab_9)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.nameEdit = LocalizedStringLineEdit(parent=self.groupBox)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_15.addWidget(self.nameEdit)
        self.formLayout_10.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_15)
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_14.setObjectName("label_14")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.label_38 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_38.setObjectName("label_38")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_38)
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setObjectName("label_15")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tagEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.tagEdit.setObjectName("tagEdit")
        self.horizontalLayout_16.addWidget(self.tagEdit)
        self.tagGenerateButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.tagGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.tagGenerateButton.setObjectName("tagGenerateButton")
        self.horizontalLayout_16.addWidget(self.tagGenerateButton)
        self.formLayout_10.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.resrefEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.horizontalLayout_17.addWidget(self.resrefEdit)
        self.resrefGenerateButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.resrefGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.resrefGenerateButton.setObjectName("resrefGenerateButton")
        self.horizontalLayout_17.addWidget(self.resrefGenerateButton)
        self.formLayout_10.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.appearanceSelect = ComboBox2DA(parent=self.groupBox)
        self.appearanceSelect.setObjectName("appearanceSelect")
        self.horizontalLayout_18.addWidget(self.appearanceSelect)
        spacerItem1 = QtWidgets.QSpacerItem(29, 17, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.formLayout_10.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_18)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.conversationEdit = FilterComboBox(parent=self.groupBox)
        self.conversationEdit.setObjectName("conversationEdit")
        self.horizontalLayout_5.addWidget(self.conversationEdit)
        self.conversationModifyButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.conversationModifyButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.conversationModifyButton.setObjectName("conversationModifyButton")
        self.horizontalLayout_5.addWidget(self.conversationModifyButton)
        self.formLayout_10.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.formLayout_10, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_16 = QtWidgets.QGroupBox(parent=self.tab_10)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.useableCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_16)
        self.useableCheckbox.setObjectName("useableCheckbox")
        self.gridLayout_5.addWidget(self.useableCheckbox, 2, 0, 1, 1)
        self.partyInteractCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_16)
        self.partyInteractCheckbox.setObjectName("partyInteractCheckbox")
        self.gridLayout_5.addWidget(self.partyInteractCheckbox, 1, 0, 1, 1)
        self.staticCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_16)
        self.staticCheckbox.setObjectName("staticCheckbox")
        self.gridLayout_5.addWidget(self.staticCheckbox, 1, 1, 1, 1)
        self.plotCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_16)
        self.plotCheckbox.setObjectName("plotCheckbox")
        self.gridLayout_5.addWidget(self.plotCheckbox, 0, 1, 1, 1)
        self.notBlastableCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_16)
        self.notBlastableCheckbox.setObjectName("notBlastableCheckbox")
        self.gridLayout_5.addWidget(self.notBlastableCheckbox, 2, 1, 1, 1)
        self.min1HpCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_16)
        self.min1HpCheckbox.setObjectName("min1HpCheckbox")
        self.gridLayout_5.addWidget(self.min1HpCheckbox, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_16)
        self.groupBox_17 = QtWidgets.QGroupBox(parent=self.tab_10)
        self.groupBox_17.setObjectName("groupBox_17")
        self.formLayout_11 = QtWidgets.QFormLayout(self.groupBox_17)
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_41 = QtWidgets.QLabel(parent=self.groupBox_17)
        self.label_41.setObjectName("label_41")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_41)
        self.factionSelect = ComboBox2DA(parent=self.groupBox_17)
        self.factionSelect.setObjectName("factionSelect")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.factionSelect)
        self.label_42 = QtWidgets.QLabel(parent=self.groupBox_17)
        self.label_42.setObjectName("label_42")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_42)
        self.animationState = QtWidgets.QSpinBox(parent=self.groupBox_17)
        self.animationState.setMinimum(-2147483648)
        self.animationState.setMaximum(2147483647)
        self.animationState.setObjectName("animationState")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.animationState)
        self.verticalLayout.addWidget(self.groupBox_17)
        self.frame_4 = QtWidgets.QFrame(parent=self.tab_10)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.currenHpSpin = QtWidgets.QSpinBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currenHpSpin.sizePolicy().hasHeightForWidth())
        self.currenHpSpin.setSizePolicy(sizePolicy)
        self.currenHpSpin.setMinimum(-2147483648)
        self.currenHpSpin.setMaximum(2147483647)
        self.currenHpSpin.setObjectName("currenHpSpin")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.currenHpSpin)
        self.label_26 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_26.setObjectName("label_26")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_26)
        self.maxHpSpin = QtWidgets.QSpinBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxHpSpin.sizePolicy().hasHeightForWidth())
        self.maxHpSpin.setSizePolicy(sizePolicy)
        self.maxHpSpin.setMinimum(-2147483648)
        self.maxHpSpin.setMaximum(2147483647)
        self.maxHpSpin.setObjectName("maxHpSpin")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.maxHpSpin)
        self.label_20 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_20)
        self.hardnessSpin = QtWidgets.QSpinBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hardnessSpin.sizePolicy().hasHeightForWidth())
        self.hardnessSpin.setSizePolicy(sizePolicy)
        self.hardnessSpin.setMinimum(-2147483648)
        self.hardnessSpin.setMaximum(2147483647)
        self.hardnessSpin.setObjectName("hardnessSpin")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.hardnessSpin)
        self.label_21 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.fortitudeSpin = QtWidgets.QSpinBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fortitudeSpin.sizePolicy().hasHeightForWidth())
        self.fortitudeSpin.setSizePolicy(sizePolicy)
        self.fortitudeSpin.setMinimum(-2147483648)
        self.fortitudeSpin.setMaximum(2147483647)
        self.fortitudeSpin.setObjectName("fortitudeSpin")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fortitudeSpin)
        self.label_24 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_24)
        self.reflexSpin = QtWidgets.QSpinBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reflexSpin.sizePolicy().hasHeightForWidth())
        self.reflexSpin.setSizePolicy(sizePolicy)
        self.reflexSpin.setMinimum(-2147483648)
        self.reflexSpin.setMaximum(2147483647)
        self.reflexSpin.setObjectName("reflexSpin")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.reflexSpin)
        self.label_25 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_25)
        self.willSpin = QtWidgets.QSpinBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.willSpin.sizePolicy().hasHeightForWidth())
        self.willSpin.setSizePolicy(sizePolicy)
        self.willSpin.setMinimum(-2147483648)
        self.willSpin.setMaximum(2147483647)
        self.willSpin.setObjectName("willSpin")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.willSpin)
        self.verticalLayout.addWidget(self.frame_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_10, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.needKeyCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.needKeyCheckbox.setObjectName("needKeyCheckbox")
        self.verticalLayout_4.addWidget(self.needKeyCheckbox)
        self.removeKeyCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.removeKeyCheckbox.setObjectName("removeKeyCheckbox")
        self.verticalLayout_4.addWidget(self.removeKeyCheckbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.keyEdit = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.keyEdit.setObjectName("keyEdit")
        self.horizontalLayout.addWidget(self.keyEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lockedCheckbox = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.lockedCheckbox.setObjectName("lockedCheckbox")
        self.verticalLayout_2.addWidget(self.lockedCheckbox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.difficultyLabel = QtWidgets.QLabel(parent=self.groupBox_2)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.difficultyLabel)
        self.difficultyModLabel = QtWidgets.QLabel(parent=self.groupBox_2)
        self.difficultyModLabel.setObjectName("difficultyModLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.difficultyModLabel)
        self.openLockSpin = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.openLockSpin.setMinimum(-2147483648)
        self.openLockSpin.setMaximum(2147483647)
        self.openLockSpin.setObjectName("openLockSpin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.openLockSpin)
        self.difficultySpin = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.difficultySpin.setMinimum(-2147483648)
        self.difficultySpin.setMaximum(2147483647)
        self.difficultySpin.setObjectName("difficultySpin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.difficultySpin)
        self.difficultyModSpin = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.difficultyModSpin.setMinimum(-2147483648)
        self.difficultyModSpin.setMaximum(2147483647)
        self.difficultyModSpin.setObjectName("difficultyModSpin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.difficultyModSpin)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 123, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.onClosedEdit = FilterComboBox(parent=self.tab_2)
        self.onClosedEdit.setObjectName("onClosedEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onClosedEdit)
        self.label_7 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.label_16 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_18)
        self.label_23 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_23)
        self.label_22 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_22)
        self.label_19 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_19)
        self.onDamagedEdit = FilterComboBox(parent=self.tab_2)
        self.onDamagedEdit.setObjectName("onDamagedEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onDamagedEdit)
        self.onDeathEdit = FilterComboBox(parent=self.tab_2)
        self.onDeathEdit.setObjectName("onDeathEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onDeathEdit)
        self.onEndConversationEdit = FilterComboBox(parent=self.tab_2)
        self.onEndConversationEdit.setObjectName("onEndConversationEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onEndConversationEdit)
        self.onOpenFailedEdit = FilterComboBox(parent=self.tab_2)
        self.onOpenFailedEdit.setObjectName("onOpenFailedEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onOpenFailedEdit)
        self.onHeartbeatEdit = FilterComboBox(parent=self.tab_2)
        self.onHeartbeatEdit.setObjectName("onHeartbeatEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onHeartbeatEdit)
        self.onInventoryEdit = FilterComboBox(parent=self.tab_2)
        self.onInventoryEdit.setObjectName("onInventoryEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onInventoryEdit)
        self.onMeleeAttackEdit = FilterComboBox(parent=self.tab_2)
        self.onMeleeAttackEdit.setObjectName("onMeleeAttackEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onMeleeAttackEdit)
        self.onSpellEdit = FilterComboBox(parent=self.tab_2)
        self.onSpellEdit.setObjectName("onSpellEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onSpellEdit)
        self.onOpenEdit = FilterComboBox(parent=self.tab_2)
        self.onOpenEdit.setObjectName("onOpenEdit")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onOpenEdit)
        self.onLockEdit = FilterComboBox(parent=self.tab_2)
        self.onLockEdit.setObjectName("onLockEdit")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onLockEdit)
        self.onUnlockEdit = FilterComboBox(parent=self.tab_2)
        self.onUnlockEdit.setObjectName("onUnlockEdit")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onUnlockEdit)
        self.onUsedEdit = FilterComboBox(parent=self.tab_2)
        self.onUsedEdit.setObjectName("onUsedEdit")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onUsedEdit)
        self.onUserDefinedEdit = FilterComboBox(parent=self.tab_2)
        self.onUserDefinedEdit.setObjectName("onUserDefinedEdit")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.onUserDefinedEdit)
        self.tabWidget.addTab(self.tab_2, "")
        self.commentsTab = QtWidgets.QWidget()
        self.commentsTab.setObjectName("commentsTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.commentsTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.commentsEdit = QtWidgets.QPlainTextEdit(parent=self.commentsTab)
        self.commentsEdit.setObjectName("commentsEdit")
        self.gridLayout_4.addWidget(self.commentsEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.commentsTab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 22))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(parent=self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRevert = QtGui.QAction(parent=MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionShowPreview = QtGui.QAction(parent=MainWindow)
        self.actionShowPreview.setCheckable(True)
        self.actionShowPreview.setObjectName("actionShowPreview")
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addAction(self.actionSave)
        self.menuNew.addAction(self.actionSave_As)
        self.menuNew.addAction(self.actionRevert)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionExit)
        self.menuView.addAction(self.actionShowPreview)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Inventory"))
        self.hasInventoryCheckbox.setText(_translate("MainWindow", "Has Inventory"))
        self.inventoryButton.setText(_translate("MainWindow", "Edit Inventory"))
        self.inventoryCountLabel.setText(_translate("MainWindow", "Total Items:"))
        self.groupBox.setTitle(_translate("MainWindow", "Profile"))
        self.label_6.setText(_translate("MainWindow", "Name:"))
        self.label_14.setText(_translate("MainWindow", "Tag:"))
        self.label_38.setText(_translate("MainWindow", "ResRef:"))
        self.label_15.setText(_translate("MainWindow", "Appearance:"))
        self.tagGenerateButton.setText(_translate("MainWindow", "-"))
        self.resrefGenerateButton.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "Conversation:"))
        self.conversationModifyButton.setText(_translate("MainWindow", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Basic"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Flags"))
        self.useableCheckbox.setText(_translate("MainWindow", "Useable"))
        self.partyInteractCheckbox.setText(_translate("MainWindow", "Party Interact"))
        self.staticCheckbox.setText(_translate("MainWindow", "Static"))
        self.plotCheckbox.setText(_translate("MainWindow", "Plot"))
        self.notBlastableCheckbox.setText(_translate("MainWindow", "Not Blastable"))
        self.min1HpCheckbox.setText(_translate("MainWindow", "Min1HP"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Other"))
        self.label_41.setText(_translate("MainWindow", "Faction:"))
        self.label_42.setText(_translate("MainWindow", "Animation State:"))
        self.label_3.setText(_translate("MainWindow", "Current HP:"))
        self.label_26.setText(_translate("MainWindow", "Max HP:"))
        self.label_20.setText(_translate("MainWindow", "Hardness:"))
        self.label_21.setText(_translate("MainWindow", "Fortitude:"))
        self.label_24.setText(_translate("MainWindow", "Reflex:"))
        self.label_25.setText(_translate("MainWindow", "Will:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Advanced"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Key"))
        self.needKeyCheckbox.setText(_translate("MainWindow", "Key required to unlock"))
        self.removeKeyCheckbox.setText(_translate("MainWindow", "Remove key on unlock"))
        self.label_4.setText(_translate("MainWindow", "Key Tag:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Lock"))
        self.lockedCheckbox.setText(_translate("MainWindow", "Locked"))
        self.label_2.setText(_translate("MainWindow", "Open Lock DC:"))
        self.difficultyLabel.setText(_translate("MainWindow", "Difficulty:"))
        self.difficultyModLabel.setText(_translate("MainWindow", "Difficulty Mod:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Lock"))
        self.label_5.setText(_translate("MainWindow", "OnClosed:"))
        self.label_7.setText(_translate("MainWindow", "OnDamaged:"))
        self.label_8.setText(_translate("MainWindow", "OnDeath:"))
        self.label_9.setText(_translate("MainWindow", "OnEndConversation:"))
        self.label_10.setText(_translate("MainWindow", "OnOpenFailed:"))
        self.label_11.setText(_translate("MainWindow", "OnHeartbeat:"))
        self.label_12.setText(_translate("MainWindow", "OnInventory:"))
        self.label_13.setText(_translate("MainWindow", "OnMeleeAttack:"))
        self.label_16.setText(_translate("MainWindow", "OnSpellCastAt:"))
        self.label_17.setText(_translate("MainWindow", "OnOpen:"))
        self.label_18.setText(_translate("MainWindow", "OnLock:"))
        self.label_23.setText(_translate("MainWindow", "OnUnlock:"))
        self.label_22.setText(_translate("MainWindow", "OnUsed:"))
        self.label_19.setText(_translate("MainWindow", "OnUserDefined:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Scripts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.commentsTab), _translate("MainWindow", "Comments"))
        self.menuNew.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionShowPreview.setText(_translate("MainWindow", "Show Preview"))
from toolset.gui.widgets.edit.combobox import FilterComboBox
from toolset.gui.widgets.edit.combobox_2da import ComboBox2DA
from toolset.gui.widgets.edit.locstring import LocalizedStringLineEdit
from toolset.gui.widgets.renderer.model import ModelRenderer

from toolset.rcc import resources_rc_pyqt6
