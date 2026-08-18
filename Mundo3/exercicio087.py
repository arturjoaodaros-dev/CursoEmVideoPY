linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
count = 1
pares = 0
for p in range(3):
    for i in range(3):
        ask = float(input(f"digite um valor para a posição [{p}, {i}]"))
        if count <= 3:
            count += 1
            linha1[i].append(ask)
        elif count <= 6:
            count += 1
            linha2[i].append(ask)
        else:
            count += 1
            linha3[i].append(ask)
print("\n", linha1, "\n", linha2, "\n", linha3)
for it in linha1:
    if it[0] % 2 == 0:
        pares += it[0]
for it in linha2:
    if it[0] % 2 == 0:
        pares += it[0]
for it in linha3:
    if it[0] % 2 == 0:
        pares += it[0]
sm = [linha2[0][0], linha2[0][0], linha2[0][0]]
print(f"a soma dos valores pares são {pares}")
print(
    f"a soma dos itens da coluna 3 é {float(linha1[2][0]) + float(linha2[2][0]) + float(linha3[2][0])}"
)
print(f"o maior valor da linha 2 é {max(sm)}")
