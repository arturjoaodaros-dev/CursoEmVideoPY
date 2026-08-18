def leiaInt(it):
    """returns the user's answer from a question, if the answer is not a
    float value, it retuns an error"""
    while True:
        try:
            i = int(input(it))
            return i
        except:
            print("\033[31m[ERROR] INSERT A VALID INTEGER\033[m")


u = leiaInt("digite um numero inteiro: ")
print(f"você acabou de digitar {u}")
