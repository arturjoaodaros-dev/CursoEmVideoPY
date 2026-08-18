ls = []
sf = 0
while True:
    Aluno = str(input("qual o nome do aluno: ")).lower()
    Nota1 = float(input("digite a primeira nota: "))
    Nota2 = float(input("digite a segunda nota: "))
    aln = [Aluno, Nota1, Nota2]
    ls.append(aln)
    Continuar = str(input("gostaria de continuar [S/N]: "))
    if Continuar == "n":
        break
    elif Continuar == "s":
        """ nada acontece"""
    else:
        Continuar = str(input("Insira uma opção valida [S/N]: "))
print("No. Nome              Média")
for alunos in ls:
    if len(alunos) <= 19:
        n = ls.index(alunos)
        print(
            f"{n}°  {alunos[0]}",
            " " * (20 - (len(str(n)) + len(alunos[0]))),
            f"MÉDIA: {(alunos[1] + alunos[2]) / 2}",
        )
while True:
    ask = str(input("digite o nome do aluno para ver a sua média (999 para sair): "))
    if ask == "999":
        break
    else:
        for it in ls:
            if it[0] != ask:
                sf + 1
            else:
                print(f"as notas de {it[0]} são {it[1]}, {it[2]}")
                break
            if sf == len(ls):
                print("nome não encontrado!")
