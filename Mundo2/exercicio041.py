print("=" * 35)
print("CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print("=" * 35)
print("documento oficial")
id = int(input("para se inscrever na competição, você deve inserir  a sua idade: "))
if id <= 9:
    print("sua categoria é mirim, não recomendado")
elif id <= 14:
    print("sua categoria é infantil recomendado")
elif id <= 19:
    print("sua categoria é junior, deve ir")
elif id <= 20:
    print("sua categoria é sênior, não recomendado")
else:
    print("você é master, parabens, mas não deve participar")
