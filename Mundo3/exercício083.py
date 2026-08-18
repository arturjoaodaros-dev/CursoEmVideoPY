ask = str(input("digite uma expressão numérica: "))
p = ask.count("(") % 2
c = ask.count("{") % 2
ch = ask.count("[") % 2
if p == c == ch == 0:
    print("expressão valida")
else:
    print("expressão inválida")
