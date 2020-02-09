# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Simon/Desktop/EasyParkingPy/ui_py/editarParq.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
"#codLab, #totalesLab, #ocupadosLab, #maxPointsLab{\n"
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
"QVBoxLayout{\n"
"border-style: solid;\n"
"border-color:white;\n"
"border-width: 2px;\n"
"}\n"
"#guardar,#regresar{\n"
"color: #2B3446;\n"
"background: white;\n"
"font-size: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"#guardar:hover,#regresar:hover{\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:white;\n"
"border-radius: 15px;\n"
"background:#2B3446;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1111, 671))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(30, 30, 1041, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1041, 551))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 1041, 541))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1041, 878))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.maxPointsLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.maxPointsLab.setFont(font)
        self.maxPointsLab.setObjectName("maxPointsLab")
        self.verticalLayout.addWidget(self.maxPointsLab)


        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setContentsMargins(7, -1, 7, -1)
        self.formLayout_3.setHorizontalSpacing(15)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(210, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.totalesLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.totalesLab.setObjectName("totalesLab")
        self.formLayout_3.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.totalesLab)
        self.ocupadosLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ocupadosLab.setObjectName("ocupadosLab")
        self.formLayout_3.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.ocupadosLab)
        self.codLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.codLab.setObjectName("codLab")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.codLab)
        spacerItem = QtWidgets.QSpacerItem(210, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_3.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.agregarEspButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.agregarEspButton.setMinimumSize(QtCore.QSize(210, 0))
        self.agregarEspButton.setObjectName("agregarEspButton")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.agregarEspButton)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(210, 0))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(210, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.verticalLayout.addLayout(self.formLayout_3)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "."))
        self.maxPointsLab.setText(_translate("MainWindow", "Usuario con mayor cantidad de puntos:"))
        self.label_2.setText(_translate("MainWindow", "Telefono"))
        self.label_3.setText(_translate("MainWindow", "Gerente"))
        self.label_5.setText(_translate("MainWindow", "Nombre"))
        self.label_6.setText(_translate("MainWindow", "Direccion"))
        self.totalesLab.setText(_translate("MainWindow", "Totales: 50"))
        self.ocupadosLab.setText(_translate("MainWindow", "Ocupados: 23"))
        self.codLab.setText(_translate("MainWindow", "Codigo"))
        self.agregarEspButton.setText(_translate("MainWindow", "AÑADIR ESPACIO"))
        self.pushButton.setText(_translate("MainWindow", "VACIAR"))
        self.pushButton_2.setText(_translate("MainWindow", "ELIMINAR"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
import logo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
