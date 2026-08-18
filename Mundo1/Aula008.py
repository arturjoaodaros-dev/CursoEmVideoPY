import math
import random

import emoji

num = float(input("diga o numero:"))
print(math.ceil(math.sqrt(num)))
print(random.randint(1, 100))
print(emoji.emojize("eu sou :thumbsup:", language="alias"))
# aqui começa
Imp = float(input("digite um numero não inteiro (use ponto)"))
print(math.floor(Imp))
# outro exercício
adj = float(input("Insira o cateto adjacente: "))
ops = float(input("Insira o cateto oposto: "))
print(f"a hipotenusa do seu trianulo retangulo é {(adj**2 + ops**2) ** 0.5}")
# outro exercício
ang = float(input("digite o angulo: "))
rad = math.radians(ang)
print(f"sin: {math.sin(rad)}, cos: {math.cos(rad)}, tan: {math.tan(rad)}")
# outro exercício
aln = int(input("digite a quantidade de alunos: "))
lista = []
for _ in range(aln):
    nm = input("digite o nome: ")
    lista.append(nm)
print(f"a escolha foi {random.choice(lista)}")
random.shuffle(lista)
print(f"a ordem de apresentação é: {lista}")
# outro exercício
aln = int(input("digite a quantidade de alunos: "))
lista = []
for _ in range(aln):
    nm = input("digite o nome: ")
    lista.append(nm)
random.shuffle(lista)
print(f"a ordem de apagar o quadro é: {lista}")
