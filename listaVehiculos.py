from datetime import datetime
from vehiculo import Vehiculo
from nodo import Nodo
from coleccion import IColeccion

class ListaVehiculos (IColeccion):
    __comienzo: Nodo
    __actual: Nodo
    __indice = 0
    __top = 0

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None

    def __str__(self) -> str:
        for vehiculo in self:
            print (vehiculo)

    def __iter__ (self):
        self.__actual = self.__comienzo
        return self

    def __next__ (self):
        if self.__actual is None or self.__indice == self.__top:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def buscarAnterior (self, i):
        nodoAnterior = self.__comienzo
        while self.__indice < i:
                nodoAnterior = nodoAnterior.getSiguiente()
                self.__indice += 1
        return nodoAnterior

    def agregarElemento(self, vehiculo):
        nodo = Nodo (vehiculo)
        nodo.setSiguiente (self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__top += 1


    def insertarElemento(self, vehiculo, posicion):
        if posicion < 0 or posicion > self.__top:
            raise ValueError ('Posición inválida')
        if posicion == 0:
            self.agregarElemento(vehiculo)
        else:
            self.__indice = 0
            nodoAnterior = self.buscarAnterior(posicion)
            nodoNuevo = Nodo(vehiculo)
            sig = nodoAnterior.getSiguiente()
            nodoNuevo.setSiguiente(sig)
            nodoAnterior.setSiguiente(nodoNuevo)
            self.__actual = nodoNuevo
            self.__top += 1
            print ('Se agregó el vehiculo')
            self.__indice = 0

    def mostrarElemento (self, index):
        if index < 0 or index > self.__top:
            raise ValueError ('Posicion invalida')
        if index == 0:
            print (str (self.__comienzo))
        else:
            for dato in self:
                if self.__indice == index:
                    print (f'Tipo de objeto: {type(dato)}')

    def calcularPrecioVentaUsado (self, vehiculo):
        currentDateTime = datetime.now()
        fecha = currentDateTime.date()
        año = int (fecha.strftime("%Y"))
        antiguedad = año - vehiculo.getAño()
        km = 0
        if vehiculo.getKm() > 100000:
            km = 2 * vehiculo.getPrecioBase() / 100
        return int (vehiculo.getPrecioBase() - (antiguedad * vehiculo.getPrecioBase() / 100) - km)

    def calcularPrecioVentaNuevo (self, vehiculo):
        pat = 10 * vehiculo.getPrecioBase() / 100
        full = 0
        if vehiculo.getVersion() == 'full':
            full += 2 * vehiculo.getPrecioBase() / 100
        return int (vehiculo.getPrecioBase() + pat + full)

    def VentaPatente (self, patente): # Obtener Precio venta por patente
        aux = self.__comienzo
        flag = False
        if aux.getDato().__class__.__name__ == 'Usado' and aux.getDato().getPatente() == patente:
            flag = True
            precio = self.calcularPrecioVentaUsado(aux.getDato())
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not flag and aux != None:
                if aux.getDato().__class__.__name__ == 'Usado' and aux.getDato().getPatente() == patente:
                    flag = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            if not flag:
                raise ValueError ('Patente no encontrada')
            else: 
                precio = self.calcularPrecioVentaUsado(aux.getDato())
                aux.getDato().setPrecioBase(precio)
        return precio

    def buscarBarato(self):
        min = 999999999999
        for dato in self:
            if dato.__class__.__name__ == 'Usado':
                precio = self.calcularPrecioVentaUsado(dato)
            else: precio = self.calcularPrecioVentaNuevo(dato)
            if precio < min:
                min = precio
                barato = dato
        print ('El precio mas barado de ${min}, es del vehiculo: ')
        return barato

    def mostrarVehiculos (self):
        for dato in self:
            print (f'''
Modelo: {dato.getModelo()}
Cantidad de puertas: {dato.getCantidadPuertas()}''')
            if dato.__class__.__name__ == 'Usado':
                print (f'Importe de venta: ${self.calcularPrecioVentaUsado(dato)}')
            else: print (f'Importe de venta: ${self.calcularPrecioVentaNuevo(dato)}')

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=[vehiculo.toJSON() for vehiculo in self]
            )
        return d