value1 = 50
value2 = 25
value3 = 1

while value3 != 0:
    value3 = value1 % value2
    value1 = value2
    value2 = value3

print("最大公約数:" + str(value1))

