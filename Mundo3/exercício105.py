def notas(*i, situation=False):
    """function that Returns the stats of a class based on all grades, all in a dic
    tionary"""
    ls = []
    for it in i:
        ls.append(it)
    dc = {}
    st = ""
    dc["QuantidadeDeNotas"] = len(ls)
    dc["MaiorNota"] = max(ls)
    dc["MenorNota"] = min(ls)
    dc["MediaDaTurma"] = sum(ls) / len(ls)
    if dc["MediaDaTurma"] < 7:
        st = "RUIM"
    else:
        st = "BOA"
    if situation:
        dc["situação"] = st
    return dc


print(notas(9, 9, 9, 9, 4, 3, 7, 10, situation=True))
