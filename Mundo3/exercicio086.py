linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
count = 1
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
print(" ", linha1, "\n", linha2, "\n", linha3)
