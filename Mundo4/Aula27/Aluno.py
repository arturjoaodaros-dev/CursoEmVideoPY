from Person import *


class Aluno(Person):  # subclasse
    def __init__(self, nome, idade, cur="", tur=""):
        super().__init__(nome, idade)  # herança
        self.curso = cur
        self.turma = tur

    def assistir_aula():
        pass
