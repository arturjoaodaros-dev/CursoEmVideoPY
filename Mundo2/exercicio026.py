# Recuperado - desafio026
a = input("digite a frase: ")
a_lower = a.lower()
print("A letra A apareceu {} vezes na frase".format(a_lower.count("a")))
primeira = a_lower.find("a")
ultima = a_lower.rfind("a")
if primeira != -1:
    print(f"Ela apareceu pela primeira vez na posi????o: {primeira + 1}")
    print(f"Ela apareceu pela ??ltima vez na posi????o: {ultima + 1}")
else:
    print("A letra A n??o aparece na frase.")
