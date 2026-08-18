def main():
    try:
        um = float(input("digite um numero:"))
        dois = float(input("digite outro numero:"))
        result = um + dois
        print(f"a soma entre {um} e {dois} é {result}:")
        answr = input("quer começar de novo? y/n")
        if answr == "y":
            main()
        else:
            print("ok, tchau")
    except:
        if ValueError:
            print(
                "ERRO: tente usar NÚMEROS, se fracionado, use PONTO ao invés de VIRGULA"
            )
            main()
        else:
            print("Algo deu de errado, tente novamente")
            main()


main()
