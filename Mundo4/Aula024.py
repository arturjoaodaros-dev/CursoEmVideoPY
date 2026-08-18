class Artur:
    def __init__(self):  # metodo construtor
        self.nome = "Artur"
        self.idade = 12
        self.sobrenome = "daros"
        self.HabilidadePrincipal = "programar"

    def aniversario(self):
        self.idade += 1

    def summarize(self):
        return f"o usuário {self.nome} tem {self.idade} e tem como habilidade principal {self.HabilidadePrincipal}"


c = Artur()
print(c.summarize())
c.HabilidadePrincipal = "calcular"
print(c.summarize())
c.aniversario()
print(c.summarize())
c2 = Artur()
c.nome = "plinio"
c.idade = 18
c.HabilidadePrincipal = "falar"
print(c2.summarize())
c3 = Artur()
print(c3.summarize)
