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
        MainWindow.resize(530, 462)
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
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 531, 461))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.parquearButton = QtWidgets.QPushButton(self.frame_3)
        self.parquearButton.setGeometry(QtCore.QRect(40, 30, 451, 81))
        self.parquearButton.setObjectName("parquearButton")
        self.generarFacturaButton = QtWidgets.QPushButton(self.frame_3)
        self.generarFacturaButton.setGeometry(QtCore.QRect(40, 340, 451, 61))
        self.generarFacturaButton.setObjectName("generarFacturaButton")
        self.modificarInfoButton = QtWidgets.QPushButton(self.frame_3)
        self.modificarInfoButton.setGeometry(QtCore.QRect(170, 410, 191, 21))
        self.modificarInfoButton.setObjectName("modificarInfoButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parquearButton.setText(_translate("MainWindow", "Parquear"))
        self.generarFacturaButton.setText(_translate("MainWindow", "Factura"))
        self.modificarInfoButton.setText(_translate("MainWindow", "Modificar Información"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
