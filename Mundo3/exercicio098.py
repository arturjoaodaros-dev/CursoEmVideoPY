from time import sleep

a = int(input("qual será o inicio da contagem: "))
b = int(input("qual será o fim da contagem: "))
c = int(input("em quantos passos irá a contagem: "))


def contagemdez(str):
    print(str)
    for i in range(1, 11):
        print(i, end=" ", flush=True)
        sleep(0.5)
    print("\n")


def contagemdois(str):
    print(str)
    for i in range(10, 0, -2):
        print(f"{i}", end=" ", flush=True)
        sleep(0.5)
    print("\n")


def customcount(str, a, b, c):
    print(str)
    if c < 0:
        c *= -1
    if c > 0:
        if a < b:
            for i in range(a, b, c):
                print(i, end=" ", flush=True)
                sleep(0.5)
            print("\n")
        else:
            for i in range(a, b, -c):
                print(i, end=" ", flush=True)
                sleep(0.5)
            print("\n")
    elif c < 0:
        if a < b:
            for i in range(a, b, c):
                print(i, end=" ", flush=True)
                sleep(0.5)
            print("\n")
        else:
            for i in range(a, b, c):
                print(i, end=" ", flush=True)
                sleep(0.5)
    else:
        c = 1
        if a < b:
            for i in range(a, b, c):
                print(i, end=" ", flush=True)
                sleep(0.5)
            print("\n")
        else:
            for i in range(a, b, -c):
                print(i, end=" ", flush=True)
                sleep(0.5)
        print("\n")


contagemdez("Contagem de 10 em 10!")
contagemdois("contagem de 10 em 10 por 2")
customcount("boa", a, b, c)
