from abc import ABC, abstractmethod

class InstrumentosMusicales(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def descripcion(self):
        pass

class Trompeta(InstrumentosMusicales):
    def __init__(self, nombre, precio, tipo_trompeta):
        super().__init__(nombre, precio)
        self.tipo_trompeta = tipo_trompeta

    def descripcion(self):
        res = (f"La trompeta {self.nombre} es del tipo {self.tipo_trompeta}. Su precio es {self.precio}.")
        return res

class Piano(InstrumentosMusicales):
    def __init__(self, nombre, precio, marca):
        super().__init__(nombre, precio)
        self.marca = marca

    def descripcion(self):
        res = (f"El piano {self.nombre} es de la marca {self.marca}. Su precio es {self.precio}.")
        return res

class Violin(InstrumentosMusicales):
    def __init__(self, nombre, precio, tipo_violin):
        super().__init__(nombre, precio)
        self.tipo_violin = tipo_violin

    def descripcion(self):
        res = (f"El violín {self.nombre} es del tipo {self.tipo_violin}. Su precio es {self.precio}.")
        return res