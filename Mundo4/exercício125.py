from abc import *


class Veiculos(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def CalcularFrete(self):
        pass


class Moto(Veiculos):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.5

    def CalcularFrete(self):
        return self.fator * self.distancia


class Drone(Veiculos):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.5

    def CalcularFrete(self):
        if self.distancia <= 10:
            return self.distancia * self.fator


class caminhão(Veiculos):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.2

    def CalcularFrete(self):
        if self.distancia <= 10:
            return self.distancia * self.fator


e = Drone(20)
print(e.CalcularFrete())
