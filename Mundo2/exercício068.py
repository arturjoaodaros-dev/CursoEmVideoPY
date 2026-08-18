import random

v = 0
while True:
    h = int(input("digite um numero inteiro (1-10): "))
    c = random.randint(1, 10)
    ask = str(input("par ou impar[P/I]: ")).lower()
    if (h + c) % 2 == 0 and ask == "p":
        print("ganhou")
        v += 1
    else:
        print(f"perdeu, eu coloquei {c}, você teve {v} vitórias consecutivas")
        break
