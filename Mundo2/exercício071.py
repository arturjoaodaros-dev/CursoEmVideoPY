while True:
    ask = int(input("qual o valor inteiro a ser sacado: "))
    c = ask // 50
    v = (ask - c * 50) // 20
    d = (ask - v * 20 - c * 50) // 10
    u = (ask - d * 10 - v * 20 - c * 50) // 1
    print(
        f"BEEP, você recebeu {c} cedulas de 50, {v} cedulas de 20, {d} cedulas de 10 e {u} cedulas de 1 "
    )
    p = str(input("quer sacar novamente [S/N]: ")).lower()
    if p == "n":
        break
