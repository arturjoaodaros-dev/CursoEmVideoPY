a = float(input("Qual a largura do terreno: "))
b = float(input("qual o comprimento do terreno: "))


def area(l, c):
    return l * c


print(f"A area do terreno {a} x {b} é de {area(a, b)}M²")
