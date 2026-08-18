p = int(input("digite o primeiro termo [tem que ser inteiro]: "))
r = int(input("digite a razão: "))
f = p + (10 - 1) * r
while p <= f:
    print(p)
    p += r
a = int(input("gostaria de ver mais termos[digite quanto ou 0 para sair]: "))
if a != 0:
    f = p + (a - 1) * r
    while p <= f:
        print(p)
        p += r
