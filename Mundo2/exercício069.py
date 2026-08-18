p = 1
m = 0
ad = 0
mm = 0

while True:
    print("-=" * 10, p, "pessoa", "-=" * 10)
    sx = str(input("informe o sexo [M/F]: ")).lower()
    id = int(input("digite a idade da pessoa: "))
    if sx in "m f" and id % 1 == 0:
        print("-=" * 10, p, "pessoa", "-=" * 10, "\n")
        if sx == "m":
            m += 1
        if id >= 18:
            ad += 1
        if sx == "f" and id <= 20:
            mm += 1
        p += 1
        ask = str(input("deseja continuar? [S / N]")).lower()
        if ask == "n":
            print(
                f"Programa encerrado, temos {ad} maiores de idade, {m} homens e {mm} mulheres menores de 20 anos"
            )
            break
    else:
        print("\033[41minsira um valor válido!!!\033[m")
