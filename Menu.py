import sys
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QPushButton
from PyQt5 import uic

class Inicio(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("interfaz.ui",self)
        self.registro.clicked.connect(self.Registrar)

    def Registrar(self):
        registro=Registro()
        registro.exec_()

class Registro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("registro.ui",self)

app=QApplication(sys.argv)
inicio=Inicio()
inicio.show()
app.exec_()