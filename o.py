from nodo import Nodo

class Lista:
    __comienzo: Nodo
    def __init__(self):
        self.__comienzo=None
    def agregarProfesor(self, profesor):
        nodo = Nodo(profesor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
    def listarDatosProfesores(self):
        aux = self.__comienzo
        while aux!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()
    def eliminarPorDNI(self, dni):
        aux=self.__comienzo
        encontrado = False
        if aux.getDato().getDNI()==dni:
            encontrado=True
            print('Encontrado:'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente()
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if aux.getDato().getDNI()==dni:
                    encontrado=True
                else:
                    ant = aux
                    aux=aux.getSiguiente()
            if encontrado:
                print('Encontrado:'+str(aux.getDato()))
                ant.setSiguiente(aux.getSiguiente())
            else:
                print('El DNI {}, no está en la lista'.format(dni))


    class Lista:
        __comienzo: Nodo
        __actual: Nodo
        __indice: int
        __tope: int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    
    def agregarProfesor(self, profesor):
        nodo = Nodo(profesor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def eliminarPorDNI(self, dni):
        aux=self.__comienzo
        encontrado = False
        if aux.getDato().getDNI()==dni:
            encontrado=True
            print('Encontrado y eliminado:\n'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente()
            self.__tope-=1
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if aux.getDato().getDNI()==dni:
                    encontrado=True
                else:
                    ant = aux
                    aux=aux.getSiguiente()
            if encontrado:
                print('Encontrado y eliminado:\n'+str(aux.getDato()))
                ant.setSiguiente(aux.getSiguiente())
                self.__tope-=1
                del aux
            else:
                print('El DNI {}, no está en la lista'.format(dni))