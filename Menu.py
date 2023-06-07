import os
from usado import Usado
from nuevo import Nuevo
from listaVehiculos import ListaVehiculos

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            5: self.opc5,
                            6: self.opc6,
                            7: self.opc7,
                            8: self.opc8,
                            99: self.mostrar,
                            0: self.salir
                        }
        
    def opcion(self,op, lv, oe):
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4 or op == 5 or op == 6 or op ==7 or op ==8  or op == 99:
            func(lv, oe)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Cargar un vehiculo
-> 2: Guardar vehiculos en archivo
-> 3: Cargar datos de vehiculos
-> 4: Insertar un vehículo
-> 5: Ver tipo de objeto en una ubicacion
-> 6: Mostrar el precio de venta por patente.
-> 7: Mostrar todos los datos del vehiculo mas barato
-> 8: Ver modelo, cantidad de puertas e importe de venta.

-> 0: Salir del programa""")

## OPCIONES

    def opc1 (self, lv, oe):
        os.system('cls')
        print ('---------->Agregar Vehiculo<----------')
        print ('''
El vehiculo es usado? 
-> 1: si 
-> 2: no''')
        op = int (input ('Su opcion: '))
        if op == 1:
            os.system('cls')
            print ('---------->Vehiculo Usado<----------\n')
            mod = input ('Ingrese modelo: ')
            cantP = int (input ('Ingrese cantidad de puertas: '))
            color = input ('Ingrese color del vehiculo: ')
            precioBase = int (input ('Ingrese precio base: '))
            pat = input ('Ingrese la patente: ')
            km = int (input ('Ingrese los kilometros del vehiculo: '))
            año = int (input ('Ingrese año del vehiculo: '))
            xUsado = Usado (mod, cantP, color, precioBase, pat.upper(), km, año)
            lv.agregarElemento (xUsado)
        elif op == 2:
            os.system('cls')
            print ('---------->Vehiculo Nuevo<----------\n')
            mod = input ('Ingrese modelo: ')
            cantP = int (input ('Ingrese cantidad de puertas: '))
            color = input ('Ingrese color del vehiculo: ')
            precioBase = int (input ('Ingrese precio base: '))
            ver = input ('Ingrese version del vehiculo (base - full): ')
            xNuevo = Nuevo (mod, cantP, color, precioBase, ver.lower())
            lv.agregarElemento (xNuevo)
        else: 
            print ('Opcion elegida incorrecta, vuelva a intentar')
            self.opc1(lv)

    def opc2 (self, lv, oe):
        os.system('cls')
        d = lv.toJSON ()
        oe.guardarJSONArchivo (d, 'Vehiculos.json')

    def opc3 (self, lv, oe):
        os.system('cls')
        dic = oe.leerJSONArchivo ('Vehiculos.json')
        lv = oe.decodificarDiccionario (dic, lv)

    def opc4 (self, lv, oe):
        os.system('cls')
        print ('---------->Agregar Vehiculo<----------')
        print ('''
El vehiculo es usado? 
-> 1: si 
-> 2: no''')
        op = int (input ('Su opcion: '))
        if op == 1:
            os.system('cls')
            print ('---------->Vehiculo Usado<----------\n')
            mod = input ('Ingrese modelo: ')
            cantP = int (input ('Ingrese cantidad de puertas: '))
            color = input ('Ingrese color del vehiculo: ')
            precioBase = int (input ('Ingrese precio base: '))
            pat = input ('Ingrese la patente: ')
            km = int (input ('Ingrese los kilometros del vehiculo: '))
            año = int (input ('Ingrese año del vehiculo: '))
            xVehiculo = Usado (mod, cantP, color, precioBase, pat.upper(), km, año)
        elif op == 2:
            os.system('cls')
            print ('---------->Vehiculo Nuevo<----------\n')
            mod = input ('Ingrese modelo: ')
            cantP = int (input ('Ingrese cantidad de puertas: '))
            color = input ('Ingrese color del vehiculo: ')
            precioBase = int (input ('Ingrese precio base: '))
            ver = input ('Ingrese version del vehiculo (base - full): ')
            xVehiculo = Nuevo (mod, cantP, color, precioBase, ver.lower())
        else: 
            print ('Opcion elegida incorrecta, vuelva a intentar')
            self.opc4(lv)
        index = int (input ('Indique posicion para insertar vehiculo: '))
        lv.insertarElemento(xVehiculo, index-1)

    def opc5 (self, lv, oe):
        os.system('cls')
        print ('---------->Ver vehiculo en una posicion<----------')
        index = int (input ('Ingrese la posicion: '))
        lv.mostrarElemento(index+1)

    def opc6 (self, lv, oe):
        os.system('cls')
        print ('---------->Ver precio de venta<----------')
        patente = input ('Ingrese la patente del vehiculo: ')
        print (patente.upper())
        precio = lv.VentaPatente(patente.upper())
        print (f'Precio de venta del vehiculo: ${precio}')

    def opc7 (self, lv, oe):
        os.system('cls')
        print ('---------->Vehiculo mas barato<----------')
        vehiculo = lv.buscarBarato()
        print (str (vehiculo))

    def opc8 (self, lv, oe):
        os.system('cls')
        print ('---------->Vehiculos<----------')
        lv.mostrarVehiculos()

    def mostrar (self, lv, oe):
        for dato in lv:
            print (dato)

    def salir (self):
        print ('saliendo...')