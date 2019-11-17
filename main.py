# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QWidget, QDesktopWidget, QLabel,QPushButton
import EasyParking, random
from datetime import date, timedelta
import time


class Ui_MainWindow(object):

    def __init__(self,mainWin,ep,indexUs,indexEmp):
        self.mainWindow = mainWin
        self.ep = ep
        self.indexUsuario = indexUs
        self.indexEmpleado = indexEmp
        self.mainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint,False)

    
    def registroLogin(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
        self.ui.setupUiRegistro(self.mainWindow)
        self.mainWindow.show()

    def cancelarRegistro(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
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

        if "" in info:
            self.ErrorLabel.setText("*Todos los campos marcados son obligatorios")
            return

        r = self.ep.addUsuarioArr(info,False)

        if r == 3:
            self.mainWindow.hide()
            self.mainWindow=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
            self.ui.setupUiLogin(self.mainWindow)
            self.mainWindow.show()
        elif r == 2:
            self.ErrorLabel.setText("*Placa incorrecta. Debe ingresar una nueva placa")
        elif r == 1:
            self.ErrorLabel.setText("*El nombre de usuario no está disponible, ingrese uno nuevo")
        elif r == 0:
            self.ErrorLabel.setText("*Ya existe un usuario con este número de documento")

    def loginLogin(self):
        tNickname = self.usernameLine.text()
        tPassword = self.passwordLine.text()
        if not self.adminButton.isChecked():
            self.indexUsuario = self.ep.checkLogin(tNickname,tPassword)
            if self.indexUsuario > -1:
                self.mainWindow.hide()
                self.mainWindow=QtWidgets.QMainWindow()
                self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
                self.ui.setupUiOpciones(self.mainWindow)
                self.mainWindow.show()
            elif self.indexUsuario == -1:
                self.ErrorLabel.setText("Contraseña incorrecta")
            elif self.indexUsuario == -2:
                self.ErrorLabel.setText("Usuario no encontrado")
        else:
            self.indexEmpleado = self.ep.checkLoginEmpleado(tNickname,tPassword)
            if self.indexEmpleado > -1:
                self.mainWindow.hide()
                self.mainWindow=QtWidgets.QMainWindow()
                self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
                self.ui.setupUiEditarParq(self.mainWindow)
                self.mainWindow.show()
            elif self.indexEmpleado == -1:
                self.ErrorLabel.setText("Contraseña de administrador incorrecta")
            elif self.indexEmpleado == -2:
                self.ErrorLabel.setText("Administrador no encontrado")

    def parquearOpciones(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
        self.ui.setupUiParqueaderos(self.mainWindow)
        self.mainWindow.show()

    def regresarOpciones(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
        self.ui.setupUiLogin(self.mainWindow)
        self.mainWindow.show()

    def facturaOpciones(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
        self.ui.setupUiFactura(self.mainWindow)
        self.mainWindow.show()

    def regresarParqueaderos(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
        self.ui.setupUiOpciones(self.mainWindow)
        self.mainWindow.show()

    def regresarFactura(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
        self.ui.setupUiOpciones(self.mainWindow)
        self.mainWindow.show()

    def regresarEditarParq(self):
        self.mainWindow.hide()
        self.mainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
        self.ui.setupUiLogin(self.mainWindow)
        self.mainWindow.show()

    def autoParqueo(self,p,inP):
        e = p.espaciosTree.siguienteLibre(p.ocupados+1,p.totales)
        if e > -1:
            p.parqueo(self.ep.usuarios[self.indexUsuario],inP,e,False)
            
            self.mainWindow.hide()
            self.mainWindow=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow(self.mainWindow,self.ep,self.indexUsuario,self.indexEmpleado)
            self.ui.setupUiOpciones(self.mainWindow)
            self.mainWindow.show()
        
        self.ErrorLabel.setText("Lo sentimos, este parqueadero no tiene cupos disponibles")

    def vaciarParq(self,p,inP):
        for u in self.ep.usuarios:
            if u.carro.enParqueo and u.carro.esp[0] == p.cod:
                u.carro.enParqueo = False
                u.carro.esp = None
        p.vaciar(inP)
        self.ocupadosLab.setText("Ocupados: 0")

    def setupUiLogin(self, MainWindow):
        self.indexEmpleado = -1
        self.indexUsuario = -1

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
        self.label_3.setPixmap(QtGui.QPixmap("logo/easy_blanco.svg"))
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
        self.adminButton = QtWidgets.QRadioButton(self.frame)
        self.adminButton.setGeometry(QtCore.QRect(470, 170, 16, 20))
        self.adminButton.setText("")
        self.adminButton.setObjectName("adminButton")
        MainWindow.setCentralWidget(self.centralwidget)

        #botones
        self.registerButton.clicked.connect(self.registroLogin)
        self.loginButton.clicked.connect(self.loginLogin)

        self.retranslateUiLogin(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiLogin(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Easy Parking", "Easy Parking"))
        self.usernameLabel.setText(_translate("MainWindow", "Usuario"))
        self.passwordLabel.setText(_translate("MainWindow", "Contraseña"))
        self.registerButton.setText(_translate("MainWindow", "Registrar"))
        self.loginButton.setText(_translate("MainWindow", "Ingresar"))

    def setupUiRegistro(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 758)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("*{\n"
        "font-family: segoe ui;\n"
        "}\n"
        "QFrame{\n"
        "background: #2B3446;\n"
        "}\n"
        "QPushButton{\n"
        "color: #2B3446;\n"
        "border-radius: 15px;\n"
        "background:white;\n"
        "font-size: 30px\n"
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
        "font-size: 30px\n"
        "}\n"
        "QLineEdit{\n"
        "background: #2B3446;\n"
        "color: white;\n"
        "border: none;\n"
        "border-bottom: 1px solid;\n"
        "border-color: white;\n"
        "font-size: 23px\n"
        "}\n"
        "QLabel{\n"
        "font-size: 20px;\n"
        "background: transparent;\n"
        "color: white;\n"
        "background: #2B3446;\n"
        "}\n"
        "#ErrorLabel{\n"
        "color: red\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 591, 761))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cancelar = QtWidgets.QPushButton(self.frame)
        self.cancelar.setGeometry(QtCore.QRect(220, 680, 151, 41))
        self.cancelar.setObjectName("cancelar")
        self.archivar = QtWidgets.QPushButton(self.frame)
        self.archivar.setGeometry(QtCore.QRect(400, 680, 151, 41))
        self.archivar.setObjectName("archivar")
        self.ErrorLabel = QtWidgets.QLabel(self.frame)
        self.ErrorLabel.setGeometry(QtCore.QRect(30, 630, 521, 31))
        self.ErrorLabel.setText("")
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(500, 10, 71, 91))
        self.label_11.setStyleSheet("")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("logo/ep_blanco.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 521, 516))
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
        self.password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
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
        MainWindow.setCentralWidget(self.centralwidget)

        #botones
        self.cancelar.clicked.connect(self.cancelarRegistro)
        self.archivar.clicked.connect(self.okRegistro)

        self.retranslateUiRegistro(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiRegistro(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Easy Parking", "Easy Parking"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.archivar.setText(_translate("MainWindow", "Registrar"))
        self.label.setText(_translate("MainWindow", "Cedula:  *"))
        self.label_2.setText(_translate("MainWindow", "Usuario:  *"))
        self.label_3.setText(_translate("MainWindow", "Contraseña:  *"))
        self.label_4.setText(_translate("MainWindow", "Nombre:  *"))
        self.label_5.setText(_translate("MainWindow", "Apellido:  *"))
        self.label_6.setText(_translate("MainWindow", "Edad:  *"))
        self.label_10.setText(_translate("MainWindow", "Placa:  *"))
        self.label_7.setText(_translate("MainWindow", "Email:"))
        self.label_8.setText(_translate("MainWindow", "Dirección:"))
        self.label_9.setText(_translate("MainWindow", "Teléfono:"))

    def setupUiOpciones(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 459)
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
        "#parquearButton{\n"
        "color: #2B3446;\n"
        "border-radius: 15px;\n"
        "background:white;\n"
        "font-size: 30px;\n"
        "}\n"
        "QToolButton{\n"
        "background: transparent;\n"
        "border:none;\n"
        "}\n"
        "#parquearButton:hover{\n"
        "background:transparent;\n"
        "color: white;\n"
        "border-color: white;\n"
        "border-radius: 15px;\n"
        "border-width: 4px;\n"
        "border-style: solid;\n"
        "}\n"
        "#generarFacturaButton{\n"
        "border-style: dotted;\n"
        "background: transparent;\n"
        "color:white;\n"
        "border-color: white;\n"
        "border-width:2px;\n"
        "border-radius: 15px;\n"
        "font-size: 30px;\n"
        "}\n"
        "#generarFacturaButton:hover{\n"
        "background: white;\n"
        "color:#2B3446;\n"
        "border: none\n"
        "}\n"
        "#regresarButton{\n"
        "color: #2B3446;\n"
        "border-radius: 15px;\n"
        "background:white;\n"
        "font-size: 30px;\n"
        "}\n"
        "#regresarButton:hover{\n"
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
        "#modificarInfoButton{\n"
        "font-size:15px;\n"
        "background: transparent;\n"
        "color: white;\n"
        "border: none;\n"
        "border-radius: 0px;\n"
        "}\n"
        "#modificarInfoButton:hover{\n"
        "text-decoration:underline;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.parquearButton = QtWidgets.QPushButton(self.frame)
        self.parquearButton.setGeometry(QtCore.QRect(40, 30, 451, 81))
        self.parquearButton.setObjectName("parquearButton")
        self.modificarInfoButton = QtWidgets.QPushButton(self.frame)
        self.modificarInfoButton.setGeometry(QtCore.QRect(300, 400, 191, 21))
        self.modificarInfoButton.setObjectName("modificarInfoButton")
        self.regresarButton = QtWidgets.QPushButton(self.frame)
        self.regresarButton.setGeometry(QtCore.QRect(50, 370, 191, 61))
        self.regresarButton.setObjectName("regresarButton")
        MainWindow.setCentralWidget(self.centralwidget)

        #botones
        self.regresarButton.clicked.connect(self.regresarOpciones)
        if self.indexUsuario > -1:
            if not self.ep.usuarios[self.indexUsuario].carro.enParqueo: self.parquearButton.clicked.connect(self.parquearOpciones)
            else: self.parquearButton.clicked.connect(self.facturaOpciones)
    
        self.retranslateUiOpciones(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiOpciones(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyParking"))
        if self.ep.usuarios[self.indexUsuario].carro.enParqueo:
            self.parquearButton.setText(_translate("MainWindow", "Factura"))
        else: self.parquearButton.setText(_translate("MainWindow", "Parquear"))
        self.modificarInfoButton.setText(_translate("MainWindow", "Modificar Información"))
        self.regresarButton.setText(_translate("MainWindow", "Regresar"))

    def setupUiFactura(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(418, 530)
        MainWindow.setStyleSheet("*{\n"
        "font-family: courier new;\n"
        "text-align: center;\n"
        "}\n"
        "QLabel{\n"
        "font-size: 15px;\n"
        "background: transparent;\n"
        "text-align: center;\n"
        "color: black;\n"
        "}\n"
        "QFrame{\n"
        "background: white;\n"
        "}\n"
        "QPushButton{\n"
        "color: #2B3446;\n"
        "border-radius: 5px;\n"
        "background:white;\n"
        "font-size: 15px\n"
        "}\n"
        "QPushButton:hover{\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 421, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.nit = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.nit.setFont(font)
        self.nit.setAlignment(QtCore.Qt.AlignCenter)
        self.nit.setObjectName("nit")
        self.verticalLayout.addWidget(self.nit)
        self.nombreParqueadero = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nombreParqueadero.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.nombreParqueadero.setFont(font)
        self.nombreParqueadero.setText("")
        self.nombreParqueadero.setAlignment(QtCore.Qt.AlignCenter)
        self.nombreParqueadero.setObjectName("nombreParqueadero")
        self.verticalLayout.addWidget(self.nombreParqueadero)
        self.direccion = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.direccion.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.direccion.setFont(font)
        self.direccion.setText("")
        self.direccion.setAlignment(QtCore.Qt.AlignCenter)
        self.direccion.setObjectName("direccion")
        self.verticalLayout.addWidget(self.direccion)
        self.ciudad = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ciudad.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.ciudad.setFont(font)
        self.ciudad.setText("")
        self.ciudad.setAlignment(QtCore.Qt.AlignCenter)
        self.ciudad.setObjectName("ciudad")
        self.verticalLayout.addWidget(self.ciudad)
        self.telefono = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.telefono.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.telefono.setFont(font)
        self.telefono.setText("")
        self.telefono.setAlignment(QtCore.Qt.AlignCenter)
        self.telefono.setObjectName("telefono")
        self.verticalLayout.addWidget(self.telefono)
        self.fecha = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fecha.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.fecha.setFont(font)
        self.fecha.setText("")
        self.fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.fecha.setObjectName("fecha")
        self.verticalLayout.addWidget(self.fecha)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nombre = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nombre.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.nombre.setFont(font)
        self.nombre.setText("")
        self.nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.nombre.setObjectName("nombre")
        self.horizontalLayout.addWidget(self.nombre)
        self.cedula = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cedula.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.cedula.setFont(font)
        self.cedula.setText("")
        self.cedula.setAlignment(QtCore.Qt.AlignCenter)
        self.cedula.setObjectName("cedula")
        self.horizontalLayout.addWidget(self.cedula)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.divisor1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.divisor1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        self.divisor1.setFont(font)
        self.divisor1.setAlignment(QtCore.Qt.AlignCenter)
        self.divisor1.setObjectName("divisor1")
        self.verticalLayout.addWidget(self.divisor1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tiempoInicio = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tiempoInicio.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.tiempoInicio.setFont(font)
        self.tiempoInicio.setText("")
        self.tiempoInicio.setAlignment(QtCore.Qt.AlignCenter)
        self.tiempoInicio.setObjectName("tiempoInicio")
        self.horizontalLayout_2.addWidget(self.tiempoInicio)
        self.tiempoFin = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tiempoFin.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.tiempoFin.setFont(font)
        self.tiempoFin.setText("")
        self.tiempoFin.setAlignment(QtCore.Qt.AlignCenter)
        self.tiempoFin.setObjectName("tiempoFin")
        self.horizontalLayout_2.addWidget(self.tiempoFin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.divisor2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.divisor2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.divisor2.setFont(font)
        self.divisor2.setAlignment(QtCore.Qt.AlignCenter)
        self.divisor2.setObjectName("divisor2")
        self.verticalLayout.addWidget(self.divisor2)
        self.valor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.valor.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setBold(True)
        font.setWeight(75)
        self.valor.setFont(font)
        self.valor.setText("")
        self.valor.setAlignment(QtCore.Qt.AlignCenter)
        self.valor.setObjectName("valor")
        self.verticalLayout.addWidget(self.valor)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tiempo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tiempo.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        
        font.setBold(True)
        font.setWeight(75)
        self.tiempo.setFont(font)
        self.tiempo.setText("")
        self.tiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.tiempo.setObjectName("tiempo")
        self.verticalLayout.addWidget(self.tiempo)
        self.total = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.total.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        
        font.setBold(True)
        font.setWeight(75)
        self.total.setFont(font)
        self.total.setText("")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setObjectName("total")
        self.verticalLayout.addWidget(self.total)
        #self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.divisor3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.divisor3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        
        font.setBold(True)
        font.setWeight(75)
        self.divisor3.setFont(font)
        self.divisor3.setAlignment(QtCore.Qt.AlignCenter)
        self.divisor3.setObjectName("divisor3")
        self.verticalLayout.addWidget(self.divisor3)
        self.divisor4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.divisor4.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        
        font.setBold(True)
        font.setWeight(75)
        self.divisor4.setFont(font)
        self.divisor4.setAlignment(QtCore.Qt.AlignCenter)
        self.divisor4.setObjectName("divisor4")
        self.verticalLayout.addWidget(self.divisor4)
        self.codigoDeBarras = QtWidgets.QLabel(self.frame)
        self.codigoDeBarras.setEnabled(True)
        self.codigoDeBarras.setGeometry(QtCore.QRect(0, 430, 421, 81))
        font = QtGui.QFont()
        font.setFamily("courier new")
        
        font.setBold(True)
        font.setWeight(75)
        self.codigoDeBarras.setFont(font)
        self.codigoDeBarras.setText("")
        self.codigoDeBarras.setAlignment(QtCore.Qt.AlignCenter)
        self.codigoDeBarras.setObjectName("codigoDeBarras")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(370, 0, 41, 51))
        self.label_11.setStyleSheet("")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("logo/ep_negro.svg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.regresarButton = QtWidgets.QPushButton(self.frame)
        self.regresarButton.setGeometry(QtCore.QRect(10, 10, 131, 28))
        self.regresarButton.setObjectName("regresarButton")
        MainWindow.setCentralWidget(self.centralwidget)

        #botones
        self.regresarButton.clicked.connect(self.regresarFactura)


        self.retranslateUiFactura(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiFactura(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyParking"))
        self.title.setText(_translate("MainWindow", "Easy Parking S.A"))
        self.nit.setText(_translate("MainWindow", "NIT: 1234567989"))
        self.divisor1.setText(_translate("MainWindow", "-------------------------------------------"))
        self.divisor2.setText(_translate("MainWindow", "-------------------------------------------"))
        self.divisor3.setText(_translate("MainWindow", "-------------------------------------------"))
        self.divisor4.setText(_translate("MainWindow", "-------------------------------------------"))
        self.regresarButton.setText(_translate("MainWindow", "Regresar"))
        if self.indexUsuario > -1:
            u = self.ep.usuarios[self.indexUsuario]
            if u.carro.esp[0] == self.ep.parqueaderos[u.carro.esp[1]].cod:
                p = self.ep.parqueaderos[self.ep.usuarios[self.indexUsuario].carro.esp[1]]

            e = p.espacios[u.carro.esp[2]]

            self.nombreParqueadero.setText(p.nombre)
            self.direccion.setText(p.direccion)
            self.ciudad.setText("Bogotá D.C")
            self.telefono.setText(p.tel)
            self.fecha.setText(str(date.today()))
            self.nombre.setText(u.nombre)
            self.cedula.setText(u.ced)
            tI = time.asctime(time.localtime(e.tiempoInicio))[4:]
            self.tiempoInicio.setText(tI)
            tF = time.asctime( time.localtime(time.time()))[4:]
            self.tiempoFin.setText(tF)
            self.valor.setText("Valor por minuto: $60")
            duracion = int(time.time()) -  e.tiempoInicio
            self.tiempo.setText("Tiempo total: "+str(timedelta(seconds=duracion)))
            self.total.setText("Valor total: $"+str(duracion))

            p.desparqueo(u,self.ep.usuarios[self.indexUsuario].carro.esp[1])

    def setupUiParqueaderos(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 669)
        MainWindow.setStyleSheet("*{\n"
        "font-family: segoe ui;\n"
        "/*background: #2B3446;*/\n"
        "border: none;\n"
        "}\n"
        "QLabel{\n"
        "font-size: 18px;\n"
        "color: white;\n"
        "}\n"
        "QFrame{\n"
        "background: #2B3446;\n"
        "}\n"
        "QToolButton{\n"
        "background: transparent;\n"
        "border:none;\n"
        "}\n"
        "#regresar{\n"
        "color: #2B3446;\n"
        "border-radius: 15px;\n"
        "background:white;\n"
        "font-size: 30px;\n"
        "}\n"
        "#regresar:hover{\n"
        "background: #2B3446;\n"
        "color: white;\n"
        "border: none;\n"
        "}\n"
        "QPushButton{\n"
        "color: #2B3446;\n"
        "border-radius: 5px;\n"
        "background:white;\n"
        "font-size: 18px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background: #2B3446;\n"
        "color: white;\n"
        "border-color: white;\n"
        "border-radius: 5px;\n"
        "border-style: solid;\n"
        "border-width: 1px;\n"
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
        "}\n"
        "QGroupBox{\n"
        "background: #2B3446;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1111, 671))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.regresar = QtWidgets.QPushButton(self.frame)
        self.regresar.setGeometry(QtCore.QRect(30, 600, 171, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regresar.sizePolicy().hasHeightForWidth())
        self.regresar.setSizePolicy(sizePolicy)
        self.regresar.setObjectName("regresar")
        
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(30, 30, 1041, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(0, 7, 0, 7)
        self.formLayout.setObjectName("formLayout")


        self.groupBox = QtWidgets.QGroupBox(self.scrollArea)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1041, 551))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setLayout(self.formLayout)

        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setWidgetResizable(True)

        self.ErrorLabel = QtWidgets.QLabel(self.frame)
        self.ErrorLabel.setGeometry(QtCore.QRect(0, 590, 1011, 31))
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")


        for inP, p in enumerate(self.ep.parqueaderos):
            label = QtWidgets.QLabel(p.nombre) 
            label.setObjectName(str("nombre_"+str(inP))) 
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed) 
            sizePolicy.setHorizontalStretch(0) 
            sizePolicy.setVerticalStretch(0) 
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth()) 
            label.setSizePolicy(sizePolicy)

            button1 = QtWidgets.QPushButton("   Elegir   ")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed) 
            sizePolicy.setHorizontalStretch(0) 
            sizePolicy.setVerticalStretch(0) 
            sizePolicy.setHeightForWidth(button1.sizePolicy().hasHeightForWidth()) 
            #---------
            button1.setSizePolicy(sizePolicy)

            button2 = DButton(self,"  Autom.  ",inP)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed) 
            sizePolicy.setHorizontalStretch(0) 
            sizePolicy.setVerticalStretch(0) 
            sizePolicy.setHeightForWidth(button2.b.sizePolicy().hasHeightForWidth()) 
            button2.b.setSizePolicy(sizePolicy)
            #---------
            button2.connectAutoParq(p)
            

            lay = QtWidgets.QHBoxLayout()
            lay.setContentsMargins(30,0,30,0)
            lay.addWidget(label)           
            lay.addWidget(button1)
            lay.addWidget(button2.b)


            self.formLayout.addRow(lay)

        #botones
        self.regresar.clicked.connect(self.regresarParqueaderos)
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUiParqueaderos(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiParqueaderos(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyParking"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
    
    def setupUiEditarParq(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 669)
        MainWindow.setStyleSheet("*{\n"
        "font-family: segoe ui;\n"
        "/*background: #2B3446;*/\n"
        "background:transparent;\n"
        "border: none;\n"
        "}\n"
        "QLabel{\n"
        "font-size: 13px;\n"
        "color: white;\n"
        "}\n"
        "QFrame{\n"
        "background: #2B3446;\n"
        "}\n"
        "QPushButton{\n"
        "color: white;\n"
        "font-size: 18px;\n"
        "font-weight: bold;\n"
        "border-style: solid;\n"
        "border-width: 1px;\n"
        "border-color:white;\n"
        "}\n"
        "QPushButton:hover{\n"
        "color: #2B3446;\n"
        "background:white;\n"
        "}\n"
        "QLineEdit{\n"
        "background:transparent;\n"
        "color: white;\n"
        "border: none;\n"
        "border-bottom: 1px solid;\n"
        "border-color: white;\n"
        "font-size: 18px;\n"
        "}\n"
        "#ErrorLabel{\n"
        "font-size: 20px;\n"
        "background: transparent;\n"
        "color: red\n"
        "}\n"
        "QGroupBox{\n"
        "background: #2B3446;\n"
        "}\n"
        "#codLab, #totalesLab, #ocupadosLab{\n"
        "font-size: 18px;\n"
        "}\n"
        "#addButton, #undoButton, #redoButton{\n"
        "border:none\n"
        "}\n"
        "#addButton:hover, #undoButton:hover, #redoButton:hover{\n"
        "border-style: solid;\n"
        "border-color:white;\n"
        "border-width: 2px;\n"
        "background: transparent;\n"
        "border-radius:20px;\n"
        "}\n"
        "#line{\n"
        "color:white;\n"
        "line-color:white;\n"
        "}\n"
        "#guardar,#regresar{\n"
        "font-weight: normal;\n"
        "color: #2B3446;\n"
        "background: white;\n"
        "font-size: 30px;\n"
        "border-radius: 15px;\n"
        "}\n"
        "#guardar:hover,#regresar:hover{\n"
        "font-weight: normal;\n"
        "color: white;\n"
        "background:#2B3446;\n"
        "border: none;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1111, 671))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.guardar = QtWidgets.QPushButton(self.frame)
        self.guardar.setGeometry(QtCore.QRect(220, 600, 171, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guardar.sizePolicy().hasHeightForWidth())
        self.guardar.setSizePolicy(sizePolicy)
        self.guardar.setObjectName("guardar")

        self.regresar = QtWidgets.QPushButton(self.frame)
        self.regresar.setGeometry(QtCore.QRect(30, 600, 171, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regresar.sizePolicy().hasHeightForWidth())
        self.regresar.setSizePolicy(sizePolicy)
        self.regresar.setObjectName("regresar")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(30, 70, 1041, 511))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.vLayout = QtWidgets.QVBoxLayout()
        self.vLayout.setContentsMargins(0, 7, 0, 7)
        self.vLayout.setObjectName("vLayout")

        self.groupBox = QtWidgets.QGroupBox(self.scrollArea)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1041, 551))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setLayout(self.vLayout)

        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setWidgetResizable(True)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(60, 60))
        self.addButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/addButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QtCore.QSize(40, 40))
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)
        self.undoButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undoButton.sizePolicy().hasHeightForWidth())
        self.undoButton.setSizePolicy(sizePolicy)
        self.undoButton.setMinimumSize(QtCore.QSize(60, 60))
        self.undoButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("logo/undoButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon1)
        self.undoButton.setIconSize(QtCore.QSize(40, 40))
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout_2.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redoButton.sizePolicy().hasHeightForWidth())
        self.redoButton.setSizePolicy(sizePolicy)
        self.redoButton.setMinimumSize(QtCore.QSize(60, 60))
        self.redoButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("logo/redoButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon2)
        self.redoButton.setIconSize(QtCore.QSize(40, 40))
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout_2.addWidget(self.redoButton)
        self.vLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.vLayout.addItem(spacerItem)

        for inP, p in enumerate(self.ep.parqueaderos):
            self.fLayout = QtWidgets.QFormLayout()
            self.fLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.fLayout.setFormAlignment(QtCore.Qt.AlignCenter)
            self.fLayout.setContentsMargins(7, -1, 7, -1)
            self.fLayout.setHorizontalSpacing(15)
            self.fLayout.setObjectName("fLayout")

            self.telLabel = QtWidgets.QLabel("Telefono")
            self.telLabel.setObjectName("label_2")
            self.fLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.telLabel)

            self.label_3 = QtWidgets.QLabel("Gerente")
            self.label_3.setObjectName("label_3")
            self.fLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_3)

            self.label_5 = QtWidgets.QLabel("Nombre")
            self.label_5.setObjectName("label_5")
            self.fLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)

            self.label_6 = QtWidgets.QLabel("Dirección")
            self.label_6.setObjectName("label_6")
            self.fLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.label_6)

            self.label_7 = QtWidgets.QLabel("")
            self.label_7.setObjectName("label_7")
            self.fLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_7)

            self.nombreEdit = QtWidgets.QLineEdit(p.nombre)
            self.nombreEdit.setObjectName("nombreEdit")
            self.fLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.nombreEdit)

            self.telEdit = QtWidgets.QLineEdit(p.tel)
            self.telEdit.setMinimumSize(QtCore.QSize(210, 0))
            self.telEdit.setObjectName("telEdit")
            self.fLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.telEdit)

            self.gerenteEdit = QtWidgets.QLineEdit(p.gerente)
            self.gerenteEdit.setObjectName("gerenteEdit")
            self.fLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.gerenteEdit)
            
            self.direccionEdit = QtWidgets.QLineEdit(p.direccion)
            self.direccionEdit.setObjectName("direccionEdit")
            self.fLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.direccionEdit)

            self.totalesLab = QtWidgets.QLabel("Totales: "+str(p.totales))
            self.totalesLab.setObjectName("totalesLab")
            self.fLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.totalesLab)

            self.ocupadosLab = QtWidgets.QLabel("Ocupados: "+str(p.ocupados))
            self.ocupadosLab.setObjectName("ocupadosLab")
            self.fLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.ocupadosLab)

            self.codLab = QtWidgets.QLabel("Codigo: "+p.cod)
            self.codLab.setObjectName("codLab")
            self.fLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.codLab)

            spacerItem1 = QtWidgets.QSpacerItem(210, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.fLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)

            agregarEspButton = DButton(self,"AÑADIR ESPACIO",inP)
            agregarEspButton.b.setMinimumSize(QtCore.QSize(210, 0))
            agregarEspButton.b.setObjectName("agregarEspButton")
            agregarEspButton.connectAgregarEsp()
            self.fLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, agregarEspButton.b)

            vaciarButton = DButton(self,"VACIAR",inP)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(vaciarButton.b.sizePolicy().hasHeightForWidth())
            vaciarButton.b.setSizePolicy(sizePolicy)
            vaciarButton.b.setMinimumSize(QtCore.QSize(210, 0))
            vaciarButton.b.setObjectName("vaciarButton")
            vaciarButton.connectVaciar(p)
            self.fLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, vaciarButton.b)
            '''
            self.eliminarButton = QtWidgets.QPushButton("ELIMINAR")
            self.eliminarButton.setMinimumSize(QtCore.QSize(210, 0))
            self.eliminarButton.setObjectName("eliminarButton"+str(inP))
            self.eliminarButton.clicked.connect(lambda: self.pp(inP))
            self.fLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.eliminarButton)
            self.eliminarButtons.append(self.eliminarButton)
            '''
            eliminarButton = DButton(self,"ELIMINAR",inP)
            eliminarButton.b.setMinimumSize(QtCore.QSize(210, 0))
            eliminarButton.b.setObjectName("eliminarButton"+str(inP))
            eliminarButton.connectEliminar()
            self.fLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, eliminarButton.b)

            for i in range(4):
                self.spLabel = QtWidgets.QLabel()
                self.fLayout.addRow(self.spLabel)

            self.vLayout.addLayout(self.fLayout)

        #botones
        self.regresar.clicked.connect(self.regresarEditarParq)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUiEditarParq(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiEditarParq(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EasyParking"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))

    def pp(self,x):
        print(f"{x} pressed")

class DButton():
    def __init__ (self,mainWindow,text,x):
        self.mainWindow = mainWindow
        self.b = QtWidgets.QPushButton(text)
        self.x = x
    
    def connectEliminar(self):
        self.b.clicked.connect(lambda: self.mainWindow.pp(self.x))
    
    def connectAutoParq(self,p):
        self.b.clicked.connect(lambda: self.mainWindow.autoParqueo(p,self.x))

    def connectVaciar(self,p):
        self.b.clicked.connect(lambda: self.mainWindow.vaciarParq(p,self.x))

    def connectAgregarEsp(self):
        self.b.clicked.connect(lambda: self.mainWindow.pp(self.x))


if __name__ == "__main__":
    '''
    for i in range(30):
        lines = []
        lines.append(f"Parqueadero{i}*{i}*Av. Calle{i} # {i+20} 65*2314506*Tomas Aparicio*10*0\n")
        lines.append("0000000000\n")
        with open(f"parqueaderos/p{i}","w") as f:
            f.writelines(lines)
    '''
    import sys
    ep = EasyParking.EasyParking()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow,ep,-1,-1)
    ui.setupUiLogin(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
