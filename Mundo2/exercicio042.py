a = float(input("Insira o cateto adjacente: "))
b = float(input("Insira o cateto oposto: "))
c = (a**2 + b**2) ** 0.5
print(f"a hipotenusa do seu triangulo retangulo é {c}")
if a == b == c:
    print("Equilátero")

elif a == b or a == c or b == c:
    print("Isósceles")

else:
    print("Escaleno")
