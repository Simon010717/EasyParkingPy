# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Simon/Desktop/EasyParkingPy/ui_py/login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 481)
        MainWindow.setStyleSheet("*{\n"
"font-family: segoe ui;\n"
"}\n"
"QLabel{\n"
"font-size: 15px;\n"
"color: white;\n"
"}\n"
"QFrame{\n"
"background: #2B3446;\n"
"}\n"
"QPushButton{\n"
"color: #2B3446;\n"
"border-radius: 15px;\n"
"background:white;\n"
"font-size: 30px;\n"
"}\n"
"QToolButton{\n"
"background: transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background: #2B3446;\n"
"color: white;\n"
"border-color: white;\n"
"border-radius: 15px;\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"color: white;\n"
"border: none;\n"
"border-bottom: 1px solid;\n"
"border-color: white;\n"
"font-size: 30px;\n"
"}\n"
"#ErrorLabel{\n"
"font-size: 20px;\n"
"background: transparent;\n"
"color: red\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.usernameLine = QtWidgets.QLineEdit(self.frame)
        self.usernameLine.setGeometry(QtCore.QRect(30, 189, 461, 61))
        self.usernameLine.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.usernameLine.setText("")
        self.usernameLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.usernameLine.setCursorPosition(0)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(self.frame)
        self.passwordLine.setGeometry(QtCore.QRect(30, 279, 461, 61))
        self.passwordLine.setText("")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setCursorPosition(0)
        self.passwordLine.setObjectName("passwordLine")
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setGeometry(QtCore.QRect(30, 170, 191, 20))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 260, 191, 20))
        self.passwordLabel.setObjectName("passwordLabel")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 381, 171))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/logo/easy_blanco.svg"))
        self.label_3.setObjectName("label_3")
        self.registerButton = QtWidgets.QPushButton(self.frame)
        self.registerButton.setGeometry(QtCore.QRect(270, 400, 181, 51))
        self.registerButton.setObjectName("registerButton")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(70, 400, 181, 51))
        self.loginButton.setObjectName("loginButton")
        self.ErrorLabel = QtWidgets.QLabel(self.frame)
        self.ErrorLabel.setGeometry(QtCore.QRect(30, 350, 461, 31))
        self.ErrorLabel.setText("")
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usernameLabel.setText(_translate("MainWindow", "Usuario"))
        self.passwordLabel.setText(_translate("MainWindow", "Contraseña"))
        self.registerButton.setText(_translate("MainWindow", "Registrar"))
        self.loginButton.setText(_translate("MainWindow", "Ingresar"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
