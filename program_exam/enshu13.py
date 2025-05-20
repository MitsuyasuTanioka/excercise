# rndArray = [2, 5, 3, 1, 6]
rndArray = [2, 5, 3, 1, 6, 20, 9, 4, 2]
i = len(rndArray)-1

while i != 0:
    for j in range(0, i):
        if rndArray[j] > rndArray[j + 1]:
            rndArray[j], rndArray[j + 1] = rndArray[j + 1], rndArray[j]
    #     print(rndArray)
    # print()
    i -= 1

print(rndArray)


# rndArray[0], rndArray[1] = rndArray[1], rndArray[0]
# print(rndArray)
