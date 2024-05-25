# Form implementation generated from reading ui file '..\ui\widgets\texture_list.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(327, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sectionCombo = QtWidgets.QComboBox(parent=Form)
        self.sectionCombo.setObjectName("sectionCombo")
        self.verticalLayout.addWidget(self.sectionCombo)
        self.textureLine = QtWidgets.QFrame(parent=Form)
        self.textureLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.textureLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.textureLine.setObjectName("textureLine")
        self.verticalLayout.addWidget(self.textureLine)
        self.searchEdit = QtWidgets.QLineEdit(parent=Form)
        self.searchEdit.setObjectName("searchEdit")
        self.verticalLayout.addWidget(self.searchEdit)
        self.resourceList = QtWidgets.QListView(parent=Form)
        self.resourceList.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.resourceList.setProperty("showDropIndicator", False)
        self.resourceList.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.resourceList.setIconSize(QtCore.QSize(64, 64))
        self.resourceList.setProperty("isWrapping", True)
        self.resourceList.setResizeMode(QtWidgets.QListView.ResizeMode.Adjust)
        self.resourceList.setLayoutMode(QtWidgets.QListView.LayoutMode.Batched)
        self.resourceList.setGridSize(QtCore.QSize(92, 92))
        self.resourceList.setViewMode(QtWidgets.QListView.ViewMode.IconMode)
        self.resourceList.setUniformItemSizes(True)
        self.resourceList.setObjectName("resourceList")
        self.verticalLayout.addWidget(self.resourceList)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchEdit.setPlaceholderText(_translate("Form", "search..."))
