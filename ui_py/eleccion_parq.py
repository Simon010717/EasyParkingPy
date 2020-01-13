# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Simon/Desktop/EasyParkingPy/ui_py/eleccion_parq.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 601)
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
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1281, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 70, 1232, 604))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.p1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1.sizePolicy().hasHeightForWidth())
        self.p1.setSizePolicy(sizePolicy)
        self.p1.setMinimumSize(QtCore.QSize(114, 196))
        self.p1.setIconSize(QtCore.QSize(5, 5))
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 0, 1, 1, 1)
        self.p1_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_3.sizePolicy().hasHeightForWidth())
        self.p1_3.setSizePolicy(sizePolicy)
        self.p1_3.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_3.setIconSize(QtCore.QSize(5, 5))
        self.p1_3.setObjectName("p1_3")
        self.gridLayout.addWidget(self.p1_3, 0, 3, 1, 1)
        self.p1_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_5.sizePolicy().hasHeightForWidth())
        self.p1_5.setSizePolicy(sizePolicy)
        self.p1_5.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_5.setIconSize(QtCore.QSize(5, 5))
        self.p1_5.setObjectName("p1_5")
        self.gridLayout.addWidget(self.p1_5, 0, 5, 1, 1)
        self.p1_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_7.sizePolicy().hasHeightForWidth())
        self.p1_7.setSizePolicy(sizePolicy)
        self.p1_7.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_7.setIconSize(QtCore.QSize(5, 5))
        self.p1_7.setObjectName("p1_7")
        self.gridLayout.addWidget(self.p1_7, 0, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 196, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.p1_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_4.sizePolicy().hasHeightForWidth())
        self.p1_4.setSizePolicy(sizePolicy)
        self.p1_4.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_4.setIconSize(QtCore.QSize(5, 5))
        self.p1_4.setObjectName("p1_4")
        self.gridLayout.addWidget(self.p1_4, 0, 4, 1, 1)
        self.p1_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_6.sizePolicy().hasHeightForWidth())
        self.p1_6.setSizePolicy(sizePolicy)
        self.p1_6.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_6.setIconSize(QtCore.QSize(5, 5))
        self.p1_6.setObjectName("p1_6")
        self.gridLayout.addWidget(self.p1_6, 0, 6, 1, 1)
        self.p1_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_9.sizePolicy().hasHeightForWidth())
        self.p1_9.setSizePolicy(sizePolicy)
        self.p1_9.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_9.setIconSize(QtCore.QSize(5, 5))
        self.p1_9.setObjectName("p1_9")
        self.gridLayout.addWidget(self.p1_9, 0, 9, 1, 1)
        self.p1_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_10.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_10.sizePolicy().hasHeightForWidth())
        self.p1_10.setSizePolicy(sizePolicy)
        self.p1_10.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_10.setIconSize(QtCore.QSize(5, 5))
        self.p1_10.setObjectName("p1_10")
        self.gridLayout.addWidget(self.p1_10, 0, 10, 1, 1)
        self.p1_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_2.sizePolicy().hasHeightForWidth())
        self.p1_2.setSizePolicy(sizePolicy)
        self.p1_2.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_2.setIconSize(QtCore.QSize(5, 5))
        self.p1_2.setObjectName("p1_2")
        self.gridLayout.addWidget(self.p1_2, 0, 2, 1, 1)
        self.p1_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_8.sizePolicy().hasHeightForWidth())
        self.p1_8.setSizePolicy(sizePolicy)
        self.p1_8.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_8.setIconSize(QtCore.QSize(5, 5))
        self.p1_8.setObjectName("p1_8")
        self.gridLayout.addWidget(self.p1_8, 0, 8, 1, 1)
        self.p1_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.p1_11.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_11.sizePolicy().hasHeightForWidth())
        self.p1_11.setSizePolicy(sizePolicy)
        self.p1_11.setMinimumSize(QtCore.QSize(114, 196))
        self.p1_11.setIconSize(QtCore.QSize(5, 5))
        self.p1_11.setObjectName("p1_11")
        self.gridLayout.addWidget(self.p1_11, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 15, 231, 41))
        self.label.setObjectName("label")
        self.archivar = QtWidgets.QPushButton(self.frame)
        self.archivar.setGeometry(QtCore.QRect(40, 540, 151, 41))
        self.archivar.setObjectName("archivar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.p1.setText(_translate("MainWindow", "."))
        self.p1_3.setText(_translate("MainWindow", "."))
        self.p1_5.setText(_translate("MainWindow", "."))
        self.p1_7.setText(_translate("MainWindow", "."))
        self.p1_4.setText(_translate("MainWindow", "."))
        self.p1_6.setText(_translate("MainWindow", "."))
        self.p1_9.setText(_translate("MainWindow", "."))
        self.p1_10.setText(_translate("MainWindow", "."))
        self.p1_2.setText(_translate("MainWindow", "."))
        self.p1_8.setText(_translate("MainWindow", "."))
        self.p1_11.setText(_translate("MainWindow", "."))
        self.label.setText(_translate("MainWindow", "Parqueadero Tulio Varon"))
        self.archivar.setText(_translate("MainWindow", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
