from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog,QGroupBox,QVBoxLayout,QHBoxLayout
import sys 

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Easy Parking"
        self.top=200
        self.left=500
        self.width=400
        self.height=500
        self.Iniciar()
        self.setStyleSheet("background-color: #847C7B")



    def Iniciar(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.Componentes()
        vbox=QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

#funcion para agregar todos los componentes
    def Componentes(self):
        self.groupBox = QGroupBox("Menú")
        vbox1=QVBoxLayout()
        registrar=QPushButton("Registrarse",self)
        registrar.setGeometry(100,100,100,50)
        registrar.setStyleSheet("border-width:2px")
        registrar.clicked.connect(self.Pasar)
        vbox1.addWidget(registrar)
        salir=QPushButton("Salir",self)
        salir.setGeometry(100,100,100,50)
        salir.clicked.connect(self.Salir)
        vbox1.addWidget(salir)
        self.groupBox.setLayout(vbox1)

    def Pasar(self):
        ventanaRegistro=Registro()
        ventanaRegistro.exec_()

    def Salir(self):
        sys.exit(0)

class Registro(QDialog):
     def __init__(self):
        QDialog.__init__(self)

        self.title = "Registro"
        self.top=100
        self.left=100
        self.width=400
        self.height=300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.Componentes()
        self.show()
    
     def Componentes(self):
        button=QPushButton("Atras",self)
        button.setGeometry(100,100,100,50)
        button.clicked.connect(self.Atras)

     def Atras(self):
        main=QMainWindow()
        main.show()




#bloque que permite ejecutar la pagina
if __name__=="__main__":
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec())


