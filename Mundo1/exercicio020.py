# Extraido de Aula008.py - desafio020
import random

aln = int(input("digite a quantidade de alunos: "))
lista = []
for _ in range(aln):
    nm = input("digite o nome: ")
    lista.append(nm)

random.shuffle(lista)
print(f"a ordem de apresenta????o ??: {lista}")
