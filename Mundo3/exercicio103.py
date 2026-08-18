def ficha(n="<desconhecido>", g=0):
    return f"o jogador {n} fez {g} gol(s) no compeonato"


ficha(
    str(input("digite o nome do jogador: ")),
    input("quantos gols ele fez no campeonato? "),
)
