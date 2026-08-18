import random

usr = str(input("pedra, papel ou tesoura? ")).lower()
computer = random.choice(["pedra", "papel", "tesoura"])
if usr and computer in "pedra papel tesoura":
    if (
        usr == "pedra"
        and computer == "tesoura"
        or usr == "papel"
        and computer == "pedra"
        or usr == "tesoura"
        and computer == "papel"
    ):
        print("\033[0;30;42mvocê venceu!\033[m")
    elif usr == computer:
        print("empate, tente novamente")
    else:
        print(f"\033[0;30;41mpuxa, você perdeu, minha escolha era {computer}\033[m")
