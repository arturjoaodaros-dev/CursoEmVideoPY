ls = []
t = 0
i = int(input("digite um numero: "))
while i != 999:
    ls.append(i)
    t += 1
    i = int(input("digite um numero: "))
print(
    f"Programa encerrado, você digitou {t} numeros e a soma entre eles foi de {sum(ls)}"
)
