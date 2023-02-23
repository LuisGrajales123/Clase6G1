class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=0
        self.__fecha_ingreso=" "
        self.__medicamento=""

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarMedicamento(self,n):
        self.__medicamento = n         

class sistemaV:
    def __init__(self):
        self.__lista_canino={}
        self.__lista_felino={}    

    def verificarIngreso(self,historia):
        if historia in self.__lista_canino.keys():
            print("Si se encuentra el canino")
            return True
        elif historia in self.__lista_felino.keys():
            print("Sí se encuentra el felino")
            return True
        else:
            print("Noseencuentra")
            return False

    def verNumeroMascotas(self):
        return len(self.__lista_felino.keys())+len(self.__lista_canino.keys())

    def ingresarCanino(self,mascota):
        if self.verificarIngreso(mascota.verHistoria()):
            return False
        else: 
            self.__lista_canino[mascota.verHistoria()] = mascota
            return True

    def ingresarFelino(self,mascota):
        if self.verificarIngreso(mascota.verHistoria()):
            return False
        else: 
            self.__lista_felino[mascota.verHistoria()] = mascota
            return True


    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.ver_Medicamento() 
        return None

    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                # del self.__lista_mascotas[historia]
                # self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False









        

         
    