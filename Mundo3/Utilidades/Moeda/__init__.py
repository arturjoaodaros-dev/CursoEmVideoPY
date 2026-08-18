def dobro(*n, list=False, formated=False):
    """Dobro: função que dobra o valor de 1 ou mais numeros ou de uma lista/tupla completa
    :param n: numeros a ser dobrados
    :param list: se o valor a serem retornado será uma lista
    :param return: retorna uma tupla com os valores agora dobrados"""
    if list:
        r = []
    else:
        r = ()
    for i in n:
        i *= 2
        if list:
            r.append(i)
        else:
            r += (i,)
    if formated:
        tmp = []
        rst = []
        for i in r:
            tmp.append(float(i))
            for id, it in enumerate(tmp):
                its = str(it).replace(".", " ").rstrip().lstrip().split()
                its[1] += "0"
                rst.append(f"R${its[0]},{its[1][0:2]}")
                tmp.remove(it)
                its = ""
    if formated:
        return rst
    else:
        return r


def triplo(*n, list=False, formated=False):
    """Triplo: função que triplica o valor de 1 ou mais numeros ou de uma lista/tupla completa
    :param n: numeros a serem Triplicados
    :param list: se o valor a ser retornado será uma lista
    :param return: retorna uma tupla com os valores agora triplicados"""
    if list:
        r = []
    else:
        r = ()
    for i in n:
        i *= 3
        if list:
            r.append(i)
        else:
            r += (i,)
    if formated:
        tmp = []
        rst = []
        for i in r:
            tmp.append(float(i))
            for id, it in enumerate(tmp):
                its = str(it).replace(".", " ").rstrip().lstrip().split()
                its[1] += "0"
                rst.append(f"R${its[0]},{its[1][0:2]}")
                tmp.remove(it)
                its = ""
    if formated:
        return rst
    else:
        return r


def metade(*n, list=False, exact=False, formated=False):
    """Metade: função que divide o valor de 1 ou mais numeros ou de uma lista/tupla completa por 2
    :param n: numeros a serem divididos
    :param list: se o valor a ser retornado será uma lista
    :param return: retorna uma tupla com os valores agora divididos"""
    if list:
        r = []
    else:
        r = ()
    for i in n:
        if exact:
            i //= 2
            if list:
                r.append(i)
            else:
                r += (i,)
        else:
            i /= 2
            if list:
                r.append(i)
            else:
                r += (i,)
    if formated:
        tmp = []
        rst = []
        for i in r:
            tmp.append(float(i))
            for id, it in enumerate(tmp):
                its = str(it).replace(".", " ").rstrip().lstrip().split()
                its[1] += "0"
                rst.append(f"R${its[0]},{its[1][0:2]}")
                tmp.remove(it)
                its = ""
    if formated:
        return rst
    else:
        return r


def aumento(a, *n, list=False, formated=False):
    """Aumento: função que aumenta um numero por uma porcentagem
    :param a: procentagem a ser aumentada em um numero
    :param n: numeros ou lista/tupla a serem aumentados
    :param list: se o valor a ser retornado será uma lista
    :param formated: se o valor retornado será com a formatação de reais
    :param return: retorna os valores agora aumentados"""
    a /= 100
    a += 1
    if list:
        r = []
    else:
        r = ()
    for it in n:
        if list:
            r.append(it * a)
        else:
            r += (it * a,)
    if formated:
        tmp = []
        rst = []
        for i in r:
            tmp.append(float(i))
            for id, it in enumerate(tmp):
                its = str(it).replace(".", " ").rstrip().lstrip().split()
                its[1] += "0"
                rst.append(f"R${its[0]},{its[1][0:2]}")
                tmp.remove(it)
                its = ""
    if formated:
        return rst
    else:
        return r


def reduzir(rd, *n, list=False, formated=False):
    """Reduzir: função que reduz um numero por uma porcentagem
    :param a: procentagem a ser reduzida em um numero
    :param n: numeros ou lista/tupla a serem reduzidos
    :param list: se o valor a ser retornado será uma lista
    :param formated: se o valor retornado será com a formatação de reais
    :param return: retorna os valores agora reduzidos"""
    if list:
        r = []
    else:
        r = ()
    rd = 1 - rd / 100
    for i in n:
        if list:
            r.append(i * rd)
        else:
            r += (i * rd,)
    if formated:
        tmp = []
        rst = []
        for i in r:
            tmp.append(float(i))
            for id, it in enumerate(tmp):
                its = str(it).replace(".", " ").rstrip().lstrip().split()
                its[1] += "0"
                rst.append(f"R${its[0]},{its[1][0:2]}")
                tmp.remove(it)
                its = ""
    if formated:
        return rst
    else:
        return r


def moeda(n):
    """Moeda: função que retorna um valor unico com a ormatação para reais brasileiros
    :param n: numero a ser formatado
    :param return: retorna o numero, agora formatado"""
    r = float(n)
    i = str(r).replace(".", " ").rstrip().split()
    i[1] += "0"
    l = f"R${i[0]},{i[1][0:2]}"
    return l
