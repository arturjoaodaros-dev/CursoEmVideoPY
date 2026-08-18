ls = []  # 2, 3, 5, 4. 1

w = 0
e = 0
r = 0

for i in range(5):
    ask = float(input(f"digite o {i}° valor:"))
    ls.append(ask)
    q = min(ls)
    t = max(ls)
    if ask == t:
        print("numero add ao final da lista")
    elif ask == q:
        print("numero add ao começo da lista")
    else:
        print(f"numero add na posição {ls.index(ask)}")
for o in ls:
    if o < t and o > q:  # 1 e 5 FORA
        if o >= r:
            if e <= r:
                w = e
                e = r
            r = o
        elif o >= e:
            w = max(e, w)
            e = o
        elif o >= w:
            w = o
print(f"a lista enumerada fica {q, w, e, r, t}")

numeros = []

ask = int(input("Quantos números deseja informar? "))
for i in range(ask):
    num = float(input(f"digite o {i}° valor:"))
    numeros.append(num)

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print(f"a lista enumerada fica {numeros}")
