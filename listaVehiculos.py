from vehiculo import Vehiculo
from nodo import Nodo
from coleccion import IColeccion

class ListaVehiculos (IColeccion):
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __top: int

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__top = 0
        self.__indice = 0

    def __str__(self) -> str:
        for vehiculo in self:
            print (vehiculo)

    def __iter__ (self):
        return self

    def __next__ (self):
        if self.__indice == self.__top:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, vehiculo):
        nodo = Nodo (vehiculo)
        nodo.setSiguiente (self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__top += 1

    def insertarElemento(self, vehiculo, posicion):
        aux = self.__comienzo
        encontrado = False
        self.__indice = 0
        if self.__indice == posicion:
            encontrado = True
            self.agregarElemento(vehiculo)
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if self.__indice == posicion:
                    encontrado = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            if encontrado:
                print ('Se agregó el Vehiculo')
                self.agregarElemento(vehiculo)
            else: print ('La posicion no existe')


    def mostrarElemento(self, posicion):
        ''

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=[vehiculo.toJSON() for vehiculo in self]
            )
        return d