# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs\inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 611)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.coreSearchEdit = QtWidgets.QLineEdit(self.tab)
        self.coreSearchEdit.setObjectName("coreSearchEdit")
        self.verticalLayout_3.addWidget(self.coreSearchEdit)
        self.coreTree = QtWidgets.QTreeView(self.tab)
        self.coreTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.coreTree.setDragEnabled(True)
        self.coreTree.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.coreTree.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.coreTree.setAlternatingRowColors(True)
        self.coreTree.setObjectName("coreTree")
        self.coreTree.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.coreTree)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.modulesSearchEdit = QtWidgets.QLineEdit(self.tab_2)
        self.modulesSearchEdit.setObjectName("modulesSearchEdit")
        self.verticalLayout_4.addWidget(self.modulesSearchEdit)
        self.modulesTree = QtWidgets.QTreeView(self.tab_2)
        self.modulesTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.modulesTree.setDragEnabled(True)
        self.modulesTree.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.modulesTree.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.modulesTree.setAlternatingRowColors(True)
        self.modulesTree.setHeaderHidden(True)
        self.modulesTree.setObjectName("modulesTree")
        self.verticalLayout_4.addWidget(self.modulesTree)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.overrideSearchEdit = QtWidgets.QLineEdit(self.tab_5)
        self.overrideSearchEdit.setObjectName("overrideSearchEdit")
        self.verticalLayout_5.addWidget(self.overrideSearchEdit)
        self.overrideTree = QtWidgets.QTreeView(self.tab_5)
        self.overrideTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.overrideTree.setDragEnabled(True)
        self.overrideTree.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.overrideTree.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.overrideTree.setAlternatingRowColors(True)
        self.overrideTree.setHeaderHidden(True)
        self.overrideTree.setObjectName("overrideTree")
        self.verticalLayout_5.addWidget(self.overrideTree)
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_2.setAcceptDrops(True)
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.standardEquipmentTab = QtWidgets.QWidget()
        self.standardEquipmentTab.setAutoFillBackground(False)
        self.standardEquipmentTab.setStyleSheet("background-color: black;")
        self.standardEquipmentTab.setObjectName("standardEquipmentTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.standardEquipmentTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.headFrame = DropFrame(self.standardEquipmentTab)
        self.headFrame.setMinimumSize(QtCore.QSize(64, 64))
        self.headFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.headFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.headFrame.setAcceptDrops(True)
        self.headFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headFrame.setObjectName("headFrame")
        self.headPicture = QtWidgets.QLabel(self.headFrame)
        self.headPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.headPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.headPicture.setStyleSheet("background-color: none;")
        self.headPicture.setText("")
        self.headPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_head.png"))
        self.headPicture.setScaledContents(True)
        self.headPicture.setObjectName("headPicture")
        self.slotPicture_3 = QtWidgets.QLabel(self.headFrame)
        self.slotPicture_3.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_3.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_3.setText("")
        self.slotPicture_3.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_3.setScaledContents(True)
        self.slotPicture_3.setObjectName("slotPicture_3")
        self.slotPicture_3.raise_()
        self.headPicture.raise_()
        self.gridLayout.addWidget(self.headFrame, 0, 1, 1, 1)
        self.beltFrame = DropFrame(self.standardEquipmentTab)
        self.beltFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.beltFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.beltFrame.setAcceptDrops(True)
        self.beltFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.beltFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.beltFrame.setObjectName("beltFrame")
        self.beltPicture = QtWidgets.QLabel(self.beltFrame)
        self.beltPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.beltPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.beltPicture.setStyleSheet("background-color: none;")
        self.beltPicture.setText("")
        self.beltPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_belt.png"))
        self.beltPicture.setScaledContents(True)
        self.beltPicture.setObjectName("beltPicture")
        self.slotPicture_8 = QtWidgets.QLabel(self.beltFrame)
        self.slotPicture_8.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_8.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_8.setText("")
        self.slotPicture_8.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_8.setScaledContents(True)
        self.slotPicture_8.setObjectName("slotPicture_8")
        self.slotPicture_8.raise_()
        self.beltPicture.raise_()
        self.gridLayout.addWidget(self.beltFrame, 2, 1, 1, 1)
        self.armrFrame = DropFrame(self.standardEquipmentTab)
        self.armrFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.armrFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.armrFrame.setAcceptDrops(True)
        self.armrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.armrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.armrFrame.setObjectName("armrFrame")
        self.armrPicture = QtWidgets.QLabel(self.armrFrame)
        self.armrPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.armrPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.armrPicture.setStyleSheet("background-color: none;")
        self.armrPicture.setText("")
        self.armrPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_forearm_r.png"))
        self.armrPicture.setScaledContents(True)
        self.armrPicture.setObjectName("armrPicture")
        self.slotPicture_10 = QtWidgets.QLabel(self.armrFrame)
        self.slotPicture_10.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_10.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_10.setText("")
        self.slotPicture_10.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_10.setScaledContents(True)
        self.slotPicture_10.setObjectName("slotPicture_10")
        self.slotPicture_10.raise_()
        self.armrPicture.raise_()
        self.gridLayout.addWidget(self.armrFrame, 1, 3, 1, 1)
        self.handrFrame = DropFrame(self.standardEquipmentTab)
        self.handrFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.handrFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.handrFrame.setAcceptDrops(True)
        self.handrFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.handrFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.handrFrame.setObjectName("handrFrame")
        self.handrPicture = QtWidgets.QLabel(self.handrFrame)
        self.handrPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.handrPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.handrPicture.setStyleSheet("background-color: none;")
        self.handrPicture.setText("")
        self.handrPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_hand_r.png"))
        self.handrPicture.setScaledContents(True)
        self.handrPicture.setObjectName("handrPicture")
        self.slotPicture_9 = QtWidgets.QLabel(self.handrFrame)
        self.slotPicture_9.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_9.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_9.setText("")
        self.slotPicture_9.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_9.setScaledContents(True)
        self.slotPicture_9.setObjectName("slotPicture_9")
        self.slotPicture_9.raise_()
        self.handrPicture.raise_()
        self.gridLayout.addWidget(self.handrFrame, 2, 3, 1, 1)
        self.handlFrame = DropFrame(self.standardEquipmentTab)
        self.handlFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.handlFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.handlFrame.setAcceptDrops(True)
        self.handlFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.handlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.handlFrame.setObjectName("handlFrame")
        self.handlPicture = QtWidgets.QLabel(self.handlFrame)
        self.handlPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.handlPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.handlPicture.setStyleSheet("background-color: none;")
        self.handlPicture.setText("")
        self.handlPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_hand_l.png"))
        self.handlPicture.setScaledContents(True)
        self.handlPicture.setObjectName("handlPicture")
        self.slotPicture_7 = QtWidgets.QLabel(self.handlFrame)
        self.slotPicture_7.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_7.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_7.setText("")
        self.slotPicture_7.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_7.setScaledContents(True)
        self.slotPicture_7.setObjectName("slotPicture_7")
        self.slotPicture_7.raise_()
        self.handlPicture.raise_()
        self.gridLayout.addWidget(self.handlFrame, 2, 0, 1, 1)
        self.implantFrame = DropFrame(self.standardEquipmentTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.implantFrame.sizePolicy().hasHeightForWidth())
        self.implantFrame.setSizePolicy(sizePolicy)
        self.implantFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.implantFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.implantFrame.setAcceptDrops(True)
        self.implantFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.implantFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.implantFrame.setObjectName("implantFrame")
        self.implantPicture = QtWidgets.QLabel(self.implantFrame)
        self.implantPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.implantPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.implantPicture.setAcceptDrops(True)
        self.implantPicture.setStyleSheet("background-color: none;")
        self.implantPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_implant.png"))
        self.implantPicture.setScaledContents(True)
        self.implantPicture.setObjectName("implantPicture")
        self.slotPicture = QtWidgets.QLabel(self.implantFrame)
        self.slotPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture.setAcceptDrops(True)
        self.slotPicture.setText("")
        self.slotPicture.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture.setScaledContents(True)
        self.slotPicture.setObjectName("slotPicture")
        self.slotPicture.raise_()
        self.implantPicture.raise_()
        self.gridLayout.addWidget(self.implantFrame, 0, 0, 1, 1)
        self.gauntletFrame = DropFrame(self.standardEquipmentTab)
        self.gauntletFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.gauntletFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.gauntletFrame.setAcceptDrops(True)
        self.gauntletFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gauntletFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gauntletFrame.setObjectName("gauntletFrame")
        self.gauntletPicture = QtWidgets.QLabel(self.gauntletFrame)
        self.gauntletPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.gauntletPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.gauntletPicture.setStyleSheet("background-color: none;")
        self.gauntletPicture.setText("")
        self.gauntletPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_gauntlet.png"))
        self.gauntletPicture.setScaledContents(True)
        self.gauntletPicture.setObjectName("gauntletPicture")
        self.slotPicture_4 = QtWidgets.QLabel(self.gauntletFrame)
        self.slotPicture_4.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_4.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_4.setText("")
        self.slotPicture_4.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_4.setScaledContents(True)
        self.slotPicture_4.setObjectName("slotPicture_4")
        self.slotPicture_4.raise_()
        self.gauntletPicture.raise_()
        self.gridLayout.addWidget(self.gauntletFrame, 0, 3, 1, 1)
        self.armorFrame = DropFrame(self.standardEquipmentTab)
        self.armorFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.armorFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.armorFrame.setAcceptDrops(True)
        self.armorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.armorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.armorFrame.setObjectName("armorFrame")
        self.armorPicture = QtWidgets.QLabel(self.armorFrame)
        self.armorPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.armorPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.armorPicture.setStyleSheet("background-color: none;")
        self.armorPicture.setText("")
        self.armorPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_armor.png"))
        self.armorPicture.setScaledContents(True)
        self.armorPicture.setObjectName("armorPicture")
        self.slotPicture_6 = QtWidgets.QLabel(self.armorFrame)
        self.slotPicture_6.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_6.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_6.setText("")
        self.slotPicture_6.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_6.setScaledContents(True)
        self.slotPicture_6.setObjectName("slotPicture_6")
        self.slotPicture_6.raise_()
        self.armorPicture.raise_()
        self.gridLayout.addWidget(self.armorFrame, 1, 1, 1, 1)
        self.armlFrame = DropFrame(self.standardEquipmentTab)
        self.armlFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.armlFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.armlFrame.setAcceptDrops(True)
        self.armlFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.armlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.armlFrame.setObjectName("armlFrame")
        self.armlPicture = QtWidgets.QLabel(self.armlFrame)
        self.armlPicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.armlPicture.setMaximumSize(QtCore.QSize(64, 64))
        self.armlPicture.setStyleSheet("background-color: none;")
        self.armlPicture.setText("")
        self.armlPicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_forearm_l.png"))
        self.armlPicture.setScaledContents(True)
        self.armlPicture.setObjectName("armlPicture")
        self.slotPicture_5 = QtWidgets.QLabel(self.armlFrame)
        self.slotPicture_5.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_5.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_5.setText("")
        self.slotPicture_5.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_5.setScaledContents(True)
        self.slotPicture_5.setObjectName("slotPicture_5")
        self.slotPicture_5.raise_()
        self.armlPicture.raise_()
        self.gridLayout.addWidget(self.armlFrame, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.standardEquipmentTab, "")
        self.naturalEquipmentTab = QtWidgets.QWidget()
        self.naturalEquipmentTab.setStyleSheet("background-color: black;")
        self.naturalEquipmentTab.setObjectName("naturalEquipmentTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.naturalEquipmentTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.claw1Frame = DropFrame(self.naturalEquipmentTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.claw1Frame.sizePolicy().hasHeightForWidth())
        self.claw1Frame.setSizePolicy(sizePolicy)
        self.claw1Frame.setMaximumSize(QtCore.QSize(64, 64))
        self.claw1Frame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.claw1Frame.setAcceptDrops(True)
        self.claw1Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.claw1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.claw1Frame.setObjectName("claw1Frame")
        self.claw1Picture = QtWidgets.QLabel(self.claw1Frame)
        self.claw1Picture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.claw1Picture.setMaximumSize(QtCore.QSize(64, 64))
        self.claw1Picture.setStyleSheet("background-color: none;")
        self.claw1Picture.setText("")
        self.claw1Picture.setPixmap(QtGui.QPixmap(":/images/inventory/human_gauntlet.png"))
        self.claw1Picture.setScaledContents(True)
        self.claw1Picture.setObjectName("claw1Picture")
        self.slotPicture_2 = QtWidgets.QLabel(self.claw1Frame)
        self.slotPicture_2.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_2.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_2.setText("")
        self.slotPicture_2.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_2.setScaledContents(True)
        self.slotPicture_2.setObjectName("slotPicture_2")
        self.slotPicture_2.raise_()
        self.claw1Picture.raise_()
        self.gridLayout_2.addWidget(self.claw1Frame, 0, 0, 1, 1)
        self.claw2Frame = DropFrame(self.naturalEquipmentTab)
        self.claw2Frame.setMinimumSize(QtCore.QSize(64, 64))
        self.claw2Frame.setMaximumSize(QtCore.QSize(64, 64))
        self.claw2Frame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.claw2Frame.setAcceptDrops(True)
        self.claw2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.claw2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.claw2Frame.setObjectName("claw2Frame")
        self.claw2Picture = QtWidgets.QLabel(self.claw2Frame)
        self.claw2Picture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.claw2Picture.setMaximumSize(QtCore.QSize(64, 64))
        self.claw2Picture.setStyleSheet("background-color: none;")
        self.claw2Picture.setText("")
        self.claw2Picture.setPixmap(QtGui.QPixmap(":/images/inventory/human_gauntlet.png"))
        self.claw2Picture.setScaledContents(True)
        self.claw2Picture.setObjectName("claw2Picture")
        self.slotPicture_13 = QtWidgets.QLabel(self.claw2Frame)
        self.slotPicture_13.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_13.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_13.setText("")
        self.slotPicture_13.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_13.setScaledContents(True)
        self.slotPicture_13.setObjectName("slotPicture_13")
        self.slotPicture_13.raise_()
        self.claw2Picture.raise_()
        self.gridLayout_2.addWidget(self.claw2Frame, 0, 1, 1, 1)
        self.claw3Frame = DropFrame(self.naturalEquipmentTab)
        self.claw3Frame.setMaximumSize(QtCore.QSize(64, 64))
        self.claw3Frame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.claw3Frame.setAcceptDrops(True)
        self.claw3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.claw3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.claw3Frame.setObjectName("claw3Frame")
        self.claw3Picture = QtWidgets.QLabel(self.claw3Frame)
        self.claw3Picture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.claw3Picture.setMaximumSize(QtCore.QSize(64, 64))
        self.claw3Picture.setStyleSheet("background-color: none;")
        self.claw3Picture.setText("")
        self.claw3Picture.setPixmap(QtGui.QPixmap(":/images/inventory/human_gauntlet.png"))
        self.claw3Picture.setScaledContents(True)
        self.claw3Picture.setObjectName("claw3Picture")
        self.slotPicture_11 = QtWidgets.QLabel(self.claw3Frame)
        self.slotPicture_11.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_11.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_11.setText("")
        self.slotPicture_11.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_11.setScaledContents(True)
        self.slotPicture_11.setObjectName("slotPicture_11")
        self.slotPicture_11.raise_()
        self.claw3Picture.raise_()
        self.gridLayout_2.addWidget(self.claw3Frame, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.naturalEquipmentTab)
        self.frame.setMaximumSize(QtCore.QSize(64, 64))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.hideFrame = DropFrame(self.naturalEquipmentTab)
        self.hideFrame.setMaximumSize(QtCore.QSize(64, 64))
        self.hideFrame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.hideFrame.setAcceptDrops(True)
        self.hideFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hideFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hideFrame.setObjectName("hideFrame")
        self.hidePicture = QtWidgets.QLabel(self.hideFrame)
        self.hidePicture.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.hidePicture.setMaximumSize(QtCore.QSize(64, 64))
        self.hidePicture.setStyleSheet("background-color: none;")
        self.hidePicture.setText("")
        self.hidePicture.setPixmap(QtGui.QPixmap(":/images/inventory/human_armor.png"))
        self.hidePicture.setScaledContents(True)
        self.hidePicture.setObjectName("hidePicture")
        self.slotPicture_12 = QtWidgets.QLabel(self.hideFrame)
        self.slotPicture_12.setGeometry(QtCore.QRect(0, 0, 64, 64))
        self.slotPicture_12.setMaximumSize(QtCore.QSize(64, 64))
        self.slotPicture_12.setText("")
        self.slotPicture_12.setPixmap(QtGui.QPixmap(":/images/inventory/slot.png"))
        self.slotPicture_12.setScaledContents(True)
        self.slotPicture_12.setObjectName("slotPicture_12")
        self.slotPicture_12.raise_()
        self.hidePicture.raise_()
        self.gridLayout_2.addWidget(self.hideFrame, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.naturalEquipmentTab)
        self.frame_2.setMaximumSize(QtCore.QSize(64, 64))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 1, 2, 1, 1)
        self.claw1Frame.raise_()
        self.claw2Frame.raise_()
        self.claw3Frame.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.hideFrame.raise_()
        self.tabWidget_2.addTab(self.naturalEquipmentTab, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.tabWidget_3 = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.contentsTable = InventoryTable(self.tab_6)
        self.contentsTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.contentsTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentsTable.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.contentsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.contentsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.contentsTable.setIconSize(QtCore.QSize(48, 48))
        self.contentsTable.setObjectName("contentsTable")
        self.contentsTable.setColumnCount(3)
        self.contentsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.contentsTable.setHorizontalHeaderItem(2, item)
        self.contentsTable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.contentsTable, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.verticalLayout.addWidget(self.tabWidget_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inventory Editor"))
        self.coreSearchEdit.setPlaceholderText(_translate("Dialog", "search..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Core Items"))
        self.modulesSearchEdit.setPlaceholderText(_translate("Dialog", "search..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Module Items"))
        self.overrideSearchEdit.setPlaceholderText(_translate("Dialog", "search..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Override Items"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.standardEquipmentTab), _translate("Dialog", "Standard Equipment"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.naturalEquipmentTab), _translate("Dialog", "Natural Equipment"))
        item = self.contentsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Icon"))
        item = self.contentsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ResRef"))
        item = self.contentsTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Name"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("Dialog", "Contents"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
from toolset.gui.dialogs.inventory import DropFrame, InventoryTable
import toolset.resources_rc
