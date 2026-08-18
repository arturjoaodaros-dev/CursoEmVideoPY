valores = list(range(1, 99, 2))
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
valores.append(99)
print(f"a lista tem {len(valores)} numeros")
valores.remove(3)  # remove o valor 3 da lista
print(f"A lista sem o numero 3 tem {len(valores)} numeros")
for v in valores:
    print(f"{v}", end=", ")
