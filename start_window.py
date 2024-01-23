# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(334, 242)
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(244, 170, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 121, 121))
        self.label.setObjectName("label")
        self.create_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.create_pushButton.setGeometry(QtCore.QRect(189, 210, 111, 21))
        self.create_pushButton.setObjectName("create_pushButton")
        self.open_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.open_pushButton.setGeometry(QtCore.QRect(30, 210, 111, 21))
        self.open_pushButton.setObjectName("open_pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "ACR v0.0.1"))
        self.label_3.setText(_translate("StartWindow", "29.10.2019"))
        self.label.setText(_translate("StartWindow", "TextLabel"))
        self.create_pushButton.setText(_translate("StartWindow", "Create project"))
        self.open_pushButton.setText(_translate("StartWindow", "Open project"))
        self.label_2.setText(_translate("StartWindow", "AutoClicker with Recognition"))
