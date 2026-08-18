tp = ("arroz", "passaro", "goblin", "estrada")
con = (
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
)
for itens in tp:
    print(f"na palavra {itens} temos as vogais", end=" ")
    for c in itens:
        if c in con:
            itens = itens.replace(c, "")
    print(itens, "\n")
