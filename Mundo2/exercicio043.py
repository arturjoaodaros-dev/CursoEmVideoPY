alt = float(input("qual a sua altura: "))
pes = float(input("digite o seu peso: "))
IMC = pes * alt**2
if IMC <= 18.5:
    print("abaixo do peso")
elif IMC <= 25:
    print("ideal")
elif IMC <= 30:
    print("sobrepeso")
elif IMC <= 40:
    print("obeso")
else:
    print("obesidade mórbida (ou órbita)")
