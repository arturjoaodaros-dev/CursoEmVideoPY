from Person import *


class professor(Person):  # tipo E1
    def __init__(self, nome, idade, esp="", exp=0):
        super().__init__(nome, idade)
        self.especialidade = esp
        self.experiencia = exp

    def dar_aula(self):
        pass
