def func1(x, y):
    z = ""
    if x == 0:
        return z

    match x:
        case 1:
            z = "一"
        case 2:
            z = "二"
        case 3:
            z = "三"
        case 4:
            z = "四"
        case 5:
            z = "五"
        case 6:
            z = "六"
        case 7:
            z = "七"
        case 8:
            z = "八"
        case 9:
            z = "九"

    if y != 0 and y % 8 == 0:
        z = z + "億"
    elif y != 0 and y % 4 == 0:
        z = z + "万"
    elif y % 4 == 1:
        if x != 1:
            z = z + "十"
        else:
            z = "十"
    elif y % 4 == 2:
        if x != 1:
            z = z + "百"
        else:
            z = "百"
    elif y % 4 == 3:
        if x != 1:
            z = z + "千"
        else:
            z = "千"

    return z


import random

arabia = random.randint(0, 2000000000)
arabia = 1500001004
print("整数:", arabia)
arabia_tmp = arabia
message = ""

flag = True
count = 0

while flag:
    # print(arabia_tmp)
    n = arabia_tmp % 10
    message = func1(n, count) + message
    if arabia_tmp < 10:
        flag = False
        break
    arabia_tmp = int(arabia_tmp / 10)
    count += 1


tmp = 0
# while i != 0:
#     tmp = arabia / 10 ^ i
#     if 0 <= tmp <= 9:
#        ans = func1(tmp)
#     i -= 1
#     print(ans)
print(message)


