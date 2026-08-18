try:
    a = float(input("denomindaor: "))
    b = float(input("Numerador: "))
    c = b / a
    print(c)
except Exception as erro:
    print(f"\033[31mERRO, não funcionou {erro.__class__}, {erro.__cause__}\033[m")
finally:
    print("\033[34mAté logo\033[m")

try:
    d = float(input("denomindaor: "))
    e = float(input("Numerador: "))
    f = e / d
    print(f)
except ValueError:
    print("\033[31mERRO, não funcionou, digite um numero inteiro literal\033[m")
except ZeroDivisionError:
    print("\033[31mOH NÃO, VOCÊ DIVIDIU UM NUMERO POR ZERO, AGORA VAMOS MORRER\033[m")
except KeyboardInterrupt:
    print("nss n tem tempo de digitar 2 numeros q pressa é essa!")
finally:
    print("\033[34mAté logo\033[m")
