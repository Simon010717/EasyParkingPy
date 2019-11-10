import time, random, string, os, time
import data_structures as dt


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
        super().__init__(ced, nickname, password, nombre, apellido, edad, email, direccion, tel)

class Espacio:
    def __init__ (self,cod,hora_incio = None,carro = None,libre = True):
        self.cod = cod
        self.hora_incio = hora_incio
        self.libre = libre
        self.carro = carro

class Empleado:
    def __init__(self,nickname,password,nombre):
        self.nickname = nickname
        self.password = password
        self.nombre = nombre

class EasyParking:

    def __init__(self):
        self.usuariosRoute = "usuarios.ep"
        self.parqueaderosRoute = "parqueaderos"
        self.empleadosRoute = "empleados.ep"
        self.usuarios = []
        self.addUsuarios()
        self.parqueaderos = []
        self.addParqueaderos()
        self.empleados = []
        self.addEmpleados()

    def addParqueaderos(self):
        n = len(os.listdir(self.parqueaderosRoute))
        for i in range(n):
            with open(self.parqueaderosRoute+"/p"+str(i),"r") as f:
                data = f.readlines()
            data[0] = data[0].rstrip('\n')
            self.addParqueadero(data[0].split('*'),True)
            ocupados = []
            for b in range (len(data[1])):
                if data[1][b] == '1': ocupados.append(b)
            l = 2
            for p in ocupados:
                info = []
                info = info + data[l].split('*')
                info[0] = info[0]
                info[1] = info[1].rstrip('\n')
                if self.buscarUsuario(info[1]) is not None:
                    self.parqueaderos[i].espacios[p] = Espacio(p,info[0],self.buscarUsuario(info[1]).carro,False)
                    self.parqueaderos[i].espaciosTree.root = self.parqueaderos[i].espaciosTree.insert(p,self.parqueaderos[i].espaciosTree.root)
                l+=1
    
    def addParqueadero(self,info,verified):
        if not verified:
            for p in self.parqueaderos:
                if p.cod == info[1]: return False
            data = []
            data.append('*'.join(info)+'\n')
            data.append("0"*(int(info[5])-int(info[6])))
            with open(self.parqueaderosRoute+"/p"+str(len(self.parqueaderos)),"w") as f:
                f.writelines(data)
        self.parqueaderos.append(Parqueadero(info[0],info[1],info[2],info[3],info[4],int(info[5]),int(info[6])))

    def addUsuarios(self):
        with open(self.usuariosRoute,"r") as f:
            data = f.readlines()
        
        for line in data:
            line = line.rstrip('\n')
            self.addUsuarioArr(line.split("*"),True)

    def addUsuarioArr(self,info,verified):
        if len(info) < 7: return None
        if not verified:
            check = self.checkInfo(info)
            if check < 3: return check

        line = '*'.join(info)

        for i in range(len(info),10):
            info.append(None)

        self.usuarios.append(Usuario(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9]))
        
        if not verified:
            with open(self.usuariosRoute,"a") as f:
                if len(self.usuarios) > 1: f.write('\n')
                f.writelines(line)

        return 3
    
    def checkLogin(self,nickname,password):
        for index, u in enumerate(self.usuarios):
            if u.nickname == nickname:
                if u.password == password: return index
                return -1
        return -2
    
    def buscarEmpleado(self,ced):
        for e in self.empleados:
            if ced == e.ced:
                return e
        return None
           
    def addEmpleados(self):
        with open(self.empleadosRoute,"r") as f:
            data = f.readlines()
        
        for line in data:
            line = line.rstrip('\n')
            self.addEmpleadoArr(line.split("*"),True)

    def addEmpleadoArr(self,info,verified):
        if len(info) < 3: return None
        if not verified:
            check = self.checkInfoEmpleado(info)
            if check < 3: return check

        line = '*'.join(info)

        for i in range(len(info),10):
            info.append(None)

        self.empleados.append(Empleado(info[0],info[1],info[2]))
        
        if not verified:
            with open(self.empleadosRoute,"a") as f:
                if len(self.empleados) > 1: f.write('\n')
                f.writelines(line)

        return 3
    
    def checkLoginEmpleado(self,nickname,password):
        for index, e in enumerate(self.empleados):
            if e.nickname == nickname:
                if e.password == password: return index
                return -1
        return -2

    def buscarUsuario(self,ced):
        for u in self.usuarios:
            if ced == u.ced:
                return u
        return None
    
class Parqueadero:

    def __init__(self,nombre,cod,direccion,tel,gerente,totales,ocupados):
        self.espaciosTree = dt.AvlTree()
        self.espacios = [None]*totales
        self.totales = totales
        self.ocupados = ocupados

        self.nombre = nombre
        self.cod = cod
        self.direccion = direccion
        self.tel = tel
        self.gerente = gerente
        
    def addEspacio(self):
        self.espacios.append(Espacio(self.espaciosTotales+1))   

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
    n = 1000
    avl = dt.AvlTree()
    st = time.time()
    for i in range(1,n+1):
        siguiente = avl.siguiente(i,n)        
        if siguiente is not None:
            avl.root = avl.insert(avl.siguiente(i,n),avl.root)
        else:
            k = n-1
            while avl.contains(k,avl.root):
                k -= 1
            avl.insert(k,avl.root)


if __name__ == "__main__":
    #main()
    print("done")

    
