class Artur:
    def __init__(self, n="Artur", i=12, s="daros", h="programar"):  # metodo construtor
        self.nome = n
        self.idade = i
        self.sobrenome = s
        self.HabilidadePrincipal = h

    def aniversario(self):
        self.idade += 1

    def summarize(self):
        return f"o usuário {self.nome} tem {self.idade} e tem como habilidade principal {self.HabilidadePrincipal}"

    def __doc__(self):
        print(
            "contem o formato de formação base de uma pessoa, se nenhum dado é dado, usa como base o mlr dev do mundo"
        )

    def __getstate__(self):
        return f"nome: {self.nome}, idade: {self.idade}, sobrenome: {self.sobrenome}, habilidade principal: {self.HabilidadePrincipal}"


c = Artur("plinio", 17, "cardoso", "falar")
c2 = Artur()
print(c.summarize(), "\n", c2.summarize())
print(c.__doc__)
print(c.__dict__)  # não personalizavel
print(c.__getstate__())  # personalizavel
print(c.__class__)


class ContaBancaria:
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"a conta {self.id} de {self.nome} tem atualmente o saldo de R${self.saldo:,.2f}"

    def depositar(self, v=0):
        self.saldo += v

    def sacar(self, v=0):
        if v < self.saldo * 0.3:
            self.saldo -= v
            print(f"saque DE {v:,.2f} AUTORIZADO PARA A CONTA ID{self.id}")
        else:
            print(f"saque DE {v:,.2f} NEGADO PARA A CONTA ID{self.id}")


cnt = ContaBancaria(183947564, "Artur", 666236984)
print(cnt)
cnt.sacar(999)

# EXTRA:
from rich import *
from rich.panel import *
from rich.table import Table
from rich.traceback import install

install()
print("olá, [red]mundo[/red]! :earth_americas:")
print("olá, [bold red]mundo[/bold red]! :vulcan_salute:")
print("olá, [bold red on white]mundo[/bold red on white]! :vulcan_salute:")
print(":+1::-1:")
box = Panel("esse é um painel de exemplo", title="teste", style="red")
print(box)
t = Table(title_justify="full", title="tabela de teste")
t.add_column("nome")
t.add_column("preço")
t.add_row("lapis", "12.5")
print(t)


def divisao(x, y):
    return x / y


divisao(12, 0)
