v = int(input("qual a velocidade do seu carro: "))
if v >= 80:
    va = v - 80
    multa = 0
    for i in range(va):
        multa += 7
    print(f"sua multa foi de {multa}$")
else:
    print("continue assim, procure não ultrapassar 80KM")
