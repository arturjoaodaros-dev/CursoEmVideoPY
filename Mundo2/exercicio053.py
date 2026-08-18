f = str(input("digite a frase: ")).replace(" ", "")
ls = []
fc = len(f)
for c in range(fc - 1, -1, -1):
    ls.append(f[c])
ls = "".join(ls)
if ls == f:
    print("palindromo")
else:
    print("frase de beta")
