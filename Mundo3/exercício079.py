ls = []
while True:
    ask = float(input("digite um valor (-999 para sair):"))
    if ask not in ls and ask != -999:
        ls.append(ask)
        print("valor adicionado com sucesso!")
    elif ask == -999:
        break
    else:
        print("ERRO, valor duplicado")
ls.sort()
for i in range(len(ls)):
    print(ls[i], end=", ")
