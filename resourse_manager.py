# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resource_manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 387)
        Form.setMinimumSize(QtCore.QSize(362, 387))
        Form.setMaximumSize(QtCore.QSize(362, 387))
        Form.setAutoFillBackground(True)
        self.images_listWidget = QtWidgets.QListWidget(Form)
        self.images_listWidget.setGeometry(QtCore.QRect(10, 10, 341, 281))
        self.images_listWidget.setObjectName("images_listWidget")
        self.path_Edit = QtWidgets.QLineEdit(Form)
        self.path_Edit.setGeometry(QtCore.QRect(10, 330, 181, 21))
        self.path_Edit.setObjectName("path_Edit")
        self.changepath_Button = QtWidgets.QPushButton(Form)
        self.changepath_Button.setGeometry(QtCore.QRect(180, 330, 80, 21))
        self.changepath_Button.setObjectName("changepath_Button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 300, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name_lineEdit = QtWidgets.QLineEdit(Form)
        self.name_lineEdit.setGeometry(QtCore.QRect(50, 300, 211, 21))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.add_Button = QtWidgets.QPushButton(Form)
        self.add_Button.setGeometry(QtCore.QRect(10, 360, 251, 21))
        self.add_Button.setObjectName("add_Button")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(270, 300, 81, 81))
        self.image_label.setObjectName("image_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Resource manager"))
        self.changepath_Button.setText(_translate("Form", "Change"))
        self.label.setText(_translate("Form", "Name"))
        self.add_Button.setText(_translate("Form", "Add"))
        self.image_label.setText(_translate("Form", "Image"))
