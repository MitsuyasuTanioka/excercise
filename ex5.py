# (1)
def square(n):
    return n ** 2

print(square(2))
print(square(3))
print("----------------")

# (2)
def mul(a, *args):
    n = a
    for i in args:
        n *= i
    return n

print(mul(1, 2))
print(mul(2, 4, 6))
print(mul(3, 5, 7, 11))
print("----------------")

# (3)
def power(a):
    def inner(x):
        return x ** a
    return inner

power3 = power(3)
power4 = power(4)

print(power3(2))
print(power4(3))
print("----------------")

# (4)
sum = 0
before = sum
while True:
    # try:
    #     n = input("Please input number:")
    #     if isinstance(n, int):
    #         sum += n
    #         print(str(before) + " + " + str(n) + " = " + str(sum))
    #         before = sum
    #     else:
    #         print("Not a number is inputted. Program exit.")
    #         break
    try:
        n = input("Please input number:")
        sum += int(n)
        print(str(before) + " + " + n + " = " + str(sum))
        before = sum
    except:
        print("Not a number is inputted. Program exit.")
        break



