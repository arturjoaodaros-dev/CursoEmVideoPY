from rich import *

from Aula27 import *


def main():
    a1 = Aluno("artur", 12, "matematica", "7ºh")
    inspect(a1, methods=True)
    a1.aniversário()
    inspect(a1, methods=True)
    a2 = professor("claudio", 38, "biologia", 44)
    inspect(a2, methods=True)
    a2.aniversário()
    inspect(a2, methods=True)
    if __name__ == "__main__":
        main()
