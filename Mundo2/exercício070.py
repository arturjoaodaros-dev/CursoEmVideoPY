p = 0
b = ""
bv = 0
pr = 0
pm = 0
while True:
    p += 1
    print(f"============={p}° produto===============")
    n = str(input("qual o nome do produto: "))
    pc = float(input("qual o preço do produto: "))
    pr += pc
    print(f"============={p}° produto===============")
    ask = str(input("quer continuar[S / N]: ")).lower()
    if ask == "n":
        break
    if bv == 0 or pc <= bv:
        b = n
    if pc >= 1000:
        pm += 1

print(
    f"o valor total é de {pr}, tivemos {pm} produtos custando mais de 1000 reais e o produto mais barato é o/a {b}"
)
