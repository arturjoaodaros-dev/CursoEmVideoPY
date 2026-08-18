import random
import time

ls = []
ask = int(input("quantos jogos você quer que a maqina sorteie: "))
for i in range(1, ask + 1):
    for it in range(6):
        g = random.randint(1, 60)
        if g not in ls:
            ls.append(g)
        else:
            ls.append(".")
    print(f"{i}° jogo ", ls)
    ls = []
    time.sleep(1)
