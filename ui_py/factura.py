# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Simon/Desktop/EasyParkingPy/ui_py/factura.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(420, 551)
        MainWindow.setStyleSheet("*{\n"
"font-family: courier new;\n"
"align: center;\n"
"}\n"
"QLabel{\n"
"font-size: 15px;\n"
"background: transparent;\n"
"text-align: center;\n"
"color: black;\n"
"}\n"
"QFrame{\n"
"background: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.tiempo.setFont(font)
        self.tiempo.setText("")
        self.tiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.tiempo.setObjectName("tiempo")
        self.horizontalLayout_3.addWidget(self.tiempo)
        self.total = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.total.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.total.setFont(font)
        self.total.setText("")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setObjectName("total")
        self.horizontalLayout_3.addWidget(self.total)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.divisor3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.divisor3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setPointSize(-1)
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
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.divisor4.setFont(font)
        self.divisor4.setAlignment(QtCore.Qt.AlignCenter)
        self.divisor4.setObjectName("divisor4")
        self.verticalLayout.addWidget(self.divisor4)
        self.codigoDeBarras = QtWidgets.QLabel(self.frame)
        self.codigoDeBarras.setEnabled(True)
        self.codigoDeBarras.setGeometry(QtCore.QRect(0, 460, 421, 81))
        font = QtGui.QFont()
        font.setFamily("courier new")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.codigoDeBarras.setFont(font)
        self.codigoDeBarras.setText("")
        self.codigoDeBarras.setAlignment(QtCore.Qt.AlignCenter)
        self.codigoDeBarras.setObjectName("codigoDeBarras")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Easy Parking S.A"))
        self.nit.setText(_translate("MainWindow", "NIT: 1234567989"))
        self.divisor1.setText(_translate("MainWindow", "-------------------------------------------"))
        self.divisor2.setText(_translate("MainWindow", "-------------------------------------------"))
        self.divisor3.setText(_translate("MainWindow", "-------------------------------------------"))
        self.divisor4.setText(_translate("MainWindow", "-------------------------------------------"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())