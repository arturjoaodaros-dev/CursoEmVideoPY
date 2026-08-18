class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self.nota = nota


class AvaliacaoSegura:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self._disciplina = disciplina
        self._nota = nota

    def ViewGrade(self):
        print(self._nota, self._disciplina)


av1 = Avaliacao("joaozinho", "matematica", 7)
av1.nota = -234
from rich import *

inspect(av1, private=True)

av2 = AvaliacaoSegura("joaozinho", "matematica", 7)
av2.nota = -234
inspect(av2, private=True)
av2.ViewGrade()


class AvaliacaoSetter:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self._disciplina = disciplina
        self._nota = nota

    @property
    def nota(self):  # getter
        return self._nota

    @nota.setter
    def nota(self, valor):  # setter
        if valor >= 0 and valor <= 10:
            self._nota = valor
        else:
            raise UserWarning(
                """não é possivel colocar notas negativas ou acima de 10"""
            )
