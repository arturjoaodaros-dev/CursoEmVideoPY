class Person:  # superclasse
    def __init__(self, nome="", idade=""):
        self.nome = nome
        self.idade = idade

    def aniversário(self):
        self.idade += 1
