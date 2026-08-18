Pessoas = []
mulheres = []
id = []
ct = 1
while True:
    print("=-" * 15, ct, "° pessoa", "=-" * 15)
    Nome = str(input("digite o seu nome: "))
    Idade = int(input("digite a sua idade: "))
    Sexo = str(input("digite seu sexo[M/F]: ")).lower()
    if Sexo in "m f":
        """tudo certo"""
    else:
        Sexo = str(input("digite uma opção válida[M/F]: ")).lower()
    dic = {"nome": Nome, "idade": Idade, "sexo": Sexo}
    Pessoas.append(dic)
    ask = str(input("deseja continuar[S/N]: ")).lower()
    if ask == "n":
        break
    elif ask != "s":
        ask = str(input("Insira uma opção valida[S/N]: ")).lower()
    print("=-" * 15, ct, "° pessoa", "=-" * 15)
    ct += 1
print(f"{len(Pessoas)} pessoas foram cadastradas")
for it in Pessoas:
    id.append(it["idade"])
    if it["sexo"] == "f":
        mulheres.append(it["nome"])
print(f"as mulheres do grupo são: {mulheres}")
print(f"a média de idade do grupo é {sum(id) / len(id)}")
print("as pessoas mais velhas que a média de idade do grupo são:", end=" ")
for it in Pessoas:
    if it["idade"] > (sum(id) / len(id)):
        print(it["nome"], end=", ")
