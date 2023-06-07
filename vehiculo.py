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

    def setPB (self, precio):
        self.__precioBase = precio

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