md = float(input("digite a sua média: "))
if md <= 5.0:
    print("você está possivelmente reprovado")
    print(f"falta {7 - md} pontos para passar")
elif md < 7.0:
    print("você está possivelmente de recuperação")
    print(f"falta {7 - md} pontos para passar")
else:
    print("você está na média, parabens")
