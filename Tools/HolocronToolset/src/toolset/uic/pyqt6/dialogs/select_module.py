# Form implementation generated from reading ui file '..\ui\dialogs\select_module.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 373)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.filterEdit.setObjectName("filterEdit")
        self.verticalLayout.addWidget(self.filterEdit)
        self.moduleList = QtWidgets.QListWidget(parent=Dialog)
        self.moduleList.setObjectName("moduleList")
        self.verticalLayout.addWidget(self.moduleList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(parent=Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.browseButton = QtWidgets.QPushButton(parent=Dialog)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.openButton = QtWidgets.QPushButton(parent=Dialog)
        self.openButton.setEnabled(False)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open Module"))
        self.filterEdit.setPlaceholderText(_translate("Dialog", "filter..."))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.browseButton.setText(_translate("Dialog", "Browse"))
        self.openButton.setText(_translate("Dialog", "Open"))
