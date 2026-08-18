nums = []
import time
from random import randint


def sorteio(lst, i, f, q):
    for n in range(q):
        x = randint(i, f)
        lst.append(x)
    return lst


def sump(lst):
    s = 0
    for i in lst:
        if i % 2 == 0:
            s += i
    return s


sorteio(nums, 1, 100, 5)
print("a soma dos numeros sorteados foram:", end=" ")
for i in range(len(nums)):
    print(f"{nums[i]}", end=", ", flush=True)
    time.sleep(0.1)
print("\n")
print(f"a soma dos numeros pares são {sump(nums)}")
