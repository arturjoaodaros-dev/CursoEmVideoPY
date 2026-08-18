from rich import *
from rich.panel import *


class Funcionário:
    def __init__(self, Nome, Setor, Cargo):
        self.nome = Nome
        self.setor = Setor
        self.cargo = Cargo

    def present(self, ShowBox=False):
        if not ShowBox:
            return f"Olá, sou {self.nome}, trabalho no setor {self.setor} como {self.cargo}"
        else:
            print(
                Panel(
                    f"[white]Olá, sou {self.nome}, trabalho no setor {self.setor} como {self.cargo}[/white]",
                    title="Funcionário",
                    style="red",
                )
            )


c = Funcionário("Artur", "tecnologia", "backend")
c.present(ShowBox=True)
