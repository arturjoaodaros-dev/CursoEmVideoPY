from Person import *


class Funcionario(Person):
    def __init__(self, nome, idade, car="", set=""):
        super().__init__(nome, idade)
        self.cargo = ""
        self.setor = ""

    def bater_ponto(self):
        pass
