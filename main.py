import os
from Menu import Menu
from listaVehiculos import ListaVehiculos
from objectEncoder import ObjectEncoder

if __name__ == '__main__':
    lv = ListaVehiculos()
    oe = ObjectEncoder()
    bandera = False
    os.system('cls')
    menu = Menu()
    while not bandera:
        menu.mostrarMenu()
        opcion = int (input("Su opcion: "))
        menu.opcion(opcion, lv, oe)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')