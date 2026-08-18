# Recuperado - desafio022
name = str(input("qual o seu nome? ")).strip
newname = name.split()
print(f"seu primeiro nome tem: {len(newname[0])} letras")
name = name.upper()
print("seu nome em maiusculo ??:", name)
name = name
name = name.capitalize()
print("seu nome em minusculo ??:", name)
name = name.replace(" ", "")
print(f"seu nome tem: {len(name)} letras")
