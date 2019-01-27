# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.buttons_matrix = []
        for j in range(3):
            self.buttons_matrix.append([])
            for i in range(3):
                self.buttons_matrix[j].append(QtWidgets.QPushButton(Dialog))
                self.buttons_matrix[j][i].setGeometry(QtCore.QRect(80 + 35 * i, 120 + 35 * j, 30, 30))
                self.buttons_matrix[j][i].setObjectName("pushButton")

        self.retranslateUi(Dialog)

        #             |-----<event>------->|
        # self.lineEdit.textChanged['QString'].connect(self.lineEdit_2.setText)
        # self.lineEdit.textChanged['QString'].connect(self.double_it)

        for j in range(3):
            for i in range(3):
                self.buttons_matrix[j][i].clicked.connect(self.calculator_set_text(i, j))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculator_set_text(self, i, j):
        def inner_set_text():
            previous_value = self.lineEdit.text()
            augmented_value = self.buttons_matrix[j][i].text()
            value = previous_value + augmented_value
            self.lineEdit.setText(value)
        return inner_set_text


    def double_it(self):
        self.lineEdit_2.setText(self.lineEdit.text() * 2)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "My Custom Title"))
        self.pushButton.setText(_translate("Dialog", "click me"))
        # self.lineEdit.setText(_translate("Dialog", "some ranfom val"))
        for j in range(3):
            for i in range(3):
                self.buttons_matrix[j][i].setText(str(3*i+j + 1))
