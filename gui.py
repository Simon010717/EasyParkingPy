# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Simon/Desktop/EasyParkingPy/login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 460)
        MainWindow.setStyleSheet("*{\n"
"font-family: segoe ui;\n"
"}\n"
"QLabel{\n"
"font-size: 15px;\n"
"color: white;\n"
"}\n"
"QFrame{\n"
"background: #444;\n"
"}\n"
"QPushButton{\n"
"color: #444;\n"
"border-radius: 15px;\n"
"background:white;\n"
"font-size: 30px;\n"
"}\n"
"QToolButton{\n"
"background: transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background: #444;\n"
"color: white;\n"
"border-color: white;\n"
"border-radius: 15px;\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"color: #717072;\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-color: #717072;\n"
"font-size: 30px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 531, 461))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.usernameLine = QtWidgets.QLineEdit(self.frame_2)
        self.usernameLine.setGeometry(QtCore.QRect(40, 310, 461, 61))
        self.usernameLine.setText("")
        self.usernameLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usernameLine.setCursorPosition(0)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(self.frame_2)
        self.passwordLine.setGeometry(QtCore.QRect(40, 220, 461, 61))
        self.passwordLine.setText("")
        self.passwordLine.setCursorPosition(0)
        self.passwordLine.setObjectName("passwordLine")
        self.registerButton = QtWidgets.QPushButton(self.frame_2)
        self.registerButton.setGeometry(QtCore.QRect(290, 380, 181, 51))
        self.registerButton.setObjectName("registerButton")
        self.loginButton = QtWidgets.QPushButton(self.frame_2)
        self.loginButton.setGeometry(QtCore.QRect(50, 380, 181, 51))
        self.loginButton.setObjectName("loginButton")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 0, 381, 171))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("easy_blanco.svg"))
        self.label.setObjectName("label")
        self.usernameLabel = QtWidgets.QLabel(self.frame_2)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 201, 191, 20))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frame_2)
        self.passwordLabel.setGeometry(QtCore.QRect(40, 291, 191, 20))
        self.passwordLabel.setObjectName("passwordLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.usernameLabel.setText(_translate("MainWindow", "Usuario"))
        self.passwordLabel.setText(_translate("MainWindow", "Contraseña"))
import logo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
