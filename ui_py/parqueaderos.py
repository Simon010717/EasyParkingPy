# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ADMIN/Desktop/EasyParkingPy/ui_py/parqueaderos.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 519)
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
        self.frame.setGeometry(QtCore.QRect(0, 0, 561, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 20, 421, 411))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nombres = QtWidgets.QVBoxLayout()
        self.nombres.setObjectName("nombres")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.nombres.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.nombres.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.nombres)
        self.botones = QtWidgets.QVBoxLayout()
        self.botones.setObjectName("botones")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.botones.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.botones.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.botones)
        self.regresar = QtWidgets.QPushButton(self.frame)
        self.regresar.setGeometry(QtCore.QRect(20, 460, 181, 41))
        self.regresar.setObjectName("regresar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
