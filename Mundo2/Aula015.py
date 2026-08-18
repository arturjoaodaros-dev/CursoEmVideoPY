cont = 1
while cont <= 10:
    print(cont, "-->", end=" ")
    cont += 1
print("acabou")


n = s = 0
while True:
    n = int(input("digite um numero:"))
    s += n
    if n == 666:
        break
s -= 666  # seria lgl iniciar uma variavel com o valor 666
print(f"a soma dos numeros deu {s}")  # python 3.6+
print("a soma dos numeros deu %s" % (s))  # python 2
