lanche = (
    "hámburger",
    "suco",
    "pizza",
    "pudim",
)  # lanche = ('hámburger', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[-1])  # n da de mudar tupla asljkdfalkjdsfhjhldsf
print(lanche[3])  # o msm de -1
print(lanche[:2])  # começa do 0 até 2
for comidas in lanche:
    print(f"comi {comidas}")
for cont in range(len(lanche)):
    print(lanche[cont])
for pos, comida in enumerate(lanche):
    print(f"eu vou comer {comida} na posição {pos}")
print(sorted(lanche))  # funciona com numeros tbm
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))
del a  # pode apagar tupla ebaaa
