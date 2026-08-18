pessoas = []
while True:
    Nome = str(input("digite o nome da pessoa: "))
    Peso = float(input("digite o peso da pessoa: "))
    ls = [Nome, Peso]
    pessoas.append(ls)
    Pergunta = str(input("gostaria de ir novamente [S/N]: ")).lower()
    if Pergunta == "n":
        break
    elif Pergunta == "s":
        """ nada acontece"""
    else:
        Pergunta = str(input("Insira um valor valido [S/N]: ")).lower()
print(f"ao todo, você cadastrou {len(pessoas)} pessoas")
pesos = [0]
for p in pessoas:
    if p[1] > max(pesos):
        pesos = []
        pesos.append(p[1])
    elif p[1] == max(pesos):
        pesos.append(p[1])
menores = [0]
for p in pessoas:
    if p[1] < min(menores) or min(menores) == 0:
        menores = []
        menores.append(p[1])
    elif p[1] == min(menores):
        menores.append(p[1])
if len(pesos) >= 2:
    for p in pessoas:
        if p[1] == pesos[0]:
            print(f"o MAIOR peso é de {pesos[0]}, peso de", end=" ")
    for p in pessoas:
        if p[1] == pesos[0]:
            print(p[0], end=", ")
if len(menores) >= 2:
    for p in pessoas:
        if p[1] == menores[0]:
            print(f"o MENOR peso é de {menores[0]}, peso de", end=" ")
            break
    for p in pessoas:
        if p[1] == menores[0]:
            print(p[0], end=", ")
