c = 1
w = 1
r = "s"
p = i = 0
while c <= 10:
    print(c)
    c += 1
while r != "n":
    w = int(input("digite um valor inteiro: "))
    if w != 0:
        if w % 2 == 0:
            p += 1
        else:
            i += 1
    else:
        break
    r = str(input("quer continuar [S / N]: ")).lower()
print(f"Tivemos {p} numeros pares e {i} numeros impares")
