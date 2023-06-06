from vehiculo import Vehiculo

class Nuevo (Vehiculo):
    __version: str

    def __init__(self, mod, cantPuertas, color, precioBase, version) -> None:
        super().__init__(mod, cantPuertas, color, precioBase)
        self.__version = version

    def __str__(self) -> str:
        s = f'Modelo: {super().getModelo()}, Cant. de puertas: {super().getCantidadPuertas()}, Color: {super().getColor()}, precio base: {super().getPrecioBase()}, version: {self.__version}'
        return s

    def getVersion (self):
        return self.__version