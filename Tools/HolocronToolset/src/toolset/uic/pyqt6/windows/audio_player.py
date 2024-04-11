# Form implementation generated from reading ui file '..\ui\windows\audio_player.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 94)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currentTimeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.currentTimeLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.currentTimeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.horizontalLayout.addWidget(self.currentTimeLabel)
        self.timeSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.timeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout.addWidget(self.timeSlider)
        self.totalTimeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.totalTimeLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.horizontalLayout.addWidget(self.totalTimeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_2.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_2.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Player"))
        self.currentTimeLabel.setText(_translate("MainWindow", "00:00:00"))
        self.totalTimeLabel.setText(_translate("MainWindow", "00:00:00"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
