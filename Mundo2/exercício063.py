# resultado esperado: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
n = int(input("Quantos termos? "))

a = 0
b = 1

sq = 0

while sq < n:
    print(a)  # a = 0

    rs = a + b  # 0 + 1 = 1
    a = b  # a = 1
    b = rs  # b = 1

    sq += 1
