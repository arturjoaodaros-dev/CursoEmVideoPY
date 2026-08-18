md = []
hm = ""
ml = []
ids = 0
print("-=" * 30)
print("contador de caracteristicas")
print("-=" * 30)

q = int(input("quantas pessoas serão analizadas: "))

for i in range(1, q + 1):
    print(f"-----{i}° pessoa------")
    sx = str(input("por favor, informe o seu sexo: ")).lower()
    id = int(input("digite a sua idade: "))
    nm = str(input("digite o seu nome: ")).lower()
    print(f"-----{i}° pessoa------\n")
    md.append(id)
    if sx == "masculino" and id >= ids:
        ids = 0
        ids += id
        hm = nm
    md.append(id)
    if sx == "feminino" and id <= 20:
        ml.append(nm)
print(f"a media de idade do grupo é {sum(md) / len(md)}")
print(f"parabens, o homem mais velho é {hm}")
print(f"temos {len(ml)} mulheres com menos de 20 anos")
