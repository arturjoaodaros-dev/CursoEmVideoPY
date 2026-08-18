ls = []
while True:
    ask = float(input("digite um numero:"))
    dnv = str(input("digite n AGORA para parar"))
    if dnv == "n":
        break
    ls.append(ask)
print(f"sua lista teve {len(ls)} elementos")
ls.sort(reverse=True)
print(f"a lista em ordem decrecente ficou {ls}")
for p, i in enumerate(ls):
    if i == 5:
        print(f"o numero 5 faz parte da lista! na posição {i}")
