tps = ()
tpf = ()
while True:
    ask = str(input("digite um produto: "))
    pr = float(input("qual o seu preço: "))
    tps += (ask,)
    tpf += (pr,)
    f = str(input("finalizar tabela[S/N]? "))
    if f == "s":
        break

print("=" * 30, "\n", "LISTA DOS PREÇOS", "\n", "=" * 30)
for i in range(len(tps)):
    print(f"{tps[i]}", "." * (10 - len(tps[i]) + 1), "R$", f"{tpf[i]}")
