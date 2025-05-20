l1 = [i for i in range(4000, 5001) if i % 17 == 0]
print(l1)
l2 = [2]
for i in range(3, 2501):
    flag = True
    for j in l2:
        if i % j == 0:
            flag = False
    if flag:
        l2.append(i)
print(l2)

for i in l1:
    tmp = i
    l3 = []
    for j in l2:
        count = 0
        while i % j == 0:
            # print(str(i) + "/" + str(j))
            i = i / j
            count += 1
        l3.append(count)
        if i == 1:
            # print("ブレイクします")
            break
        # if tmp==4012:
        #     print(l3)
    # print(l3)
    # print(len(l3))
    print(str(tmp) + " = ", end="")
    for k in range(0, len(l3)):
        if l3[k] != 0:
            print(str(l2[k]) + " ^ " + str(l3[k]), end="")
            if k != len(l3) - 1:
                print(" * ", end="")
    print()



