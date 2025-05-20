l1 = [2, 5, 3, 1, 6]
l2 = []

for i in range(0, len(l1)):
    min = l1[0]
    for j in l1:
        if min > j:
            min = j
    l2.append(min)
    l1.remove(min)
print(l1)
print(l2)
