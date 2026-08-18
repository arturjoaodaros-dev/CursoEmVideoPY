# Extraido de Aula008.py - desafio019
import random

aln = int(input("digite a quantidade de alunos: "))
lista = []
for _ in range(aln):
    nm = input("digite o nome: ")
    lista.append(nm)

print(f"a escolha foi {random.choice(lista)}")
