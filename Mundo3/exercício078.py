ls = []
p = []
m = []

apps = 0
while True:
    ask = float(input("digite um NUMERO: "))
    ls.append(ask)
    dnv = str(input("adicionar mais numeros[S/N]: ")).lower()
    if dnv == "n":
        break

mr = max(ls)
mn = min(ls)

if ls.count(max(ls)) >= 2:
    for ps, r in enumerate(ls):
        if r == mr:
            p.append(ps)
            apps += 1
    print(f"o MAIOR numero é {max(ls)} e ele aparece na(s) posição(s) {p}")
else:
    print(
        f"o MAIOR numero é {max(ls)} e ele aparece na(s) posição(s) {ls.index(max(ls))}"
    )
if ls.count(min(ls)) >= 2:
    for ps, i in enumerate(ls):
        if i == mn:
            m.append(ps)
            apps += 1
    print(f"o MENOR numero é {min(ls)} e ele aparece na(s) posição(s) {m}")
else:
    print(
        f"o MENOR numero é {min(ls)} e ele aparece na(s) posição(s) {ls.index(min(ls))}"
    )
