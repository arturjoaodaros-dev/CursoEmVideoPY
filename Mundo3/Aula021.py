def couter(b, c):  # usando a global
    global a
    """prints a loop starting from the first value and going 
    to the second value, the steps are measured by a third value"""
    if b > a:
        for i in range(a, b, c):
            print(i, end=" ")
            print("\n")
    else:
        for i in range(a, b, -c):
            print(i, end=" ")
            print("\n")


a = 9
help(couter)


def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print(factorial(5))
