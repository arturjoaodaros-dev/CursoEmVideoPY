for c in range(6):
    print("oi")
print("FIM")
for i in range(6):
    print(i)
print("FIM")
for i in range(0, 7, 2):  # começa no 0, até o 7, indo de 2 em 2
    print(i)
print("FIM")

n = int(input("digite um numero inteiro: "))
for i in range(n + 1):
    print(i)

ini = int(input("digite um numero inicial: "))
med = int(input("vai de quanto em quanto? : "))
fim = int(input("digite um numero final: "))
for i in range(ini, fim + 1, med):
    print(i)
