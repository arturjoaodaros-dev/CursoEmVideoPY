pss = [["artur", 12], ["thiago", 40], ["daiane", 40]]
nps = []
print(pss[0][1])
pss[0][0] = "cachorro"
print(pss[:])
pss[0][1] = 2
print(pss[0][1])
print(pss[:])
print(pss[0])
for p in pss:
    print(p[0])
for p in pss:
    print(p[0], end=", ")
    nps.append(
        str(input("digite um nome: "))
    )  # pss.append(str(input('digite um nome: '))) INFINITO
