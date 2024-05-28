# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/editors/sav.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGlobalVars = QtWidgets.QWidget()
        self.tabGlobalVars.setObjectName("tabGlobalVars")
        self.verticalLayoutGlobalVars = QtWidgets.QVBoxLayout(self.tabGlobalVars)
        self.verticalLayoutGlobalVars.setObjectName("verticalLayoutGlobalVars")
        self.tableWidgetGlobalVars = QtWidgets.QTableWidget(self.tabGlobalVars)
        self.tableWidgetGlobalVars.setRowCount(16)
        self.tableWidgetGlobalVars.setColumnCount(2)
        self.tableWidgetGlobalVars.setObjectName("tableWidgetGlobalVars")
        self.verticalLayoutGlobalVars.addWidget(self.tableWidgetGlobalVars)
        self.tabWidget.addTab(self.tabGlobalVars, "")
        self.tabCachedModules = QtWidgets.QWidget()
        self.tabCachedModules.setObjectName("tabCachedModules")
        self.verticalLayoutCachedModules = QtWidgets.QVBoxLayout(self.tabCachedModules)
        self.verticalLayoutCachedModules.setObjectName("verticalLayoutCachedModules")
        self.treeViewCachedModules = QtWidgets.QTreeView(self.tabCachedModules)
        self.treeViewCachedModules.setObjectName("treeViewCachedModules")
        self.verticalLayoutCachedModules.addWidget(self.treeViewCachedModules)
        self.tabWidget.addTab(self.tabCachedModules, "")
        self.tabGeneralResources = QtWidgets.QWidget()
        self.tabGeneralResources.setObjectName("tabGeneralResources")
        self.verticalLayoutGeneralResources = QtWidgets.QVBoxLayout(self.tabGeneralResources)
        self.verticalLayoutGeneralResources.setObjectName("verticalLayoutGeneralResources")
        self.tabWidget.addTab(self.tabGeneralResources, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.page1 = QtWidgets.QWidget()
        self.page1.setGeometry(QtCore.QRect(0, 0, 392, 385))
        self.page1.setObjectName("page1")
        self.toolBox.addItem(self.page1, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page2.setObjectName("page2")
        self.toolBox.addItem(self.page2, "")
        self.page3 = QtWidgets.QWidget()
        self.page3.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page3.setObjectName("page3")
        self.toolBox.addItem(self.page3, "")
        self.page4 = QtWidgets.QWidget()
        self.page4.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page4.setObjectName("page4")
        self.toolBox.addItem(self.page4, "")
        self.page5 = QtWidgets.QWidget()
        self.page5.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page5.setObjectName("page5")
        self.toolBox.addItem(self.page5, "")
        self.page6 = QtWidgets.QWidget()
        self.page6.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page6.setObjectName("page6")
        self.toolBox.addItem(self.page6, "")
        self.page7 = QtWidgets.QWidget()
        self.page7.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page7.setObjectName("page7")
        self.toolBox.addItem(self.page7, "")
        self.horizontalLayout.addWidget(self.toolBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionRebuildCachedModules = QtWidgets.QAction(MainWindow)
        self.actionRebuildCachedModules.setObjectName("actionRebuildCachedModules")
        self.actionFlushEventQueue = QtWidgets.QAction(MainWindow)
        self.actionFlushEventQueue.setObjectName("actionFlushEventQueue")
        self.menuTools.addAction(self.actionRebuildCachedModules)
        self.menuTools.addAction(self.actionFlushEventQueue)
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGlobalVars), _translate("MainWindow", "Global Variables"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCachedModules), _translate("MainWindow", "Cached Modules"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneralResources), _translate("MainWindow", "General Resources"))
        self.menuTools.setTitle(_translate("MainWindow", "&Tools"))
        self.actionRebuildCachedModules.setText(_translate("MainWindow", "Rebuild cached modules"))
        self.actionFlushEventQueue.setText(_translate("MainWindow", "Flush EventQueue"))

from toolset.rcc import resources_rc_pyqt5
