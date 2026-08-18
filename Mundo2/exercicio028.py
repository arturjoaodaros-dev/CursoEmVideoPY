import random


def main():
    try:
        n = random.randint(0, 5)
        i = int(input("tente adivinhar o numero que estou pensando: "))
        if i == n:
            print("parabens era este")
        else:
            print("tente novamente")
            main()
    except:
        print("algo de errado aconteceu")
        main()


main()
