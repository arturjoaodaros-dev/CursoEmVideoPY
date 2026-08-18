while True:
    ask = float(input("digite um numero(negativo para parar):"))
    if ask < 0:
        break
    else:
        print("-" * 30)
        for i in range(11):
            print(f"{ask} X {i} = {ask * i}")
        print("-" * 30)
