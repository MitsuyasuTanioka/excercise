import random

l1 = []
l1 = [random.randint(0, 99) for i in range(0, 100)]
print(l1)

l2 = {i for i in l1}
print(l1)
print(l2)
