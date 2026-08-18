# Extraido de Aula007.py - desafio007
import time

notas = int(input("quantas provas houve no trimestre"))
soma = 0
for i in range(notas):
    print("insira a nota abaixo")
    nota = float(input(">"))
    soma += nota
print(f"a média é {soma / notas}")
time.sleep(1)
