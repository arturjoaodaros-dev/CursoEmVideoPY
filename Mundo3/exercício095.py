ls = []
while True:
    Jogador = {}
    Jogador["Nome"] = str(input("digite o nome do jogador: "))
    Jogador["Idade"] = int(input("digite a idade do jogador: "))
    Jogador["Aproveitamento"] = []
    p = int(input("digite o total de partidas jogadas: "))
    for i in range(1, p + 1):
        g = int(input(f"digite quantos gols marcou na {i}° partida: "))
        Jogador["Aproveitamento"].append(g)
    Jogador["TotalDeGolsNoCampeonato"] = sum(Jogador["Aproveitamento"])
    ls.append(Jogador)
    ask = str(input("quer continuar[S/N]: "))
    if ask == "n":
        break
    elif ask != "s":
        ask = str(input("Insira uma opção valida[S/N]: "))
print("ID  NOME   APROVEITAMENTO   TOTAL")
for id, it in enumerate(ls):
    print(
        f"{id:<4}{it['Nome']:^4}   {it['Aproveitamento']}{sum(it['Aproveitamento']):>4}"
    )
while True:
    ps = 0
    ask = int(input("mostrar dados de qual jogador[ID, 999 para sair]: "))
    if ask == 999:
        break
    for its in ls:
        try:
            if its == ls[ask]:
                ps += 1
                for i, v in enumerate(its["Aproveitamento"]):
                    print(f"na partida {i + 1}, ele marcou {v} gols")
        except:
            if IndexError:
                print("Jogador não encontrado")
    if ps != 1:
        print("Jogador não encontrado")
    else:
        ps = 0
