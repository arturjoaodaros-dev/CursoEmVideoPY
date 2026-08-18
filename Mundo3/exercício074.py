import random

tp = tuple(random.sample(range(1, 1000), 5))
print(sorted(tp))
print(min(tp))
print(max(tp))
