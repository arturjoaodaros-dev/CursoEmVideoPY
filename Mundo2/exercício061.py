p = int(input("digite o primeiro termo [tem que ser inteiro]: "))
r = int(input("digite a razão: "))
f = p + (10 - 1) * r
while p <= f:
    print(p)
    p += r
