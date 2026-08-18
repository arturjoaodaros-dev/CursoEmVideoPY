house = float(input("qual o valor da casa"))
salary = float(input("qual o valor do salário"))
year = int(input("em quantos anos vai pagar"))
prst = year * 12 / house

if salary * 0.30 <= prst:
    print("empréstimo negado, limite excedido")
else:
    print(f"""ótimo, podemos fazer o empréstimo sim, segue o formulário e confirme tudo:
           prestações: {prst}
           valor total {house}
           valor de cada prestação {house / prst}
           salário {salary}""")
