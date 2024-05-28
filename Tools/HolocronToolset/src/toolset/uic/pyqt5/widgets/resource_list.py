# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/widgets/resource_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(333, 364)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sectionCombo = QtWidgets.QComboBox(Form)
        self.sectionCombo.setMaxVisibleItems(18)
        self.sectionCombo.setObjectName("sectionCombo")
        self.horizontalLayout_2.addWidget(self.sectionCombo)
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setMinimumSize(QtCore.QSize(70, 0))
        self.refreshButton.setMaximumSize(QtCore.QSize(16777215, 70))
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_2.addWidget(self.refreshButton)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_4.addWidget(self.searchEdit)
        self.reloadButton = QtWidgets.QPushButton(Form)
        self.reloadButton.setEnabled(True)
        self.reloadButton.setMinimumSize(QtCore.QSize(70, 0))
        self.reloadButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.reloadButton.setObjectName("reloadButton")
        self.horizontalLayout_4.addWidget(self.reloadButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.resourceTree = QtWidgets.QTreeView(Form)
        self.resourceTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.resourceTree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resourceTree.setAlternatingRowColors(True)
        self.resourceTree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.resourceTree.setSortingEnabled(True)
        self.resourceTree.setAllColumnsShowFocus(True)
        self.resourceTree.setObjectName("resourceTree")
        self.resourceTree.header().setSortIndicatorShown(True)
        self.resourceTree.header().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.resourceTree)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.refreshButton.setToolTip(_translate("Form", "Refresh the list of modules."))
        self.refreshButton.setText(_translate("Form", "Refresh"))
        self.searchEdit.setPlaceholderText(_translate("Form", "search..."))
        self.reloadButton.setToolTip(_translate("Form", "Reload the active module."))
        self.reloadButton.setText(_translate("Form", "Reload"))

from toolset.rcc import resources_rc_pyqt5
