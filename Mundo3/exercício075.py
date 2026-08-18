tp = ()
p = 0
pp = ()
for i in range(4):
    ask = int(input("digite um numero inteiro: "))
    tp += (ask,)
print(f"o numero 9 apareceu {tp.count(9)} vezes")
print(f"o numero 3 apareceu pela primeira vez na posição de {tp.index(3) + 1}° lugar")
for i in tp:
    if i % 2 == 0:
        p += 1
        pp += (i,)
print(f"tivemos {p} numeros pares")
