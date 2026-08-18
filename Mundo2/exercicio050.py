ls = []
for i in range(6):
    m = int(input("digite um numero inteiro: "))
    if m & 2 == 0:
        ls.append(m)
print(sum(ls))
