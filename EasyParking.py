import time, random, string, os, time
import data_structures as dt


class Carro:
    def __init__ (self, placa):
        self.placa = placa
        self.enParqueo = False
        self.esp = None

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
    def __init__(self, ced, nickname, password, nombre, apellido, edad, placa, puntos, email=None, direccion=None, tel=None):
        self.carro = Carro(placa)
        super().__init__(ced, nickname, password, nombre, apellido, edad, email, direccion, tel)
        self.puntos = int(puntos)

class Espacio:
    def __init__ (self,cod,tiempoI,carro = None,libre = True):
        self.cod = cod
        self.tiempoInicio = tiempoI
        self.libre = libre
        self.carro = carro
        self.reservas = dt.BinaryHeap(10)

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
        self.usuarios = dt.HashMap(1000)
        self.nicknames = dt.StringHashMap(1000,15)
        self.placas = dt.StringHashMap(1000,10)
        self.addUsuarios()
        self.parqueaderos = []
        self.addParqueaderos()
        self.empleados = dt.StringHashMap(1000,15)
        self.addEmpleados()
        self.puntos = dt.BinaryHeap()

    def addParqueaderos(self):
        n = len(os.listdir(self.parqueaderosRoute))
        for p in range(n):
            with open(self.parqueaderosRoute+"/p"+str(p),"r") as f:
                data = f.readlines()
            data[0] = data[0].rstrip('\n')
            self.addParqueadero(data[0].split('*'),True)
            ocupados = []
            for b in range (len(data[1])):
                if data[1][b] == '1': ocupados.append(b)
            l = 2
            for e in ocupados:
                info = []
                info = info + data[l].split('*')
                info[1] = info[1].rstrip('\n')
                u = self.buscarUsuario(int(info[1]))
                if u is not None:
                    self.parqueaderos[p].parqueo(u,p,e,True)
                    self.parqueaderos[p].espacios[e].tiempoInicio = int(info[0])
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
        
        n = len(data)

        self.usuarios = dt.HashMap(int(1.12*n))
        self.nicknames = dt.StringHashMap(int(1.12*n),self.nicknames.L)
        self.placas = dt.StringHashMap(int(1.12*n),self.placas.L)

        for i in range(n):
            self.addUsuarioArr(data[i].rstrip('\n').split("*"),True)

    def addUsuarioArr(self,info,verified):
        if len(info) < 8: return None
        if not verified:
            check = self.checkInfoUsuario(info)
            if check < 3: return check

        line = '*'.join(info)

        for i in range(len(info),10): info.append(None)

        self.usuarios.add(int(info[0]),Usuario(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10]))
        self.nicknames.add(info[1],int(info[0]))
        self.placas.add(info[6],int(info[0]))
        
        if not verified:
            with open(self.usuariosRoute,"a") as f:
                f.writelines(line+'\n')

        return 3
    
    def checkCambioInfo(self,info,oldCed):
        if int(info[0]) == oldCed:
            if self.nicknames.get(info[1]) is not None and self.usuarios.get(int(info[0])).nickname != info[1]: return 1
            elif self.placas.get(info[6]) is not None and self.usuarios.get(int(info[0])).carro.placa != info[6]: return 2
        else:
            if self.usuarios.get(int(info[0])) is not None: return 0
            u = self.usuarios.get(int(info[0]))
            if self.nicknames.get(info[1]) is not None and self.usuarios.get(self.nicknames.get(info[1])).nickname != info[1]: return 1
            elif self.placas.get(info[6]) is not None and self.usuarios.get(self.placas.get(info[6])).carro.placa != info[6]: return 2
        return 3

    def cambioInfo(self,info,oldCed):
        print(oldCed)

        check = self.checkCambioInfo(info,oldCed)
        if check < 3: return check

        line = '*'.join(info)

        with open(self.usuariosRoute,"r") as f:
            data = f.readlines()

        found = False
        for i,l in enumerate(data):
            if l.split("*")[0] == str(oldCed):
                found = True
                data[i] = line+'\n'
                with open(self.usuariosRoute,"w") as f:
                    f.writelines("".join(data))
        if not found: return
        
        if info[0] != str(oldCed):
            self.usuarios.add(int(info[0]),Usuario(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9]))
            self.nicknames.delete(self.usuarios.get(oldCed).nickname)
            self.nicknames.add(info[1],int(info[0]))
            self.placas.delete(self.usuarios.get(oldCed).carro.placa)
            self.placas.add(info[6],int(info[0]))
            self.usuarios.delete(oldCed)
        else:
            if self.usuarios.get(oldCed).nickname != info[1]:
                self.nicknames.delete(self.usuarios.get(oldCed).nickname)
                self.usuarios.get(oldCed).nickname = info[1]
                self.nicknames.add(info[1],oldCed)
            if self.usuarios.get(oldCed).carro.placa != info[6]:
                self.placas.delete(self.usuarios.get(oldCed).carro.placa)
                self.usuarios.get(oldCed).carro.placa = info[6]
                self.placas.add(info[6],oldCed)

        return 3

    def checkInfoUsuario(self,info):
        if self.usuarios.get(int(info[0])) is not None: return 0
        elif self.nicknames.get(info[1]) is not None: return 1
        elif self.placas.get(info[6]) is not None: return 2
        return 3
    
    def checkLogin(self,nickname,password):
        c = self.nicknames.get(nickname)
        if c is None: return -2
        u = self.usuarios.get(c)
        if u is None: return -2
        if u.password != password: return -1
        return u
    
    def buscarEmpleado(self,ced):
        for e in self.empleados:
            if ced == e.ced:
                return e
        return None
           
    def addEmpleados(self):
        with open(self.empleadosRoute,"r") as f:
            data = f.readlines()
        
        self.empleados = dt.StringHashMap(max(10,len(data)),self.empleados.L)

        for line in data:
            line = line.rstrip('\n')
            self.addEmpleadoArr(line.split("*"),True)

    def addEmpleadoArr(self,info,verified):
        if len(info) < 3: return None
        if not verified:
            check = self.checkInfoEmpleado(info)
            if check < 3: return check

        line = '*'.join(info)

        self.empleados.add(info[0],Empleado(info[0],info[1],info[2]))
        
        if not verified:
            with open(self.empleadosRoute,"a") as f:
                if len(self.empleados) > 1: f.write('\n')
                f.writelines(line)

        return 3
    
    def checkLoginEmpleado(self,nickname,password):
        e = self.empleados.get(nickname)
        if e is None: return "-2"
        elif e.password == password: return e
        return "-1"

    def checkInfoEmpleado(self,info):
        if self.empleados.get(int(info[0])) is not None: return 0
        elif self.empNicknames.get(info[1]): return 1
        return 3

    def buscarUsuario(self,ced):
        return self.usuarios.get(ced)
    
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

        self.parqueaderosRoute = "parqueaderos"

    def parqueo(self,user,inP,e,verified):
        if user is not None and user.carro is not None and not user.carro.enParqueo:
            self.espacios[e] = Espacio(e,int(time.time()), user.carro,False)
            self.espaciosTree.root = self.espaciosTree.insert(e,self.espaciosTree.root)
            user.carro.enParqueo = True
            user.carro.esp = (self.cod,inP,e)
            if not verified:
                with open(self.parqueaderosRoute+"/p"+str(inP),"r") as f:
                    data = f.readlines()
                data[1]=data[1][0:e]+"1"+data[1][e+1:]
                data.append(str(int(time.time()))+"*"+user.ced+"\n")
                with open(self.parqueaderosRoute+"/p"+str(inP),"w") as f:   
                    f.write("".join(data))

            self.ocupados += 1

            return True

        return False

    def desparqueo(self,user,inP):
        if user is not None and user.carro is not None and user.carro.enParqueo:
            inE = user.carro.esp[2]
            self.espacios[inE] = None
            self.espaciosTree.remove(inE,self.espaciosTree.root)
            user.carro.enParqueo = False
            user.carro.esp = None
            with open(self.parqueaderosRoute+"/p"+str(inP),"r") as f:
                data = f.readlines()
            
            data[1]=data[1][0:inE]+"0"+data[1][inE+1:]
            data.pop(data[1].count("1",0,inE)+2)
            with open(self.parqueaderosRoute+"/p"+str(inP),"w") as f:
                f.write("".join(data)) 

            self.ocupados -= 1          

    def vaciar(self,inP):
        self.espaciosTree.makeEmpty()
        self.espacios = [None]*self.totales
        self.ocupados = 0
        data = [self.nombre,self.cod,self.direccion,self.tel,self.gerente,str(self.totales),str(self.ocupados)]
        data = "*".join(data) + "\n"
        data += "0"*self.totales + "\n"
        with open(self.parqueaderosRoute+"/p"+str(inP),"w") as f:
            f.write(data)

def main():
    ep = EasyParking()

if __name__ == "__main__":
    main()
    
