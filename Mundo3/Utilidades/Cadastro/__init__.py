def CreateTXTPerson(list=False):
    n = 0
    if list:
        while n < 100:
            try:
                wer = open(f"teste{n}.txt", "w")
                print(wer)
                break
            except:
                n += 1
    else:
        r = 0
        while r < 1:
            try:
                w = open(f"teste{n}.txt", "x")
                print(f"------------------EDITANDO TESTE{n}.TXT------------------")
                f = 1
                while True:
                    nm = input(f"digite o nome da {f}° pessoa: ")
                    i = input(f"digite a idade da {f}° pessoa: ")
                    w.write(f"""NOME: {nm}
IDADE: {i} \n""")
                    f += 1
                    ask = input("gostaria de continuar[S/N]: ").lower()
                    if ask == "n":
                        r += 1
                        break
                    elif ask != "s":
                        ask = input("insira uma opção válida[S/N]: ").lower()
                    print("\n")
            except:
                n += 1


CreateTXTPerson()
