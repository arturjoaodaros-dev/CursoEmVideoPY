dados = [
    {
        "nome": "Artur",
        "idade": 12,
    },
    {"nome": "thiago", "idade": 40},
    {"nome": "daiane", "idade": 40},
]
# dados['sexo'] = 'Masculino'
# print(dados['nome'], '\n', dados['idade'], '\n', dados['sexo'])
# del dados['idade']
# print(dados['nome'], dados['sexo'])
# print(dados.values())
# print(dados.keys())
# for k, v in dados.items():
#    print(f'o {k} é {v}')
print(dados[0]["nome"])
for n in dados:
    for v, t in n.items():
        print(v, "=", t)

dados.remove()
