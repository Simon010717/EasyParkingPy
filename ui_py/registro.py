# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Simon/Desktop/EasyParkingPy/ui_py/registro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 758)
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
        self.label_11.setPixmap(QtGui.QPixmap(":/logo/ep_blanco.svg"))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
