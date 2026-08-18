ls = []
lsp = []
lsi = []
while True:
    ask = int(input("digite um numero: "))
    dnv = str(input("digite n AGORA para parar: "))
    ls.append(ask)
    if dnv == "n":
        break

ls.sort()
for i in ls:
    if i % 2 == 0:
        lsp.append(i)
    else:
        lsi.append(i)
print(f"""
      LISTA 1: {ls}
      LISTA 2: {lsp}
      LISTA 3: {lsi}""")
