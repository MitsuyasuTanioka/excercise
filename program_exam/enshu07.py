target = 42
flag = False

if target % 2 == 0:
    if target % 3 == 0:
        if target % 5 != 0:
            flag = True
        else:
            if target % 7 == 0:
                flag = True
    else:
        if target % 5 != 0:
            flag = True
else:
    if target % 3 == 0:
        if target % 5 == 0:
            flag = True
        else:
            if target % 7 != 0:
                flag = True
    else:
        if target % 5 != 0:
            if target % 7 != 0:
                flag = True

if flag:
    print("◎")
else:
    print("×")
