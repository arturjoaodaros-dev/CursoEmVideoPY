id = int(input("digite a sua idade: "))
if id == 18:
    print("se aliste agora")
elif id >= 18:
    c = input("já se alistou: s/n")
    if c == "s":
        print("bom, não minta")
    else:
        print("190 chamand...")
        print(f"você está a {id - 18} atrasado")
else:
    print(f"você tem {18 - id} anos para se alistar")
