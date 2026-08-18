import math
from abc import *


class Poligono(ABC):
    def __init__(self, lados):
        self.lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio**2


class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__(lados)
        self.lado = lados

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado**4


c = Circulo(20)
print(c.area())
print(c.perimetro())
d = Quadrado(20)
print(d.area())
print(d.perimetro())
