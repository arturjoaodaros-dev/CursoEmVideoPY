import random

try:
    n = random.randint(0, 10)
    i = int(input("tente adivinhar o numero que estou pensando: "))
    t = 0
    while n != i:
        print("tente novamente")
        i = int(input("tente adivinhar o numero que estou pensando: "))
        t += 1
    print("parabens era este")
    print(f"você precisou de somente {t} tentativas para vencer")
except:
    print("algo de errado aconteceu")
