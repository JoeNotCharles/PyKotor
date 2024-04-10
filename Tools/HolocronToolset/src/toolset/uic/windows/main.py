# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\ui\windows\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 471)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gameCombo = QtWidgets.QComboBox(self.centralwidget)
        self.gameCombo.setObjectName("gameCombo")
        self.verticalLayout_4.addWidget(self.gameCombo)
        self.resourceTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.resourceTabs.setObjectName("resourceTabs")
        self.coreTab = QtWidgets.QWidget()
        self.coreTab.setObjectName("coreTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.coreTab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.coreWidget = ResourceList(self.coreTab)
        self.coreWidget.setObjectName("coreWidget")
        self.verticalLayout_2.addWidget(self.coreWidget)
        self.resourceTabs.addTab(self.coreTab, "")
        self.modulesTab = QtWidgets.QWidget()
        self.modulesTab.setObjectName("modulesTab")
        self.verticalLayoutModulesTab = QtWidgets.QVBoxLayout(self.modulesTab)
        self.verticalLayoutModulesTab.setObjectName("verticalLayoutModulesTab")
        self.specialActionButton = QtWidgets.QPushButton(self.modulesTab)
        self.specialActionButton.setObjectName("specialActionButton")
        self.verticalLayoutModulesTab.addWidget(self.specialActionButton)
        self.gridLayoutModules = QtWidgets.QGridLayout()
        self.gridLayoutModules.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutModules.setSpacing(0)
        self.gridLayoutModules.setObjectName("gridLayoutModules")
        self.modulesWidget = ResourceList(self.modulesTab)
        self.modulesWidget.setObjectName("modulesWidget")
        self.gridLayoutModules.addWidget(self.modulesWidget, 0, 0, 1, 2)
        self.verticalLayoutModulesTab.addLayout(self.gridLayoutModules)
        self.resourceTabs.addTab(self.modulesTab, "")
        self.overrideTab = QtWidgets.QWidget()
        self.overrideTab.setObjectName("overrideTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.overrideTab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.overrideWidget = ResourceList(self.overrideTab)
        self.overrideWidget.setObjectName("overrideWidget")
        self.verticalLayout_3.addWidget(self.overrideWidget)
        self.resourceTabs.addTab(self.overrideTab, "")
        self.texturesTab = QtWidgets.QWidget()
        self.texturesTab.setObjectName("texturesTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.texturesTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.texturesWidget = TextureList(self.texturesTab)
        self.texturesWidget.setObjectName("texturesWidget")
        self.verticalLayout_6.addWidget(self.texturesWidget)
        self.resourceTabs.addTab(self.texturesTab, "")
        self.verticalLayout_4.addWidget(self.resourceTabs)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.vboxlayout.setObjectName("vboxlayout")
        spacerItem = QtWidgets.QSpacerItem(124, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vboxlayout.addItem(spacerItem)
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.openButton = QtWidgets.QPushButton(self.sidebar)
        self.openButton.setObjectName("openButton")
        self.verticalLayout_5.addWidget(self.openButton)
        self.extractButton = QtWidgets.QPushButton(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extractButton.sizePolicy().hasHeightForWidth())
        self.extractButton.setSizePolicy(sizePolicy)
        self.extractButton.setObjectName("extractButton")
        self.verticalLayout_5.addWidget(self.extractButton)
        self.tpcGroup_2 = QtWidgets.QGroupBox(self.sidebar)
        self.tpcGroup_2.setObjectName("tpcGroup_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tpcGroup_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tpcDecompileCheckbox = QtWidgets.QCheckBox(self.tpcGroup_2)
        self.tpcDecompileCheckbox.setObjectName("tpcDecompileCheckbox")
        self.verticalLayout_10.addWidget(self.tpcDecompileCheckbox)
        self.tpcTxiCheckbox = QtWidgets.QCheckBox(self.tpcGroup_2)
        self.tpcTxiCheckbox.setObjectName("tpcTxiCheckbox")
        self.verticalLayout_10.addWidget(self.tpcTxiCheckbox)
        self.verticalLayout_5.addWidget(self.tpcGroup_2)
        self.mdlGroup_2 = QtWidgets.QGroupBox(self.sidebar)
        self.mdlGroup_2.setObjectName("mdlGroup_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mdlGroup_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mdlDecompileCheckbox = QtWidgets.QCheckBox(self.mdlGroup_2)
        self.mdlDecompileCheckbox.setObjectName("mdlDecompileCheckbox")
        self.verticalLayout_9.addWidget(self.mdlDecompileCheckbox)
        self.mdlTexturesCheckbox = QtWidgets.QCheckBox(self.mdlGroup_2)
        self.mdlTexturesCheckbox.setObjectName("mdlTexturesCheckbox")
        self.verticalLayout_9.addWidget(self.mdlTexturesCheckbox)
        self.verticalLayout_5.addWidget(self.mdlGroup_2)
        self.vboxlayout.addWidget(self.sidebar)
        spacerItem1 = QtWidgets.QSpacerItem(124, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.vboxlayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuDiscord = QtWidgets.QMenu(self.menuHelp)
        self.menuDiscord.setObjectName("menuDiscord")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.cloneModuleAction = QtWidgets.QAction(MainWindow)
        self.cloneModuleAction.setObjectName("cloneModuleAction")
        self.actionRecent_Files = QtWidgets.QAction(MainWindow)
        self.actionRecent_Files.setObjectName("actionRecent_Files")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.actionCreature = QtWidgets.QAction(MainWindow)
        self.actionCreature.setObjectName("actionCreature")
        self.actionItem = QtWidgets.QAction(MainWindow)
        self.actionItem.setObjectName("actionItem")
        self.actionDoor = QtWidgets.QAction(MainWindow)
        self.actionDoor.setObjectName("actionDoor")
        self.actionPlaceable = QtWidgets.QAction(MainWindow)
        self.actionPlaceable.setObjectName("actionPlaceable")
        self.actionMerchant = QtWidgets.QAction(MainWindow)
        self.actionMerchant.setObjectName("actionMerchant")
        self.actionEncounter = QtWidgets.QAction(MainWindow)
        self.actionEncounter.setObjectName("actionEncounter")
        self.actionTrigger = QtWidgets.QAction(MainWindow)
        self.actionTrigger.setObjectName("actionTrigger")
        self.actionWaypoint = QtWidgets.QAction(MainWindow)
        self.actionWaypoint.setObjectName("actionWaypoint")
        self.actionDialog = QtWidgets.QAction(MainWindow)
        self.actionDialog.setEnabled(False)
        self.actionDialog.setObjectName("actionDialog")
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.actionNewGFF = QtWidgets.QAction(MainWindow)
        self.actionNewGFF.setObjectName("actionNewGFF")
        self.actionNewERF = QtWidgets.QAction(MainWindow)
        self.actionNewERF.setObjectName("actionNewERF")
        self.actionNewTXT = QtWidgets.QAction(MainWindow)
        self.actionNewTXT.setObjectName("actionNewTXT")
        self.actionEditTLK = QtWidgets.QAction(MainWindow)
        self.actionEditTLK.setEnabled(False)
        self.actionEditTLK.setObjectName("actionEditTLK")
        self.actionHelpUpdates = QtWidgets.QAction(MainWindow)
        self.actionHelpUpdates.setObjectName("actionHelpUpdates")
        self.actionHelpAbout = QtWidgets.QAction(MainWindow)
        self.actionHelpAbout.setObjectName("actionHelpAbout")
        self.actionNewSSF = QtWidgets.QAction(MainWindow)
        self.actionNewSSF.setObjectName("actionNewSSF")
        self.actionNewUTC = QtWidgets.QAction(MainWindow)
        self.actionNewUTC.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/kx/creature.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNewUTC.setIcon(icon)
        self.actionNewUTC.setObjectName("actionNewUTC")
        self.actionCloneModule = QtWidgets.QAction(MainWindow)
        self.actionCloneModule.setEnabled(False)
        self.actionCloneModule.setObjectName("actionCloneModule")
        self.actionNewUTP = QtWidgets.QAction(MainWindow)
        self.actionNewUTP.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/kx/placeable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTP.setIcon(icon1)
        self.actionNewUTP.setObjectName("actionNewUTP")
        self.actionNewUTD = QtWidgets.QAction(MainWindow)
        self.actionNewUTD.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/kx/door.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTD.setIcon(icon2)
        self.actionNewUTD.setObjectName("actionNewUTD")
        self.actionNewUTW = QtWidgets.QAction(MainWindow)
        self.actionNewUTW.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/kx/waypoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTW.setIcon(icon3)
        self.actionNewUTW.setObjectName("actionNewUTW")
        self.actionNewUTT = QtWidgets.QAction(MainWindow)
        self.actionNewUTT.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/kx/trigger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTT.setIcon(icon4)
        self.actionNewUTT.setObjectName("actionNewUTT")
        self.actionNewUTE = QtWidgets.QAction(MainWindow)
        self.actionNewUTE.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons/kx/encounter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTE.setIcon(icon5)
        self.actionNewUTE.setObjectName("actionNewUTE")
        self.actionNewUTS = QtWidgets.QAction(MainWindow)
        self.actionNewUTS.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icons/kx/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTS.setIcon(icon6)
        self.actionNewUTS.setObjectName("actionNewUTS")
        self.actionNewUTM = QtWidgets.QAction(MainWindow)
        self.actionNewUTM.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icons/kx/merchant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTM.setIcon(icon7)
        self.actionNewUTM.setObjectName("actionNewUTM")
        self.actionNewTLK = QtWidgets.QAction(MainWindow)
        self.actionNewTLK.setEnabled(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/icons/kx/tlk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewTLK.setIcon(icon8)
        self.actionNewTLK.setObjectName("actionNewTLK")
        self.actionNewUTI = QtWidgets.QAction(MainWindow)
        self.actionNewUTI.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/icons/kx/item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewUTI.setIcon(icon9)
        self.actionNewUTI.setObjectName("actionNewUTI")
        self.actionNewDLG = QtWidgets.QAction(MainWindow)
        self.actionNewDLG.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/icons/kx/dialog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewDLG.setIcon(icon10)
        self.actionNewDLG.setObjectName("actionNewDLG")
        self.actionNewNSS = QtWidgets.QAction(MainWindow)
        self.actionNewNSS.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/icons/kx/script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewNSS.setIcon(icon11)
        self.actionNewNSS.setObjectName("actionNewNSS")
        self.actionEditJRL = QtWidgets.QAction(MainWindow)
        self.actionEditJRL.setEnabled(False)
        self.actionEditJRL.setObjectName("actionEditJRL")
        self.actionFileSearch = QtWidgets.QAction(MainWindow)
        self.actionFileSearch.setEnabled(False)
        self.actionFileSearch.setObjectName("actionFileSearch")
        self.actionGeometryEditor = QtWidgets.QAction(MainWindow)
        self.actionGeometryEditor.setEnabled(False)
        self.actionGeometryEditor.setObjectName("actionGeometryEditor")
        self.defaultLight = QtWidgets.QAction(MainWindow)
        self.defaultLight.setObjectName("defaultLight")
        self.breezeDark = QtWidgets.QAction(MainWindow)
        self.breezeDark.setObjectName("breezeDark")
        self.darkManualTheme2 = QtWidgets.QAction(MainWindow)
        self.darkManualTheme2.setObjectName("darkManualTheme2")
        self.actionIndoorMapBuilder = QtWidgets.QAction(MainWindow)
        self.actionIndoorMapBuilder.setEnabled(False)
        self.actionIndoorMapBuilder.setObjectName("actionIndoorMapBuilder")
        self.actionEditModule = QtWidgets.QAction(MainWindow)
        self.actionEditModule.setEnabled(False)
        self.actionEditModule.setObjectName("actionEditModule")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionDiscordHolocronToolset = QtWidgets.QAction(MainWindow)
        self.actionDiscordHolocronToolset.setObjectName("actionDiscordHolocronToolset")
        self.actionDiscordKotOR = QtWidgets.QAction(MainWindow)
        self.actionDiscordKotOR.setObjectName("actionDiscordKotOR")
        self.actionDiscordDeadlyStream = QtWidgets.QAction(MainWindow)
        self.actionDiscordDeadlyStream.setObjectName("actionDiscordDeadlyStream")
        self.actionModuleDesigner = QtWidgets.QAction(MainWindow)
        self.actionModuleDesigner.setEnabled(False)
        self.actionModuleDesigner.setObjectName("actionModuleDesigner")
        self.menuNew.addAction(self.actionNewDLG)
        self.menuNew.addAction(self.actionNewNSS)
        self.menuNew.addAction(self.actionNewUTC)
        self.menuNew.addAction(self.actionNewUTP)
        self.menuNew.addAction(self.actionNewUTD)
        self.menuNew.addAction(self.actionNewUTI)
        self.menuNew.addAction(self.actionNewUTS)
        self.menuNew.addAction(self.actionNewUTT)
        self.menuNew.addAction(self.actionNewUTM)
        self.menuNew.addAction(self.actionNewUTW)
        self.menuNew.addAction(self.actionNewUTE)
        self.menuNew.addAction(self.actionNewTLK)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionNewGFF)
        self.menuNew.addAction(self.actionNewERF)
        self.menuNew.addAction(self.actionNewTXT)
        self.menuNew.addAction(self.actionNewSSF)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.openAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionRecent_Files)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEditTLK)
        self.menuEdit.addAction(self.actionEditJRL)
        self.menuTheme.addAction(self.defaultLight)
        self.menuTheme.addAction(self.breezeDark)
        self.menuTheme.addAction(self.darkManualTheme2)
        self.menuTools.addAction(self.actionModuleDesigner)
        self.menuTools.addAction(self.actionIndoorMapBuilder)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionFileSearch)
        self.menuTools.addAction(self.actionCloneModule)
        self.menuDiscord.addAction(self.actionDiscordHolocronToolset)
        self.menuDiscord.addAction(self.actionDiscordKotOR)
        self.menuDiscord.addAction(self.actionDiscordDeadlyStream)
        self.menuHelp.addAction(self.actionHelpAbout)
        self.menuHelp.addAction(self.menuDiscord.menuAction())
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionHelpUpdates)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.resourceTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Holocron Toolset"))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.coreTab), _translate("MainWindow", "Core"))
        self.specialActionButton.setText(_translate("MainWindow", "Open in Module Designer"))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.modulesTab), _translate("MainWindow", "Modules"))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.overrideTab), _translate("MainWindow", "Override"))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.texturesTab), _translate("MainWindow", "Textures"))
        self.openButton.setText(_translate("MainWindow", "Open Selected"))
        self.extractButton.setText(_translate("MainWindow", "Extract Selected"))
        self.tpcGroup_2.setTitle(_translate("MainWindow", "TPC"))
        self.tpcDecompileCheckbox.setText(_translate("MainWindow", "Decompile"))
        self.tpcTxiCheckbox.setText(_translate("MainWindow", "Extract TXI"))
        self.mdlGroup_2.setTitle(_translate("MainWindow", "MDL"))
        self.mdlDecompileCheckbox.setText(_translate("MainWindow", "Decompile"))
        self.mdlTexturesCheckbox.setText(_translate("MainWindow", "Extract Textures"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuDiscord.setTitle(_translate("MainWindow", "Discord"))
        self.cloneModuleAction.setText(_translate("MainWindow", "Clone Module"))
        self.actionRecent_Files.setText(_translate("MainWindow", "Recent Files"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for Updates"))
        self.actionCreature.setText(_translate("MainWindow", "Creature"))
        self.actionItem.setText(_translate("MainWindow", "Item"))
        self.actionDoor.setText(_translate("MainWindow", "Door"))
        self.actionPlaceable.setText(_translate("MainWindow", "Placeable"))
        self.actionMerchant.setText(_translate("MainWindow", "Merchant"))
        self.actionEncounter.setText(_translate("MainWindow", "Encounter"))
        self.actionTrigger.setText(_translate("MainWindow", "Trigger"))
        self.actionWaypoint.setText(_translate("MainWindow", "Waypoint"))
        self.actionDialog.setText(_translate("MainWindow", "Dialog"))
        self.openAction.setText(_translate("MainWindow", "Open"))
        self.actionNewGFF.setText(_translate("MainWindow", "GFF"))
        self.actionNewERF.setText(_translate("MainWindow", "ERF"))
        self.actionNewTXT.setText(_translate("MainWindow", "TXT"))
        self.actionEditTLK.setText(_translate("MainWindow", "Edit Talk Table"))
        self.actionHelpUpdates.setText(_translate("MainWindow", "Check For Updates"))
        self.actionHelpAbout.setText(_translate("MainWindow", "About"))
        self.actionNewSSF.setText(_translate("MainWindow", "SSF"))
        self.actionNewUTC.setText(_translate("MainWindow", "Creature"))
        self.actionCloneModule.setText(_translate("MainWindow", "Clone Module"))
        self.actionNewUTP.setText(_translate("MainWindow", "Placeable"))
        self.actionNewUTD.setText(_translate("MainWindow", "Door"))
        self.actionNewUTW.setText(_translate("MainWindow", "Waypoint"))
        self.actionNewUTT.setText(_translate("MainWindow", "Trigger"))
        self.actionNewUTE.setText(_translate("MainWindow", "Encounter"))
        self.actionNewUTS.setText(_translate("MainWindow", "Sound"))
        self.actionNewUTM.setText(_translate("MainWindow", "Merchant"))
        self.actionNewTLK.setText(_translate("MainWindow", "TalkTable"))
        self.actionNewUTI.setText(_translate("MainWindow", "Item"))
        self.actionNewDLG.setText(_translate("MainWindow", "Dialog"))
        self.actionNewNSS.setText(_translate("MainWindow", "Script"))
        self.actionEditJRL.setText(_translate("MainWindow", "Edit Journal"))
        self.actionFileSearch.setText(_translate("MainWindow", "File Search"))
        self.actionGeometryEditor.setText(_translate("MainWindow", "Geometry Editor"))
        self.defaultLight.setText(_translate("MainWindow", "Default (Light)"))
        self.breezeDark.setText(_translate("MainWindow", "Breeze (Dark)"))
        self.darkManualTheme2.setText(_translate("MainWindow", "Fusion (Dark)"))
        self.actionIndoorMapBuilder.setText(_translate("MainWindow", "Indoor Map Builder"))
        self.actionEditModule.setText(_translate("MainWindow", "Edit Module"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionDiscordHolocronToolset.setText(_translate("MainWindow", "Holocron Toolset"))
        self.actionDiscordKotOR.setText(_translate("MainWindow", "r/KotOR"))
        self.actionDiscordDeadlyStream.setText(_translate("MainWindow", "Deadly Stream"))
        self.actionModuleDesigner.setText(_translate("MainWindow", "Module Designer"))
from toolset.gui.widgets.main_widgets import ResourceList, TextureList
import resources_rc
