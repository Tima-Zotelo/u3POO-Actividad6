'''
De cada vehículo desea registrar el modelo (ej. Palio, Focus, etc.), cantidad de puertas, color y el precio base de venta. 
Los vehículos nuevos son de una misma marca, en cambio los usados pueden ser de cualquier marca, por ello este también es un dato que debe registrar.

Además, para los usados se registrará la patente, el año y el kilometraje.

De un vehículo nuevo también registra la versión (base o full).
'''
class Vehiculo:
    __modelo: str
    __cantPuertas: int
    __color: str
    __precioBase: int

    def __init__(self, mod, cantPuertas, color, precioBase) -> None:
        self.__modelo = mod
        self.__cantPuertas = cantPuertas
        self.__color = color
        self.__precioBase = precioBase

    def getModelo (self):
        return self.__modelo

    def getCantidadPuertas (self):
        return self.__cantPuertas

    def getColor (self):
        return self.__color

    def getPrecioBase (self):
        return self.__precioBase

    def toJSON(self):
        if self.__class__.__name__ == 'Usado':
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    mod = self.__modelo,
                    cantPuertas = self.__cantPuertas,
                    color = self.__color,
                    precioBase = self.__precioBase,
                    patente = self.getPatente(),
                    km = self.getKm(),
                    año = self.getAño()
                )   
            )
        else:
            d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                    mod = self.__modelo,
                    cantPuertas = self.__cantPuertas,
                    color = self.__color,
                    precioBase = self.__precioBase,
                    version = self.getVersion()
                )   
            )
        return d