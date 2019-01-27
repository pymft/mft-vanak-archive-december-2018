# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        # self.button_list = []
        # for i in range(5):
        #     for j in range(5):
        #         tmp = QtWidgets.QPushButton(Dialog)
        #         self.button_list.append(tmp)
        #         self.button_list[-1].setGeometry(QtCore.QRect(60 + 40 * i , 10 + 30 * j, 23, 23))
        #         self.button_list[-1].setText(str(i*j))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("click me !")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 170, 200, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        # self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.echo)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def echo(self):
        print(self.lineEdit.text())
        self.lineEdit.setText("hello")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

