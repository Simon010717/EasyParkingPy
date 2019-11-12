# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Simon/Desktop/EasyParkingPy/ui_py/opciones.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 459)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parquearButton.setText(_translate("MainWindow", "Parquear"))
        self.modificarInfoButton.setText(_translate("MainWindow", "Modificar Información"))
        self.regresarButton.setText(_translate("MainWindow", "Regresar"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
