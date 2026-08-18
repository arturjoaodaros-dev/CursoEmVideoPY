p = float(input("qual o preço do item: "))
c = str(input("qual a foma de pagamento: ")).lower()
v = int(input("em quantas vezes: "))
dis = 0
if v <= 2:
    if c in "dinheiro cheque":
        dis += 0.90
    elif c in "cartão":
        dis += 0.95
    print(dis * p)
elif v >= 2:
    if c in "dinheiro cheque":
        dis += 0.90
    elif c in "cartão":
        dis += 0.95
    print(p * 1.2 * dis)
