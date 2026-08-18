from abc import *


class Funcionario(ABC):
    def __init__(self, nome, SalarioBruto):
        self.nome = nome
        self.SalarioBruto = SalarioBruto
        self.SalarioMinimo = 1612
        self.INSS = 0.935
        self.Legal = False

    @abstractmethod
    def CalcularSalario(self):
        pass

    def AnalizarSalario(self):
        import rich.panel as rp
        from rich import print

        if self.SalarioBruto * self.INSS >= self.SalarioMinimo:
            self.Legal = True
        panel = rp.Panel(
            f"""
Salario Bruto: {self.SalarioBruto}
Salario minimo: {self.SalarioMinimo}
Salario liquido: {self.CalcularSalario()}
Desconto INSS atual: {self.INSS}
salario legalizado: {self.Legal}
Corresponde a {self.CalcularSalario() / self.SalarioMinimo:.2f} salarios minimos""",
            title=f"Salario de {self.nome}",
            style="blue",
        )
        print(panel)


class Horista(Funcionario):
    def __init__(self, nome, Horas, Valor, SalarioBruto=0):
        super().__init__(nome, SalarioBruto)
        self.HorasDeTrabalho = Horas
        self.ValorPorHora = Valor
        self.SalarioBruto = 30 * self.HorasDeTrabalho * self.ValorPorHora

    def CalcularSalario(self):
        return 30 * (self.HorasDeTrabalho * self.ValorPorHora) * self.INSS


class Mensalista(Funcionario):
    def __init__(self, nome, SalarioBruto):
        super().__init__(nome, SalarioBruto)

    def CalcularSalario(self):
        return self.SalarioBruto * self.INSS


m = Mensalista("Artur", 2000)
print(m.CalcularSalario())
m.AnalizarSalario()
h = Horista("Artur", 8, 10)
h.AnalizarSalario()
print(h.CalcularSalario())
