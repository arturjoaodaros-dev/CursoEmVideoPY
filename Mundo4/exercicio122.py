import rich.panel as pn
from rich import *


class ControleRemoto:
    def __init__(self, canal, volume, estado=True):
        self.canal = canal
        self.volume = volume
        self.estado = estado
        self.select = "12345"

    def LigaDesliga(self):
        if self.estado:
            self.estado = False
        else:
            self.estado = True
        while True:
            c = pn.Panel(
                f"""Canal: {self.select}
Volume: {"[green on green] [/green on green]" * self.volume}{"[red on red] [/red on red]" * (5 - self.volume)}""",
                title=f"TV: {self.estado}",
            )
            print(c)
            c = str(
                input("trocar canal: <>, Mudar volume: +-, desligar/ligar TV: @ >>>: ")
            )
            if c == "@":
                self.LigaDesliga()
            if c == 0 or str(0):
                import sys

                sys.exit(0)
            if self.estado:
                if c == ">":
                    self.SUM("mais")
                    self.ReturnStateOfChannel()
                elif c == "<":
                    self.SUM("menos")
                    self.ReturnStateOfChannel()
                elif c == "+":
                    self.Volume("mais")
                elif c == "-":
                    self.Volume("menos")

    def SUM(self, c):
        if c.lower() == "menos" and self.canal != 0:
            self.canal -= 1
        elif c.lower() == "menos":
            self.canal += 5
        elif c.lower() == "mais" and self.canal != 5:
            self.canal += 1
        elif c.lower() == "mais":
            self.canal -= 4

    def Volume(self, v):
        if v == "mais" and self.volume != 5:
            self.volume += 1
        elif v == "menos" and self.volume != 1:
            self.volume -= 1

    def ReturnStateOfChannel(self):
        st = ""
        for i in self.select:
            if i == str(self.canal):
                st += f"[yellow]{i}[/yellow]"
            elif i.isnumeric():
                st += i
        self.select = st
        print(st)


c = ControleRemoto(3, 5)
c.LigaDesliga()
