def factorial(a, show=False):
    """return a numbers factorial, the factorial is calculated
    by multiplying a number by its decendents
    show=bool[true, false] modyfies the function for it to return or not
    the way it was calculated."""
    f = 1
    for c in range(1, a):
        if show:
            print(f"{f} X {c} = {f * c}")
        f *= c
    return f


print(factorial(5, True))
