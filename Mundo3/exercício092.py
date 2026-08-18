import datetime

Dados = {}
Dados["Nome"] = str(input("Digite o seu nome: "))
Dados["Idade"] = int(datetime.date.today().year) - int(
    input("digite o seu ano de nascimento: ")
)
Dados["IDDaCarteira"] = int(input("inserir o ID da carteira: "))
if Dados["IDDaCarteira"] != 0:
    Dados["AnoDeContratação"] = int(input("Digite o ano de contratação: "))
    Dados["salario"] = float(input("digite o salário: "))
Dados["TempoRestanteDeTrabalho"] = 60 - (
    int(datetime.date.today().year) - Dados["AnoDeContratação"]
)
for k, v in Dados.items():
    print(f"{k} = {v}")
