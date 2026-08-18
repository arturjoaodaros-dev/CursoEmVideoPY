t = 0
s = 0
while True:
    ask = int(input("digite um numero(999 para parar): "))
    if ask == 999:
        break
    else:
        s += ask
        t += 1
print(f"você colocou {t} numeros e a soma entre eles é {s}")
