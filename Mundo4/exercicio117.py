from rich import *
from rich.table import *


class product:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def ShowTable(self):
        t = Table(title_justify="full", title="tabela de teste")
        t.add_column("nome")
        t.add_column("preço")
        t.add_row("lapis", "12.5")
        print(t)


p = product("arroz", 12.50)
p.ShowTable()
