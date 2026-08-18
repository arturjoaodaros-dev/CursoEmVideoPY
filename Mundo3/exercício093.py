Jogador = {}
Jogador["Nome"] = str(input("digite o nome do jogador: "))
Jogador["Idade"] = int(input("digite a idade do jogador: "))
Jogador["Aproveitamento"] = []
p = int(input("digite o total de partidas jogadas: "))
for i in range(1, p + 1):
    g = int(input(f"digite quantos gols marcou na {i}° partida: "))
    Jogador["Aproveitamento"].append(g)
Jogador["TotalDeGolsNoCampeonato"] = sum(Jogador["Aproveitamento"])
print("=-" * 30)
print(Jogador)
print("=-" * 30)
for k, v in Jogador.items():
    print(f"{k} = {v}")
print("=-" * 30)
print(f"o jogador {Jogador['Nome']} jogou {p} partidas")
for i, v in enumerate(Jogador["Aproveitamento"]):
    print(f"na partida {i + 1}, ele marcou {v} gols")
print(f"foi um total de {sum(Jogador['Aproveitamento'])} gols")
