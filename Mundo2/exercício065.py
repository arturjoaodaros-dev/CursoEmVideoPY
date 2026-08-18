ls = []
r = ""
while r != "n":
    i = float(input("digite um numero:"))
    ls.append(i)
    r = str(input("quer continuar [S / N]")).lower()
print(
    f"programa encerrado, a media entre os numeros foi {sum(ls) // len(ls)} [Arredondado]"
)
