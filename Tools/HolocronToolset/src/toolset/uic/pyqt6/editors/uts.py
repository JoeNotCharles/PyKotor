# Form implementation generated from reading ui file '../ui/editors/uts.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 364)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.nameEdit = LocalizedStringLineEdit(parent=self.tab)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_18.addWidget(self.nameEdit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_18)
        self.label_14 = QtWidgets.QLabel(parent=self.tab)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.tagEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.tagEdit.setObjectName("tagEdit")
        self.horizontalLayout_19.addWidget(self.tagEdit)
        self.tagGenerateButton = QtWidgets.QPushButton(parent=self.tab)
        self.tagGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.tagGenerateButton.setObjectName("tagGenerateButton")
        self.horizontalLayout_19.addWidget(self.tagGenerateButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_19)
        self.label_38 = QtWidgets.QLabel(parent=self.tab)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_38)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.resrefEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.horizontalLayout_20.addWidget(self.resrefEdit)
        self.resrefGenerateButton = QtWidgets.QPushButton(parent=self.tab)
        self.resrefGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.resrefGenerateButton.setObjectName("resrefGenerateButton")
        self.horizontalLayout_20.addWidget(self.resrefGenerateButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_20)
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.volumeSlider = QtWidgets.QSlider(parent=self.tab)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.volumeSlider)
        self.verticalLayout.addLayout(self.formLayout)
        self.activeCheckbox = QtWidgets.QCheckBox(parent=self.tab)
        self.activeCheckbox.setObjectName("activeCheckbox")
        self.verticalLayout.addWidget(self.activeCheckbox)
        spacerItem = QtWidgets.QSpacerItem(20, 132, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.styleGroup = QtWidgets.QGroupBox(parent=self.tab_2)
        self.styleGroup.setObjectName("styleGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.styleGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.styleOnceRadio = QtWidgets.QRadioButton(parent=self.styleGroup)
        self.styleOnceRadio.setChecked(True)
        self.styleOnceRadio.setObjectName("styleOnceRadio")
        self.verticalLayout_2.addWidget(self.styleOnceRadio)
        self.styleRepeatRadio = QtWidgets.QRadioButton(parent=self.styleGroup)
        self.styleRepeatRadio.setObjectName("styleRepeatRadio")
        self.verticalLayout_2.addWidget(self.styleRepeatRadio)
        self.styleSeamlessRadio = QtWidgets.QRadioButton(parent=self.styleGroup)
        self.styleSeamlessRadio.setObjectName("styleSeamlessRadio")
        self.verticalLayout_2.addWidget(self.styleSeamlessRadio)
        self.horizontalLayout.addWidget(self.styleGroup)
        self.orderGroup = QtWidgets.QGroupBox(parent=self.tab_2)
        self.orderGroup.setObjectName("orderGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.orderGroup)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.orderSequentialRadio = QtWidgets.QRadioButton(parent=self.orderGroup)
        self.orderSequentialRadio.setChecked(False)
        self.orderSequentialRadio.setObjectName("orderSequentialRadio")
        self.verticalLayout_3.addWidget(self.orderSequentialRadio)
        self.orderRandomRadio = QtWidgets.QRadioButton(parent=self.orderGroup)
        self.orderRandomRadio.setChecked(True)
        self.orderRandomRadio.setObjectName("orderRandomRadio")
        self.verticalLayout_3.addWidget(self.orderRandomRadio)
        self.horizontalLayout.addWidget(self.orderGroup)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.intervalGroup = QtWidgets.QGroupBox(parent=self.tab_2)
        self.intervalGroup.setObjectName("intervalGroup")
        self.formLayout_2 = QtWidgets.QFormLayout(self.intervalGroup)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.intervalGroup)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.intervalGroup)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.intervalSpin = QtWidgets.QSpinBox(parent=self.intervalGroup)
        self.intervalSpin.setMaximum(1000000)
        self.intervalSpin.setObjectName("intervalSpin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.intervalSpin)
        self.intervalVariationSpin = QtWidgets.QSpinBox(parent=self.intervalGroup)
        self.intervalVariationSpin.setMaximum(1000000)
        self.intervalVariationSpin.setObjectName("intervalVariationSpin")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.intervalVariationSpin)
        self.verticalLayout_4.addWidget(self.intervalGroup)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.variationGroup = QtWidgets.QGroupBox(parent=self.tab_2)
        self.variationGroup.setObjectName("variationGroup")
        self.formLayout_3 = QtWidgets.QFormLayout(self.variationGroup)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.variationGroup)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.volumeVariationSlider = QtWidgets.QSlider(parent=self.variationGroup)
        self.volumeVariationSlider.setMaximum(127)
        self.volumeVariationSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volumeVariationSlider.setObjectName("volumeVariationSlider")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.volumeVariationSlider)
        self.label_5 = QtWidgets.QLabel(parent=self.variationGroup)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.pitchVariationSlider = QtWidgets.QSlider(parent=self.variationGroup)
        self.pitchVariationSlider.setMaximum(100)
        self.pitchVariationSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.pitchVariationSlider.setObjectName("pitchVariationSlider")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pitchVariationSlider)
        self.verticalLayout_5.addWidget(self.variationGroup)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.soundList = QtWidgets.QListWidget(parent=self.tab_3)
        self.soundList.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.soundList.setAlternatingRowColors(True)
        self.soundList.setObjectName("soundList")
        self.verticalLayout_9.addWidget(self.soundList)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.addSoundButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.addSoundButton.setObjectName("addSoundButton")
        self.verticalLayout_8.addWidget(self.addSoundButton)
        self.removeSoundButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.removeSoundButton.setObjectName("removeSoundButton")
        self.verticalLayout_8.addWidget(self.removeSoundButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.moveUpButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.moveUpButton.setObjectName("moveUpButton")
        self.verticalLayout_8.addWidget(self.moveUpButton)
        self.moveDownButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.moveDownButton.setObjectName("moveDownButton")
        self.verticalLayout_8.addWidget(self.moveDownButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.playSoundButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.playSoundButton.setObjectName("playSoundButton")
        self.verticalLayout_8.addWidget(self.playSoundButton)
        self.stopSoundButton = QtWidgets.QPushButton(parent=self.tab_3)
        self.stopSoundButton.setObjectName("stopSoundButton")
        self.verticalLayout_8.addWidget(self.stopSoundButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.playEverywhereRadio = QtWidgets.QRadioButton(parent=self.tab_4)
        self.playEverywhereRadio.setObjectName("playEverywhereRadio")
        self.verticalLayout_6.addWidget(self.playEverywhereRadio)
        self.playRandomRadio = QtWidgets.QRadioButton(parent=self.tab_4)
        self.playRandomRadio.setObjectName("playRandomRadio")
        self.verticalLayout_6.addWidget(self.playRandomRadio)
        self.playSpecificRadio = QtWidgets.QRadioButton(parent=self.tab_4)
        self.playSpecificRadio.setObjectName("playSpecificRadio")
        self.verticalLayout_6.addWidget(self.playSpecificRadio)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.distanceGroup = QtWidgets.QGroupBox(parent=self.tab_4)
        self.distanceGroup.setObjectName("distanceGroup")
        self.formLayout_4 = QtWidgets.QFormLayout(self.distanceGroup)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(parent=self.distanceGroup)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.cutoffSpin = QtWidgets.QDoubleSpinBox(parent=self.distanceGroup)
        self.cutoffSpin.setObjectName("cutoffSpin")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cutoffSpin)
        self.label_8 = QtWidgets.QLabel(parent=self.distanceGroup)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.maxVolumeDistanceSpin = QtWidgets.QDoubleSpinBox(parent=self.distanceGroup)
        self.maxVolumeDistanceSpin.setObjectName("maxVolumeDistanceSpin")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.maxVolumeDistanceSpin)
        self.verticalLayout_7.addWidget(self.distanceGroup)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.heightGroup = QtWidgets.QGroupBox(parent=self.tab_4)
        self.heightGroup.setObjectName("heightGroup")
        self.formLayout_5 = QtWidgets.QFormLayout(self.heightGroup)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_9 = QtWidgets.QLabel(parent=self.heightGroup)
        self.label_9.setObjectName("label_9")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.heightSpin = QtWidgets.QDoubleSpinBox(parent=self.heightGroup)
        self.heightSpin.setObjectName("heightSpin")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.heightSpin)
        self.horizontalLayout_2.addWidget(self.heightGroup)
        self.rangeGroup = QtWidgets.QGroupBox(parent=self.tab_4)
        self.rangeGroup.setObjectName("rangeGroup")
        self.formLayout_6 = QtWidgets.QFormLayout(self.rangeGroup)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.rangeGroup)
        self.label_10.setObjectName("label_10")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.northRandomSpin = QtWidgets.QDoubleSpinBox(parent=self.rangeGroup)
        self.northRandomSpin.setObjectName("northRandomSpin")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.northRandomSpin)
        self.label_11 = QtWidgets.QLabel(parent=self.rangeGroup)
        self.label_11.setObjectName("label_11")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.eastRandomSpin = QtWidgets.QDoubleSpinBox(parent=self.rangeGroup)
        self.eastRandomSpin.setObjectName("eastRandomSpin")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.eastRandomSpin)
        self.horizontalLayout_2.addWidget(self.rangeGroup)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.commentsEdit = QtWidgets.QPlainTextEdit(parent=self.tab_5)
        self.commentsEdit.setObjectName("commentsEdit")
        self.gridLayout_2.addWidget(self.commentsEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRevert = QtGui.QAction(parent=MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionRevert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sound Editor"))
        self.label_6.setText(_translate("MainWindow", "Name:"))
        self.label_14.setText(_translate("MainWindow", "Tag:"))
        self.tagGenerateButton.setText(_translate("MainWindow", "-"))
        self.label_38.setText(_translate("MainWindow", "ResRef:"))
        self.resrefGenerateButton.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "Volume:"))
        self.activeCheckbox.setText(_translate("MainWindow", "Active"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.styleGroup.setTitle(_translate("MainWindow", "Play Style"))
        self.styleOnceRadio.setText(_translate("MainWindow", "Once"))
        self.styleRepeatRadio.setText(_translate("MainWindow", "Repeating"))
        self.styleSeamlessRadio.setText(_translate("MainWindow", "Seamless Looping"))
        self.orderGroup.setTitle(_translate("MainWindow", "Play Order"))
        self.orderSequentialRadio.setText(_translate("MainWindow", "Sequential"))
        self.orderRandomRadio.setText(_translate("MainWindow", "Random"))
        self.intervalGroup.setTitle(_translate("MainWindow", "Interval"))
        self.label_2.setText(_translate("MainWindow", "Interval between sounds (s):"))
        self.label_3.setText(_translate("MainWindow", "Interval variation (s):"))
        self.variationGroup.setTitle(_translate("MainWindow", "Variation"))
        self.label_4.setText(_translate("MainWindow", "Volume Variation:"))
        self.label_5.setText(_translate("MainWindow", "Pitch Variation:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Advanced"))
        self.addSoundButton.setText(_translate("MainWindow", "Add"))
        self.removeSoundButton.setText(_translate("MainWindow", "Remove"))
        self.moveUpButton.setText(_translate("MainWindow", "Move Up"))
        self.moveDownButton.setText(_translate("MainWindow", "Move Down"))
        self.playSoundButton.setText(_translate("MainWindow", "Play"))
        self.stopSoundButton.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Sounds"))
        self.playEverywhereRadio.setText(_translate("MainWindow", "Plays everywhere in area"))
        self.playRandomRadio.setText(_translate("MainWindow", "Plays from a random position each time"))
        self.playSpecificRadio.setText(_translate("MainWindow", "Plays from a specific position"))
        self.distanceGroup.setTitle(_translate("MainWindow", "Volume Distances"))
        self.label_7.setText(_translate("MainWindow", "Cutoff Distance (m):"))
        self.label_8.setText(_translate("MainWindow", "Max Volume Distance (m):"))
        self.heightGroup.setTitle(_translate("MainWindow", "Height"))
        self.label_9.setText(_translate("MainWindow", "Height (m):"))
        self.rangeGroup.setTitle(_translate("MainWindow", "Random Range:"))
        self.label_10.setText(_translate("MainWindow", "North/South (m):"))
        self.label_11.setText(_translate("MainWindow", "East/West (m):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Positioning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Comments"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from toolset.gui.widgets.edit.locstring import LocalizedStringLineEdit

from toolset.rcc import resources_rc_pyqt6
