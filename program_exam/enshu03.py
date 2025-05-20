for i in range(0, 10):
    for j in range(0, 10):
        if i == 0 and j == 0:
            print("", end="\t")
        elif i == 0:
            print(j, end="\t")
        elif j == 0:
            print(i, end="\t")
        elif i*j % 6 == 0:
            print("##", end="\t")
        elif i*j % 2 == 0:
            print("**", end="\t")
        elif i*j % 3 == 0:
            print("@@", end="\t")
        else:
            print(i * j, end="\t")
    print()
