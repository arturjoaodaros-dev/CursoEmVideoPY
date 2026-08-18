lsm = []
ls = []

print("-=" * 30)
print("contador de maioridade")
print("-=" * 30)
q = int(input("por favor, insira a quantidade de pessoas a serem analizadas: "))
print("-" * 60)
for i in range(q):
    l = int(input("insira a idade: "))
    if l <= 18:
        ls.append(l)
    else:
        lsm.append(l)
print(f"Há {len(ls)} pessoas MENORES de idade")
print(f"Há {len(lsm)} pessoas MAIORES de idade")
