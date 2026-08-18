import random
import time

dic = {}
ls = [0, 0, 0, 0]
for p in range(1, 5):  # imprime o dicionário
    j = random.randint(1, 6)
    print(f"o jogador {p} tirou {j}")
    time.sleep(1)
    dic[str(p)] = j
for i in range(4):
    for k, v in dic.items():
        if v == sorted(dic.values())[3] and ls[0] == 0:
            ls[0] += int(k)
        elif v == sorted(dic.values())[2] and ls[1] == 0:
            ls[1] += int(k)
        elif v == sorted(dic.values())[1] and ls[2] == 0:
            ls[2] += int(k)
        elif v == sorted(dic.values())[0] and ls[3] == 0:
            ls[3] += int(k)
        elif v == sorted(dic.values())[3] and ls[1] == 0:
            ls[1] += int(k)
        elif v == sorted(dic.values())[2] and ls[2] == 0:
            ls[2] += int(k)
        elif v == sorted(dic.values())[1] and ls[3] == 0:
            ls[3] += int(k)
for i in range(1, 5):
    print(f"{i}° lugar: jogador {ls[i - 1]}")
