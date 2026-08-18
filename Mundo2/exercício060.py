import math

ls = []
n = int(input("digite um numero: "))
while n != 0:
    ls.append(n)
    n -= 1
print(math.prod(ls))
