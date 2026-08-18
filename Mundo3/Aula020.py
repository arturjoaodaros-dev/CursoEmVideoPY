def showtitle(title):
    print("-" * 30)
    print(f"\033[1m{title:^30}\033[m")
    print("-" * 30, "\n")


def soma(a, b):
    print(a + b)


def somaplus(*num):
    s = 0
    for v in num:
        s += v
    print(s)


def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        print(list[pos])
        pos += 1


somaplus(9, 9, 6, 5, 8)
soma(3.97908, 6.33333)
showtitle("ola")
dobra([1, 2, 3, 4, 5])
