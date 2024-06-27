# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from toolset.gui.widgets.main_widgets import ResourceList
from toolset.gui.widgets.main_widgets import TextureList

from toolset.rcc import resources_rc_pyside2
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(512, 471)
        MainWindow.setAcceptDrops(True)
        self.cloneModuleAction = QAction(MainWindow)
        self.cloneModuleAction.setObjectName(u"cloneModuleAction")
        self.actionRecent_Files = QAction(MainWindow)
        self.actionRecent_Files.setObjectName(u"actionRecent_Files")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionCheck_for_Updates = QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName(u"actionCheck_for_Updates")
        self.actionCreature = QAction(MainWindow)
        self.actionCreature.setObjectName(u"actionCreature")
        self.actionItem = QAction(MainWindow)
        self.actionItem.setObjectName(u"actionItem")
        self.actionDoor = QAction(MainWindow)
        self.actionDoor.setObjectName(u"actionDoor")
        self.actionPlaceable = QAction(MainWindow)
        self.actionPlaceable.setObjectName(u"actionPlaceable")
        self.actionMerchant = QAction(MainWindow)
        self.actionMerchant.setObjectName(u"actionMerchant")
        self.actionEncounter = QAction(MainWindow)
        self.actionEncounter.setObjectName(u"actionEncounter")
        self.actionTrigger = QAction(MainWindow)
        self.actionTrigger.setObjectName(u"actionTrigger")
        self.actionWaypoint = QAction(MainWindow)
        self.actionWaypoint.setObjectName(u"actionWaypoint")
        self.actionDialog = QAction(MainWindow)
        self.actionDialog.setObjectName(u"actionDialog")
        self.actionDialog.setEnabled(False)
        self.openAction = QAction(MainWindow)
        self.openAction.setObjectName(u"openAction")
        self.actionNewGFF = QAction(MainWindow)
        self.actionNewGFF.setObjectName(u"actionNewGFF")
        self.actionNewERF = QAction(MainWindow)
        self.actionNewERF.setObjectName(u"actionNewERF")
        self.actionNewTXT = QAction(MainWindow)
        self.actionNewTXT.setObjectName(u"actionNewTXT")
        self.actionEditTLK = QAction(MainWindow)
        self.actionEditTLK.setObjectName(u"actionEditTLK")
        self.actionEditTLK.setEnabled(False)
        self.actionHelpUpdates = QAction(MainWindow)
        self.actionHelpUpdates.setObjectName(u"actionHelpUpdates")
        self.actionHelpAbout = QAction(MainWindow)
        self.actionHelpAbout.setObjectName(u"actionHelpAbout")
        self.actionNewSSF = QAction(MainWindow)
        self.actionNewSSF.setObjectName(u"actionNewSSF")
        self.actionNewUTC = QAction(MainWindow)
        self.actionNewUTC.setObjectName(u"actionNewUTC")
        self.actionNewUTC.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/images/icons/kx/creature.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionNewUTC.setIcon(icon)
        self.actionCloneModule = QAction(MainWindow)
        self.actionCloneModule.setObjectName(u"actionCloneModule")
        self.actionCloneModule.setEnabled(False)
        self.actionNewUTP = QAction(MainWindow)
        self.actionNewUTP.setObjectName(u"actionNewUTP")
        self.actionNewUTP.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/kx/placeable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTP.setIcon(icon1)
        self.actionNewUTD = QAction(MainWindow)
        self.actionNewUTD.setObjectName(u"actionNewUTD")
        self.actionNewUTD.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/kx/door.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTD.setIcon(icon2)
        self.actionNewUTW = QAction(MainWindow)
        self.actionNewUTW.setObjectName(u"actionNewUTW")
        self.actionNewUTW.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/kx/waypoint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTW.setIcon(icon3)
        self.actionNewUTT = QAction(MainWindow)
        self.actionNewUTT.setObjectName(u"actionNewUTT")
        self.actionNewUTT.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/kx/trigger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTT.setIcon(icon4)
        self.actionNewUTE = QAction(MainWindow)
        self.actionNewUTE.setObjectName(u"actionNewUTE")
        self.actionNewUTE.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/kx/encounter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTE.setIcon(icon5)
        self.actionNewUTS = QAction(MainWindow)
        self.actionNewUTS.setObjectName(u"actionNewUTS")
        self.actionNewUTS.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/images/icons/kx/sound.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTS.setIcon(icon6)
        self.actionNewUTM = QAction(MainWindow)
        self.actionNewUTM.setObjectName(u"actionNewUTM")
        self.actionNewUTM.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/images/icons/kx/merchant.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTM.setIcon(icon7)
        self.actionNewTLK = QAction(MainWindow)
        self.actionNewTLK.setObjectName(u"actionNewTLK")
        self.actionNewTLK.setEnabled(True)
        icon8 = QIcon()
        icon8.addFile(u":/images/icons/kx/tlk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewTLK.setIcon(icon8)
        self.actionNewUTI = QAction(MainWindow)
        self.actionNewUTI.setObjectName(u"actionNewUTI")
        self.actionNewUTI.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u":/images/icons/kx/item.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewUTI.setIcon(icon9)
        self.actionNewDLG = QAction(MainWindow)
        self.actionNewDLG.setObjectName(u"actionNewDLG")
        self.actionNewDLG.setEnabled(False)
        icon10 = QIcon()
        icon10.addFile(u":/images/icons/kx/dialog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewDLG.setIcon(icon10)
        self.actionNewNSS = QAction(MainWindow)
        self.actionNewNSS.setObjectName(u"actionNewNSS")
        self.actionNewNSS.setEnabled(False)
        icon11 = QIcon()
        icon11.addFile(u":/images/icons/kx/script.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewNSS.setIcon(icon11)
        self.actionEditJRL = QAction(MainWindow)
        self.actionEditJRL.setObjectName(u"actionEditJRL")
        self.actionEditJRL.setEnabled(False)
        self.actionFileSearch = QAction(MainWindow)
        self.actionFileSearch.setObjectName(u"actionFileSearch")
        self.actionFileSearch.setEnabled(False)
        self.actionGeometryEditor = QAction(MainWindow)
        self.actionGeometryEditor.setObjectName(u"actionGeometryEditor")
        self.actionGeometryEditor.setEnabled(False)
        self.defaultLight = QAction(MainWindow)
        self.defaultLight.setObjectName(u"defaultLight")
        self.defaultDark = QAction(MainWindow)
        self.defaultDark.setObjectName(u"defaultDark")
        self.fusionLight = QAction(MainWindow)
        self.fusionLight.setObjectName(u"fusionLight")
        self.fusionDark = QAction(MainWindow)
        self.fusionDark.setObjectName(u"fusionDark")
        self.breezeDark = QAction(MainWindow)
        self.breezeDark.setObjectName(u"breezeDark")
        self.actionIndoorMapBuilder = QAction(MainWindow)
        self.actionIndoorMapBuilder.setObjectName(u"actionIndoorMapBuilder")
        self.actionIndoorMapBuilder.setEnabled(False)
        self.actionEditModule = QAction(MainWindow)
        self.actionEditModule.setObjectName(u"actionEditModule")
        self.actionEditModule.setEnabled(False)
        self.actionInstructions = QAction(MainWindow)
        self.actionInstructions.setObjectName(u"actionInstructions")
        self.actionDiscordHolocronToolset = QAction(MainWindow)
        self.actionDiscordHolocronToolset.setObjectName(u"actionDiscordHolocronToolset")
        self.actionDiscordKotOR = QAction(MainWindow)
        self.actionDiscordKotOR.setObjectName(u"actionDiscordKotOR")
        self.actionDiscordDeadlyStream = QAction(MainWindow)
        self.actionDiscordDeadlyStream.setObjectName(u"actionDiscordDeadlyStream")
        self.actionModuleDesigner = QAction(MainWindow)
        self.actionModuleDesigner.setObjectName(u"actionModuleDesigner")
        self.actionModuleDesigner.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gameCombo = QComboBox(self.centralwidget)
        self.gameCombo.setObjectName(u"gameCombo")

        self.verticalLayout_4.addWidget(self.gameCombo)

        self.resourceTabs = QTabWidget(self.centralwidget)
        self.resourceTabs.setObjectName(u"resourceTabs")
        self.coreTab = QWidget()
        self.coreTab.setObjectName(u"coreTab")
        self.verticalLayout_2 = QVBoxLayout(self.coreTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.coreWidget = ResourceList(self.coreTab)
        self.coreWidget.setObjectName(u"coreWidget")

        self.verticalLayout_2.addWidget(self.coreWidget)

        self.resourceTabs.addTab(self.coreTab, "")
        self.savesTab = QWidget()
        self.savesTab.setObjectName(u"savesTab")
        self.gridLayoutSaves = QGridLayout(self.savesTab)
        self.gridLayoutSaves.setSpacing(0)
        self.gridLayoutSaves.setObjectName(u"gridLayoutSaves")
        self.gridLayoutSaves.setContentsMargins(0, 0, 0, 0)
        self.savesWidget = ResourceList(self.savesTab)
        self.savesWidget.setObjectName(u"savesWidget")

        self.gridLayoutSaves.addWidget(self.savesWidget, 0, 0, 2, 2)

        self.resourceTabs.addTab(self.savesTab, "")
        self.modulesTab = QWidget()
        self.modulesTab.setObjectName(u"modulesTab")
        self.verticalLayoutModulesTab = QVBoxLayout(self.modulesTab)
        self.verticalLayoutModulesTab.setObjectName(u"verticalLayoutModulesTab")
        self.specialActionButton = QPushButton(self.modulesTab)
        self.specialActionButton.setObjectName(u"specialActionButton")

        self.verticalLayoutModulesTab.addWidget(self.specialActionButton)

        self.gridLayoutModules = QGridLayout()
        self.gridLayoutModules.setSpacing(0)
        self.gridLayoutModules.setObjectName(u"gridLayoutModules")
        self.gridLayoutModules.setContentsMargins(0, 0, 0, 0)
        self.modulesWidget = ResourceList(self.modulesTab)
        self.modulesWidget.setObjectName(u"modulesWidget")

        self.gridLayoutModules.addWidget(self.modulesWidget, 0, 0, 1, 2)


        self.verticalLayoutModulesTab.addLayout(self.gridLayoutModules)

        self.resourceTabs.addTab(self.modulesTab, "")
        self.overrideTab = QWidget()
        self.overrideTab.setObjectName(u"overrideTab")
        self.verticalLayout_3 = QVBoxLayout(self.overrideTab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.overrideWidget = ResourceList(self.overrideTab)
        self.overrideWidget.setObjectName(u"overrideWidget")

        self.verticalLayout_3.addWidget(self.overrideWidget)

        self.resourceTabs.addTab(self.overrideTab, "")
        self.texturesTab = QWidget()
        self.texturesTab.setObjectName(u"texturesTab")
        self.verticalLayout_6 = QVBoxLayout(self.texturesTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.texturesWidget = TextureList(self.texturesTab)
        self.texturesWidget.setObjectName(u"texturesWidget")

        self.verticalLayout_6.addWidget(self.texturesWidget)

        self.resourceTabs.addTab(self.texturesTab, "")

        self.verticalLayout_4.addWidget(self.resourceTabs)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.vboxlayout = QVBoxLayout()
        self.vboxlayout.setObjectName(u"vboxlayout")
        self.vboxlayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalSpacer_2 = QSpacerItem(124, 45, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vboxlayout.addItem(self.verticalSpacer_2)

        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.sidebar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.openButton = QPushButton(self.sidebar)
        self.openButton.setObjectName(u"openButton")

        self.verticalLayout_5.addWidget(self.openButton)

        self.extractButton = QPushButton(self.sidebar)
        self.extractButton.setObjectName(u"extractButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extractButton.sizePolicy().hasHeightForWidth())
        self.extractButton.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.extractButton)

        self.tpcGroup_2 = QGroupBox(self.sidebar)
        self.tpcGroup_2.setObjectName(u"tpcGroup_2")
        self.verticalLayout_10 = QVBoxLayout(self.tpcGroup_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tpcDecompileCheckbox = QCheckBox(self.tpcGroup_2)
        self.tpcDecompileCheckbox.setObjectName(u"tpcDecompileCheckbox")

        self.verticalLayout_10.addWidget(self.tpcDecompileCheckbox)

        self.tpcTxiCheckbox = QCheckBox(self.tpcGroup_2)
        self.tpcTxiCheckbox.setObjectName(u"tpcTxiCheckbox")

        self.verticalLayout_10.addWidget(self.tpcTxiCheckbox)


        self.verticalLayout_5.addWidget(self.tpcGroup_2)

        self.mdlGroup_2 = QGroupBox(self.sidebar)
        self.mdlGroup_2.setObjectName(u"mdlGroup_2")
        self.verticalLayout_9 = QVBoxLayout(self.mdlGroup_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.mdlDecompileCheckbox = QCheckBox(self.mdlGroup_2)
        self.mdlDecompileCheckbox.setObjectName(u"mdlDecompileCheckbox")

        self.verticalLayout_9.addWidget(self.mdlDecompileCheckbox)

        self.mdlTexturesCheckbox = QCheckBox(self.mdlGroup_2)
        self.mdlTexturesCheckbox.setObjectName(u"mdlTexturesCheckbox")

        self.verticalLayout_9.addWidget(self.mdlTexturesCheckbox)


        self.verticalLayout_5.addWidget(self.mdlGroup_2)


        self.vboxlayout.addWidget(self.sidebar)

        self.verticalSpacer = QSpacerItem(124, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vboxlayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.vboxlayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 512, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        self.menuRecentFiles = QMenu(self.menuFile)
        self.menuRecentFiles.setObjectName(u"menuRecentFiles")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTheme = QMenu(self.menubar)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuDiscord = QMenu(self.menuHelp)
        self.menuDiscord.setObjectName(u"menuDiscord")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.openAction)
        self.menuFile.addAction(self.menuRecentFiles.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
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
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEditTLK)
        self.menuEdit.addAction(self.actionEditJRL)
        self.menuTheme.addAction(self.defaultLight)
        self.menuTheme.addAction(self.defaultDark)
        self.menuTheme.addAction(self.fusionLight)
        self.menuTheme.addAction(self.fusionDark)
        self.menuTheme.addAction(self.breezeDark)
        self.menuTools.addAction(self.actionModuleDesigner)
        self.menuTools.addAction(self.actionIndoorMapBuilder)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionFileSearch)
        self.menuTools.addAction(self.actionCloneModule)
        self.menuHelp.addAction(self.actionHelpAbout)
        self.menuHelp.addAction(self.menuDiscord.menuAction())
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionHelpUpdates)
        self.menuDiscord.addAction(self.actionDiscordHolocronToolset)
        self.menuDiscord.addAction(self.actionDiscordKotOR)
        self.menuDiscord.addAction(self.actionDiscordDeadlyStream)

        self.retranslateUi(MainWindow)

        self.resourceTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Holocron Toolset", None))
        self.cloneModuleAction.setText(QCoreApplication.translate("MainWindow", u"Clone Module", None))
        self.actionRecent_Files.setText(QCoreApplication.translate("MainWindow", u"Recent Files", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionCheck_for_Updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates", None))
        self.actionCreature.setText(QCoreApplication.translate("MainWindow", u"Creature", None))
        self.actionItem.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.actionDoor.setText(QCoreApplication.translate("MainWindow", u"Door", None))
        self.actionPlaceable.setText(QCoreApplication.translate("MainWindow", u"Placeable", None))
        self.actionMerchant.setText(QCoreApplication.translate("MainWindow", u"Merchant", None))
        self.actionEncounter.setText(QCoreApplication.translate("MainWindow", u"Encounter", None))
        self.actionTrigger.setText(QCoreApplication.translate("MainWindow", u"Trigger", None))
        self.actionWaypoint.setText(QCoreApplication.translate("MainWindow", u"Waypoint", None))
        self.actionDialog.setText(QCoreApplication.translate("MainWindow", u"Dialog", None))
        self.openAction.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNewGFF.setText(QCoreApplication.translate("MainWindow", u"GFF", None))
        self.actionNewERF.setText(QCoreApplication.translate("MainWindow", u"ERF", None))
        self.actionNewTXT.setText(QCoreApplication.translate("MainWindow", u"TXT", None))
        self.actionEditTLK.setText(QCoreApplication.translate("MainWindow", u"Edit Talk Table", None))
        self.actionHelpUpdates.setText(QCoreApplication.translate("MainWindow", u"Check For Updates", None))
        self.actionHelpAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionNewSSF.setText(QCoreApplication.translate("MainWindow", u"SSF", None))
        self.actionNewUTC.setText(QCoreApplication.translate("MainWindow", u"Creature", None))
        self.actionCloneModule.setText(QCoreApplication.translate("MainWindow", u"Clone Module", None))
        self.actionNewUTP.setText(QCoreApplication.translate("MainWindow", u"Placeable", None))
        self.actionNewUTD.setText(QCoreApplication.translate("MainWindow", u"Door", None))
        self.actionNewUTW.setText(QCoreApplication.translate("MainWindow", u"Waypoint", None))
        self.actionNewUTT.setText(QCoreApplication.translate("MainWindow", u"Trigger", None))
        self.actionNewUTE.setText(QCoreApplication.translate("MainWindow", u"Encounter", None))
        self.actionNewUTS.setText(QCoreApplication.translate("MainWindow", u"Sound", None))
        self.actionNewUTM.setText(QCoreApplication.translate("MainWindow", u"Merchant", None))
        self.actionNewTLK.setText(QCoreApplication.translate("MainWindow", u"TalkTable", None))
        self.actionNewUTI.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.actionNewDLG.setText(QCoreApplication.translate("MainWindow", u"Dialog", None))
        self.actionNewNSS.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.actionEditJRL.setText(QCoreApplication.translate("MainWindow", u"Edit Journal", None))
        self.actionFileSearch.setText(QCoreApplication.translate("MainWindow", u"File Search", None))
        self.actionGeometryEditor.setText(QCoreApplication.translate("MainWindow", u"Geometry Editor", None))
        self.defaultLight.setText(QCoreApplication.translate("MainWindow", u"Native (Light)", None))
        self.defaultDark.setText(QCoreApplication.translate("MainWindow", u"Native (Dark)", None))
        self.fusionLight.setText(QCoreApplication.translate("MainWindow", u"Fusion (Light)", None))
        self.fusionDark.setText(QCoreApplication.translate("MainWindow", u"Fusion (Dark)", None))
        self.breezeDark.setText(QCoreApplication.translate("MainWindow", u"Breeze (Dark)", None))
        self.actionIndoorMapBuilder.setText(QCoreApplication.translate("MainWindow", u"Indoor Map Builder", None))
        self.actionEditModule.setText(QCoreApplication.translate("MainWindow", u"Edit Module", None))
        self.actionInstructions.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
        self.actionDiscordHolocronToolset.setText(QCoreApplication.translate("MainWindow", u"Holocron Toolset", None))
        self.actionDiscordKotOR.setText(QCoreApplication.translate("MainWindow", u"KOTOR Community Portal", None))
        self.actionDiscordDeadlyStream.setText(QCoreApplication.translate("MainWindow", u"Deadly Stream", None))
        self.actionModuleDesigner.setText(QCoreApplication.translate("MainWindow", u"Module Designer", None))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.coreTab), QCoreApplication.translate("MainWindow", u"Core", None))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.savesTab), QCoreApplication.translate("MainWindow", u"Saves", None))
        self.specialActionButton.setText(QCoreApplication.translate("MainWindow", u"Designer", None))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.modulesTab), QCoreApplication.translate("MainWindow", u"Modules", None))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.overrideTab), QCoreApplication.translate("MainWindow", u"Override", None))
        self.resourceTabs.setTabText(self.resourceTabs.indexOf(self.texturesTab), QCoreApplication.translate("MainWindow", u"Textures", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"Open Selected", None))
        self.extractButton.setText(QCoreApplication.translate("MainWindow", u"Extract Selected", None))
        self.tpcGroup_2.setTitle(QCoreApplication.translate("MainWindow", u"TPC", None))
        self.tpcDecompileCheckbox.setText(QCoreApplication.translate("MainWindow", u"Decompile", None))
        self.tpcTxiCheckbox.setText(QCoreApplication.translate("MainWindow", u"Extract TXI", None))
        self.mdlGroup_2.setTitle(QCoreApplication.translate("MainWindow", u"MDL", None))
        self.mdlDecompileCheckbox.setText(QCoreApplication.translate("MainWindow", u"Decompile", None))
        self.mdlTexturesCheckbox.setText(QCoreApplication.translate("MainWindow", u"Extract Textures", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New", None))
        self.menuRecentFiles.setTitle(QCoreApplication.translate("MainWindow", u"Recent Files", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuDiscord.setTitle(QCoreApplication.translate("MainWindow", u"Discord", None))
    # retranslateUi

