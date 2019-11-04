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

class EasyParking:

    def __init__(self):
        self.usuariosRoute = "usuarios.ep"
        self.parqueaderosRoute = "parqueaderos"
        self.usuarios = []
        self.addUsuarios()
        self.parqueaderos = []
        self.addParqueaderos()

    def addParqueaderos(self):
        n = len(os.listdir(self.parqueaderosRoute))
        for i in range(n):
            with open(self.parqueaderosRoute+"/p"+str(i),"r") as f:
                data = f.readlines()
            l = 0
            data[l] = data[l].rstrip('\n')
            self.addParqueadero(data[l].split('*'),True)
            l += 1
            ocupados = []
            for b in range (len(data[l])):
                if data[l][b] == '1': ocupados.append(b)
            l += 1
            for p in ocupados:
                info = [p]
                info = info + data[l].split('*')
                info[1] = int(info[1])
                info[2] = int(info[2].rstrip('\n'))
                self.parqueaderos[i].parqueo(info,True)
                self.parqueaderos[i].espacios[p] = Espacio(l-2,info[0],self.buscarUsuario(info[1]).carro,False)
                l+=1
    
    def buscarUsuario(self,ced):
        for u in self.usuarios:
            if ced == u.ced: return u
        return None
        
    def addParqueadero(self,info,verified):
        if not verified:
            for p in self.parqueaderos:
                if p.cod == info[1]: return False
            data = []
            data.append('*'.join(info)+'\n')
            data.append("0"*(int(info[5])-int(info[6])))
            print(data)
            with open(self.parqueaderosRoute+"/p"+str(len(self.parqueaderos)),"w") as f:
                f.writelines(data)
        self.parqueaderos.append(Parqueadero(info[0],info[1],info[2],info[3],info[4],int(info[5]),int(info[6])))
        
    def addUsuarios(self):
        with open(self.usuariosRoute,"r") as f:
            data = f.readlines()
        
        for line in data:
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
                if self.usuarios > 1: f.write('\n')
                f.writelines(line)

        return 3
    
    def checkLogin(self,nickname,password):
        for u in self.usuarios:
            if u.nickname == nickname:
                if u.password == password: return True
                return False
        return False


    #def addUsuario(self, ced, nickname, password, nombre, apellido, edad, placa, email=None, direccion=None, tel=None):
    #    self.usuarios.append(Usuario(ced, nickname, password, nombre, apellido, edad, placa, email, direccion, tel))

    def checkInfo(self,info):
        ced = info[0]
        nickname = info[1]
        placa = info[2]

        for u in self.usuarios:
            if u.ced == ced: return 0
            if u.nickname == nickname: return 1
            if u.carro.placa == placa: return 2
        return 3
    
    def comprobarUsuario(self, nickname, password):
        for i in range(len(self.usuarios)):
            if(self.usuarios[i].nickname == nickname and self.usuarios[i].password == password):
                return True
        
        return False
    
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

    def parqueo(self,info,verified):
        carro = self.buscarUsuario(info[2])
        if not verified and carro is None: return False
        self.espacios[info[0]] = Espacio(info[0],info[1],carro,False)
        self.espaciosTree.insert(info[0])
        

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

    print()
    print(avl.root.data)
    print(avl.findMax(avl.root))
    print(avl.findMin(avl.root))
    print(avl.x)
    for i in range(n):
        if not avl.contains(i,avl.root): print(i,end = ':')



if __name__ == "__main__":
    main()


    
