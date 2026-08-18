def leiaInt(it):
    """returns the user's answer from a question, if the answer is not a
    float value, it retuns an error"""
    while True:
        try:
            i = int(input(it))
            return i
        except KeyboardInterrupt:
            print("\n \033[31mO usuário não digitou esse numero")
        except:
            print("\033[31m[ERROR] INSERT A VALID INTEGER\033[m")


def leiaFloat(it):
    while True:
        try:
            i = float(input(it))
            return i
        except KeyboardInterrupt:
            print("\n \033[31mO usuário não digitou esse numero\033[m")
            return 0
            break
        except:
            print("\033[31m[ERROR] INSERT A VALID FLOAT\033[m")


r = leiaFloat("Digite um Inteiro: ")
d = leiaFloat("digite um real: ")
print(f"{r}, {d}")
