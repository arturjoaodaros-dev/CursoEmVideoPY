nums = (
    "zero",
    "um",
    "dois",
    "tres",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
while True:
    ask = int(input("digite um numero inteiro de 0 - 20(-1 para sair): "))
    if ask <= 20:
        print(f"seu numero por extenso é \033[34m{nums[ask].upper()}\033[m")
        break
    elif ask == -1:
        break
    else:
        print("digite um numero valido")
