# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/dialogs/save_in_rim.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(271, 77)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.overrideSaveButton = QtWidgets.QPushButton(Dialog)
        self.overrideSaveButton.setObjectName("overrideSaveButton")
        self.horizontalLayout.addWidget(self.overrideSaveButton)
        self.modSaveButton = QtWidgets.QPushButton(Dialog)
        self.modSaveButton.setObjectName("modSaveButton")
        self.horizontalLayout.addWidget(self.modSaveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cannot save to RIM"))
        self.label.setText(_translate("Dialog", "Saving to RIM files is disabled. You can choose\n"
"to save it to the Override or .MOD file instead."))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.overrideSaveButton.setText(_translate("Dialog", "Save to Override"))
        self.modSaveButton.setText(_translate("Dialog", "Save to .MOD"))

from toolset.rcc import resources_rc_pyqt5
