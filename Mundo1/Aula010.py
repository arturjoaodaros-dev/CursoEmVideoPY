time = int(input("quantos anos tem o seu carro?"))

if time <= 20:
    print("carro novo")
else:
    print("Carro velho")

print("carro novo" if time <= 3 else "carro velho")

nome = str(input("Qual o seu nome:"))
if nome.count("a".upper().lower()) == 1:
    print("bom nome")
else:
    print("nome feio")
print(f"bom dia {nome}")

n1 = float(input("qual foi a primeira nota"))
n2 = float(input("qual foi a segunda nota"))
if n1 + n2 >= 19:
    print("damn bro, boa")
elif n1 + n2 >= 15:
    print("media, boa")
else:
    print("recuperação trouxa hahahah")
