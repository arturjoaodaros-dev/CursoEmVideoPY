ls = []
for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        ls.append(i)
print(sum(ls))
