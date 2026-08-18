from abc import ABC, abstractmethod


class Person(ABC):  # superclasse
    def __init__(self, nome="", idade=""):
        self.nome = nome
        self.idade = idade

    def aniversário(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


c = Person(
    "artur", 12
)  # TypeError: Can't instantiate abstract class Person without an implementation for abstract method 'estudar'


class professor(Person):  # tipo E1
    def __init__(self, nome, idade, esp="", exp=0):
        super().__init__(nome, idade)
        self.especialidade = esp
        self.experiencia = exp

    def dar_aula(self):
        pass

    def estudar(self):
        print(
            f"{self.nome} está estudando {self.especialidade} para dar aulas com mais qualidade"
        )  # OBRIGATOÓRIO


class Aluno(Person):  # subclasse
    def __init__(self, nome, idade, cur="", tur=""):
        super().__init__(nome, idade)  # herança
        self.curso = cur
        self.turma = tur

    def assistir_aula():
        pass

    def estudar(self):
        print(
            f"{self.nome} está estudando {self.curso} para ir bem nas provas"
        )  # OBRIGATOÓRIO


al = Aluno("artur", 12, "matematica", "7°H")
al.estudar()
