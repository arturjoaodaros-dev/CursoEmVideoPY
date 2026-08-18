def maior(*num):
    ls = []
    for i in num:
        ls.append(i)
    if len(ls) > 0:
        return max(ls)
    else:
        return None


print(f"{maior()}")
