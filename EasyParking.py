import time, random, string


class Carro:
    def __init__ (self, placa):
        self.placa = placa
        self.enParqueo = False

class Persona:
    def __init__ (self, ced, nickname, password, nombre, apellido, edad, email=None, direccion=None, tel=None):
        self.ced = ced
        self.nickname = nickname
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.direccion = direccion
        self.tel = tel   

class Usuario(Persona):
    def __init__(self, ced, nickname, password, nombre, apellido, edad, placa, email=None, direccion=None, tel=None):
        self.carro = Carro(placa)
        Persona.__init__(self, ced, nickname, password, nombre, apellido, edad, email, direccion, tel)

class Espacio:
    def __init__ (self,numero):
        self.numero = numero
        libre = True
        carro = None

    def llenar(self,usuario):
        self.carro = usuario.carro
        self.libre = False

class Parqueadero:
    def __init__(self):
        self.espacios = []
        self.usuarios = []
        self.espaciosTotales = 0
        self.espaciosOcupados = 0

    def addEspacio(self):
        self.espacios.append(Espacio(self.espaciosTotales+1))

    def addUsuario(self, ced, nickname, password, nombre, apellido, edad, placa, email=None, direccion=None, tel=None):
        self.usuarios.append(Usuario(ced, nickname, password, nombre, apellido, edad, placa, email, direccion, tel))

    def buscarId(self,id):
        for i in range(len(self.usuarios)):
            if(self.usuarios[i].id == id):
                return usuarios[i]
    
    def comprobarUsuario(self, nickname, password):
        for i in range(len(self.usuarios)):
            if(self.usuarios[i].nickname == nickname and self.usuarios[i].password == password):
                return True
        
        return False
    
    def puestosVacios(self):
        return self.espaciosTotales - len(self.espacios)
    
    def nextLibre(self):
        if(len(self.espacios) < espaciosTotales):
            if(len(self.espacios) == 0): 
                return 0
            elif (self.espacios[len(self.espacios)-1].numero < espaciosTotales-1):
                return self.espacios[len(self.espacios)-1].numero
            else:
                for i in range(len(self.espacios)-1):
                    if(espacios[i].numero != i):
                        return espacios[i-1].numero +1
        return -1
    
    def parqueo(self, user):
        if(len(self.espacios) < self.espaciosTotales and user.carro.enParqueo):
            nextLibre = nextLibre()
            self.espacios.append(Espacio(nextLibre))
            self.espacios[len(self.espacios)-1].llenar(user)
        else:
            print("Parqueadero ocupado")

    def desparqueo(self,user: Usuario):
        for i in range(len(self.espacios)): #puede ser mejorable guardando el espacio en el carro
            if(espacios[i].carro.placa == user.carro.placa):
                self.espacios.pop(i)

class Test:
    def rndStr(self,n):
        return "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") for i in range(n))

    def testDynamicArray(self,n,p):
        start = time.time()
        usuarios = []

        for i in range(0,n):
            usuarios.append(Usuario(self.rndStr(10),self.rndStr(10),self.rndStr(10),self.rndStr(10),self.rndStr(10),random.randint(18,70),self.rndStr(3)+str(random.randrange(1000))))
            if(i%5 == 0):
                usuarios[random.randrange(len(usuarios))].nombre = self.rndStr(10)
            if(i%20):
                usuarios.pop(random.randrange(len(usuarios)))

        return time.time() - start

    


def main():
    print("Testing")
    user = Usuario("1001","saparicio","SAB","Simon","Aparicio",15,"DNS243")
    print(user.nombre)



if __name__ == "__main__":
    test = Test()
    print(test.testDynamicArray(1000000,500000))


    
