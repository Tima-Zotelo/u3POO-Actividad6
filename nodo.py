from vehiculo import Vehiculo

class Nodo:
    __vehiculo: Vehiculo
    __siguiente: object

    def __init__(self, veh):
        self.__vehiculo = veh
        self.__siguiente=None

    def __str__(self) -> str:
        return str (self.__siguiente)

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__vehiculo