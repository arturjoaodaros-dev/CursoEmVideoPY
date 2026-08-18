Dados = []
while True:
    nome = str(input("digite o nome do aluno: "))
    media = float(input(f"digite a media do {nome}: "))
    dic = {"nome": nome, "media": media}
    if media <= 7:
        dic["situação"] = "reprovado"
    else:
        dic["situação"] = "aprovado"
    Dados.append(dic.copy())
    ask = str(input("deseja continuar[S/N]? "))
    if ask == "n":
        break
    elif ask == "s":
        """ nada acontece"""
    else:
        ask = str(input("insira uma opção válida[S/N]: "))
for d in Dados:
    for t, v in d.items():
        print(f"{t} = {v}", end="\n")
