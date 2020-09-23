# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from db import insert,viewfolder,delete,view

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 532)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(46, 52, 54);\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0 ,0 ,0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 0, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Vemana2000")
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label1.setObjectName("label1")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(20, 40, 81, 20))
        self.l1.setStyleSheet("color: rgb(255, 255, 255);")
        self.l1.setObjectName("l1")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(110, 40, 271, 20))
        self.t1.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);")
        self.t1.setText("")
        self.t1.setObjectName("t1")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(20, 70, 81, 17))
        self.l2.setStyleSheet("color: rgb(255, 255, 255);")
        self.l2.setObjectName("l2")
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(110, 70, 271, 21))
        self.t2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t2.setObjectName("t2")
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(20, 100, 81, 17))
        self.l3.setStyleSheet("color: rgb(255, 255, 255);")
        self.l3.setObjectName("l3")
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setGeometry(QtCore.QRect(110, 100, 271, 20))
        self.t3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t3.setObjectName("t3")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(80, 140, 89, 25))
        self.b1.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"background-color: rgb(196, 160, 0);")
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(lambda : insert(self.t1.text(),self.t2.text(),self.t3.text()))
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Vemana2000")
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label2.setObjectName("label2")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(80, 210, 89, 25))
        self.b2.setStyleSheet("background-color: rgb(206, 92, 0);\n"
"background-color: rgb(245, 121, 0);\n"
"background-color: rgb(245, 121, 0);\n"
"background-color: rgb(196, 160, 0);\n"
"background-color: rgb(245, 121, 0);")
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(lambda : viewfolder())
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Vemana2000")
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label3.setObjectName("label3")
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(20, 290, 81, 17))
        self.l4.setStyleSheet("color: rgb(255, 255, 255);")
        self.l4.setObjectName("l4")
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setGeometry(QtCore.QRect(110, 290, 271, 21))
        self.t4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t4.setObjectName("t4")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(80, 340, 89, 25))
        self.b3.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(lambda  : delete(self.t4.text()))
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(20, 370, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Vemana2000")
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label4.setObjectName("label4")
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(20, 410, 81, 17))
        self.l5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.l5.setObjectName("l5")
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        self.t5.setGeometry(QtCore.QRect(110, 410, 271, 21))
        self.t5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.t5.setObjectName("t5")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(80, 460, 89, 25))
        self.b4.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(lambda  :  view(self.t5.text()))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 22))
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
        self.label1.setText(_translate("MainWindow", "Insert"))
        self.l1.setText(_translate("MainWindow", "Website    :"))
        self.l2.setText(_translate("MainWindow", "UserId       :"))
        self.l3.setText(_translate("MainWindow", "Password : "))
        self.b1.setText(_translate("MainWindow", "Insert"))
        self.label2.setText(_translate("MainWindow", "View Folders"))
        self.b2.setText(_translate("MainWindow", "View "))
        self.label3.setText(_translate("MainWindow", "Delete Folder"))
        self.l4.setText(_translate("MainWindow", "Website    :"))
        self.b3.setText(_translate("MainWindow", "Delete"))
        self.label4.setText(_translate("MainWindow", "View  Username  and  Password"))
        self.l5.setText(_translate("MainWindow", "Website    :   "))
        self.b4.setText(_translate("MainWindow", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
