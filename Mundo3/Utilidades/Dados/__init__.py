try:
    from ..Moeda import *
except ImportError:
    import os
    import sys

    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from CursoEmVideo.Mundo3.Utilidades.Moeda import *


def sumarize(i, p=10, c=10):
    return (
        "\n----------------resumo do valor-------------\n"
        f"preço analizado: {moeda(i):^30}\n"
        f"Dobro do preço: {dobro(i, formated=True)[0]:^30}\n"
        f"Metade do preço: {metade(i, formated=True)[0]:^30}\n"
        f"{p}% de aumento: {aumento(p, i, formated=True)[0]:^30}\n"
        f"{c}% de redução: {reduzir(c, i, formated=True)[0]:^30}"
    )


def leiadinheiro(texto):
    m = input("digite o valor: R$")
    m = m.replace(",", ".")
    return float(m)
