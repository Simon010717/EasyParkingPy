# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import EasyParking

class Ui_MainWindow(object):

    def __init__(self,mainWin,ep):
        self.mainWindow = mainWin
        self.ep = ep

    def registroLogin(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep)
        self.ui.setupUiRegistro(self.mainWindow)
        self.mainWindow.show()

    def cancelarRegistro(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep)
        self.ui.setupUiLogin(self.mainWindow)
        self.mainWindow.show()
    
    def okRegistro(self):
        tCedula= self.cedula.text()
        tNickname= self.nickname.text()
        tPassword = self.password.text()
        tNombre =  self.nombre.text()
        tApellido= self.apellido.text()
        tEdad= self.edad.text()
        tPlaca= self.placa.text()
        tEmail= self.email.text()
        tDireccion= self.direccion.text()
        tTelefono= self.telefono.text()

        info= [tCedula,tNickname,tPassword,tNombre,tApellido,tEdad,tPlaca,tEmail,tDireccion,tTelefono]

        print(self.ep.addUsuarioArr(info,False))

    def loginLogin(self):
        tNickname = self.usernameLine.text()
        tPassword = self.passwordLine.text()

        if self.ep.checkLogin(tNickname,tPassword): print("Done")
        else: print("Not done")

    

    def setupUiRegistro(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 647)
        MainWindow.setStyleSheet("*{\n"
"font-family: segoe ui;\n"
"font-size: 30px;\n"
"border-color: transparent;\n"
"}\n"
"QFrame{\n"
"background: #444;\n"
"}\n"
"QPushButton{\n"
"color: #444;\n"
"border-radius: 15px;\n"
"background:white;\n"
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
"}\n"
"QLabel{\n"
"font-size: 12px;\n"
"background: transparent;\n"
"color: white;\n"
"}")
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cancelar = QtWidgets.QPushButton(self.frame)
        self.cancelar.setGeometry(QtCore.QRect(160, 590, 151, 41))
        self.cancelar.setObjectName("cancelar")
        self.cancelar.clicked.connect(self.cancelarRegistro)
        self.archivar = QtWidgets.QPushButton(self.frame)
        self.archivar.setGeometry(QtCore.QRect(410, 590, 151, 41))
        self.archivar.setObjectName("archivar")
        self.archivar.clicked.connect(self.okRegistro)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 521, 516))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cedula = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.cedula.setStyleSheet("")
        self.cedula.setObjectName("cedula")
        self.verticalLayout.addWidget(self.cedula)
        self.nickname = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.nickname.setStyleSheet("")
        self.nickname.setObjectName("nickname")
        self.verticalLayout.addWidget(self.nickname)
        self.password = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.password.setStyleSheet("")
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.nombre = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.nombre.setStyleSheet("")
        self.nombre.setObjectName("nombre")
        self.verticalLayout.addWidget(self.nombre)
        self.apellido = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.apellido.setStyleSheet("")
        self.apellido.setObjectName("apellido")
        self.verticalLayout.addWidget(self.apellido)
        self.edad = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edad.setStyleSheet("")
        self.edad.setObjectName("edad")
        self.verticalLayout.addWidget(self.edad)
        self.placa = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.placa.setObjectName("placa")
        self.verticalLayout.addWidget(self.placa)
        self.email = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.email.setStyleSheet("")
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.direccion = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.direccion.setStyleSheet("")
        self.direccion.setObjectName("direccion")
        self.verticalLayout.addWidget(self.direccion)
        self.telefono = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.telefono.setStyleSheet("")
        self.telefono.setObjectName("telefono")
        self.verticalLayout.addWidget(self.telefono)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUiRegistro(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiRegistro(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Registro", "Registro"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.archivar.setText(_translate("MainWindow", "Registar"))
        self.label.setText(_translate("MainWindow", "Cedula:"))
        self.label_2.setText(_translate("MainWindow", "Nombre de usuario:"))
        self.label_3.setText(_translate("MainWindow", "Contraseña:"))
        self.label_4.setText(_translate("MainWindow", "Nombre:"))
        self.label_5.setText(_translate("MainWindow", "Apellido:"))
        self.label_6.setText(_translate("MainWindow", "Edad:"))
        self.label_10.setText(_translate("MainWindow", "Placa:"))
        self.label_7.setText(_translate("MainWindow", "Email:"))
        self.label_8.setText(_translate("MainWindow", "Dirección:"))
        self.label_9.setText(_translate("MainWindow", "Teléfono:"))


    def setupUiLogin(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 456)
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
        self.usernameLine.setGeometry(QtCore.QRect(40, 220, 461, 61))
        self.usernameLine.setText("")
        self.usernameLine.setCursorPosition(0)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(self.frame_2)
        self.passwordLine.setGeometry(QtCore.QRect(40, 310, 461, 61))
        self.passwordLine.setText("")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
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
        self.label.setPixmap(QtGui.QPixmap(":/easy_blanco.svg"))
        self.label.setObjectName("label")
        self.usernameLabel = QtWidgets.QLabel(self.frame_2)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 201, 191, 20))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.frame_2)
        self.passwordLabel.setGeometry(QtCore.QRect(40, 291, 191, 20))
        self.passwordLabel.setObjectName("passwordLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.registerButton.clicked.connect(self.registroLogin)
        self.loginButton.clicked.connect(self.loginLogin)

        self.retranslateUiLogin(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiLogin(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Login", "Login"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.usernameLabel.setText(_translate("MainWindow", "Usuario"))
        self.passwordLabel.setText(_translate("MainWindow", "Contraseña"))



if __name__ == "__main__":
    import sys
    ep = EasyParking.EasyParking()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow,ep)
    ui.setupUiLogin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
