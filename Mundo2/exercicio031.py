o = int(input("qual a distância da viagem em KM:"))
if o <= 200:
    o *= 0.50
    print(f"o preço da passagem é {o}")
else:
    o *= 0.45
    print(f"o preço da passagem é {o}")
