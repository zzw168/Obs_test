# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Obs_test_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_picture = QtWidgets.QLabel(self.frame)
        self.label_picture.setMinimumSize(QtCore.QSize(800, 600))
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        self.gridLayout_2.addWidget(self.label_picture, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_GetPicture_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_GetPicture_4.setObjectName("pushButton_GetPicture_4")
        self.gridLayout_4.addWidget(self.pushButton_GetPicture_4, 4, 2, 1, 1)
        self.pushButton_GetPicture_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_GetPicture_3.setObjectName("pushButton_GetPicture_3")
        self.gridLayout_4.addWidget(self.pushButton_GetPicture_3, 2, 2, 1, 1)
        self.pushButton_GetPicture = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_GetPicture.setObjectName("pushButton_GetPicture")
        self.gridLayout_4.addWidget(self.pushButton_GetPicture, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 4, 0, 1, 1)
        self.pushButton_ObsConnect = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_ObsConnect.setObjectName("pushButton_ObsConnect")
        self.gridLayout_4.addWidget(self.pushButton_ObsConnect, 0, 0, 1, 3)
        self.pushButton_GetPicture_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_GetPicture_2.setObjectName("pushButton_GetPicture_2")
        self.gridLayout_4.addWidget(self.pushButton_GetPicture_2, 1, 0, 1, 3)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 2, 0, 1, 1)
        self.pushButton_GetPicture_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_GetPicture_5.setObjectName("pushButton_GetPicture_5")
        self.gridLayout_4.addWidget(self.pushButton_GetPicture_5, 4, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_GetPicture_4.setText(_translate("MainWindow", "来源关闭"))
        self.pushButton_GetPicture_3.setText(_translate("MainWindow", "场景关闭"))
        self.pushButton_GetPicture.setText(_translate("MainWindow", "场景开启"))
        self.pushButton_ObsConnect.setText(_translate("MainWindow", "链接OBS"))
        self.pushButton_GetPicture_2.setText(_translate("MainWindow", "获取图片"))
        self.pushButton_GetPicture_5.setText(_translate("MainWindow", "来源开启"))
