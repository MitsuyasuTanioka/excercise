li = [68, 9, 100, 81]

for i in range(0, len(li)):
    print(str(i+1) + " :", end="")
    for j in range(0, int(li[i]/10)):
        print("*", end="")
    print()

