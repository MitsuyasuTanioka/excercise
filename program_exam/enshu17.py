li = [68, 9, 100, 81]
n = 100
while n != 0:
    for i in range(0, len(li)):
        if int(li[i] / n) >= 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
    n -= 10

for i in range(0, len(li)):
    print("= ", end="")
print()
for i in range(0, len(li)):
    print(i+1, end=" ")
print()


