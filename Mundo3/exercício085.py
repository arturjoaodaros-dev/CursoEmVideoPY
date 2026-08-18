ListaDosNumeros = [[], []]
for i in range(1, 8):
    Valor = int(input(f"digite um valor inteiro ({i}°): "))
    if Valor % 2 == 0:
        ListaDosNumeros[0].append(Valor)
    else:
        ListaDosNumeros[1].append(Valor)
ListaDosNumeros[0].sort()
ListaDosNumeros[1].sort()
print(f"os numero pares são {ListaDosNumeros[0]}")
print(f"os numero Impares são {ListaDosNumeros[1]}")
