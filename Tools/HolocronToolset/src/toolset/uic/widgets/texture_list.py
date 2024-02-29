# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src\ui\widgets\texture_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(327, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sectionCombo = QtWidgets.QComboBox(Form)
        self.sectionCombo.setObjectName("sectionCombo")
        self.verticalLayout.addWidget(self.sectionCombo)
        self.textureLine = QtWidgets.QFrame(Form)
        self.textureLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.textureLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textureLine.setObjectName("textureLine")
        self.verticalLayout.addWidget(self.textureLine)
        self.searchEdit = QtWidgets.QLineEdit(Form)
        self.searchEdit.setObjectName("searchEdit")
        self.verticalLayout.addWidget(self.searchEdit)
        self.resourceList = QtWidgets.QListView(Form)
        self.resourceList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resourceList.setProperty("showDropIndicator", False)
        self.resourceList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.resourceList.setIconSize(QtCore.QSize(64, 64))
        self.resourceList.setProperty("isWrapping", True)
        self.resourceList.setResizeMode(QtWidgets.QListView.Adjust)
        self.resourceList.setLayoutMode(QtWidgets.QListView.Batched)
        self.resourceList.setGridSize(QtCore.QSize(92, 92))
        self.resourceList.setViewMode(QtWidgets.QListView.IconMode)
        self.resourceList.setUniformItemSizes(True)
        self.resourceList.setObjectName("resourceList")
        self.verticalLayout.addWidget(self.resourceList)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchEdit.setPlaceholderText(_translate("Form", "search..."))
