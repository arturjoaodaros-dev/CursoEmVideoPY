def vote(i):
    import datetime

    df = datetime.date.today().year - i
    if df < 18:
        return df, "NEGADO"
    elif df < 60:
        return df, "OBRIGATÓRIO"
    else:
        return df, "OPCIONAL"


a = vote(int(input("digite o ano de nascimento: ")))
print(f"com {a[0]} anos, seu voto é {a[1]}")
