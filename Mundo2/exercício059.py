import math

print("-=" * 30)
print("TABELA DOS VALORES")
print("-=" * 30)
ls = []
o = float(input("digite o \033[34mPRIMEIRO\033[m valor: "))
t = float(input("digite o \033[34mSEGUNDO\033[m valor: "))
ls.append(o)
ls.append(t)


def main():
    while True:
        print(""" SELECIONE UMA DAS OPÇÔES ABAIXO:
            [1] SOMAR
            [2] MULTIPLICAR
            [3] MAIOR
            [4] ADICIONAR NOVO NUMERO
            [5] SAIR""")
        c = int(input(">"))
        if c == 1:
            print(sum(ls))
        elif c == 2:
            print(math.prod(ls))
        elif c == 3:
            print(max(ls))
        elif c == 4:
            nw = int(input("novo numero: "))
            ls.append(nw)
        elif c == 5:
            break
        else:
            print("tente novamente: ")


main()
