import datetime


def Program():

    try:
        dia = int(input("qual o dia de seu nascimento?"))
        mes = int(input("qual o mês de seu nascimento? (em numero)"))
        ano = int(input("qual o ano de seu nascimento?"))
        print("você nasceu em", dia, "/", mes, "/", ano)
        anos = datetime.datetime.now().year - ano
        print("voce tem", anos)
    except:
        print(
            "poxa cara, é meu primeiro código maneiro de phyton, só segue as regras certinho, ngm ta te achando o engraçadão pq colocou isoo ae n, tá mais pra um chato, retardo, literal é só um experimento que crie sozinho aq, quer uma estrelinha na cabeça pq fez errado? quer saber, vou te foçar a fazer tudo dnv pra ver se aprende msm"
        )
        Program()


Program()
