import math

rndArray = [2, 5, 3, 1, 6]
# rndArray = [2, 5, 3, 1, 6, 3, 7, 10, 8, 4]

def merge(li):
    if len(li) != 1:
        index1 = math.ceil(len(li) / 2)
        l1 = list_split(li, 0, index1)
        l2 = list_split(li, index1, len(li))
        l1 = merge(l1)
        l2 = merge(l2)
        li.clear()
        while len(l1) != 0 and len(l2) != 0:
            if l1[0] < l2[0]:
                li.append(l1[0])
                del l1[0]
            else:
                li.append(l2[0])
                del l2[0]
        if len(l1) != 0:
            li = li + l1
        else:
            li = li + l2
        # print(li)
    return li

def list_split(lx, index1, index2):
    ly = [i for i in lx[index1:index2]]
    # print(ly)
    return ly

# print(merge(rndArray))
rndArray = merge(rndArray)
print(rndArray)

