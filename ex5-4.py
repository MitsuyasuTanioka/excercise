import time

def deco(func):
    def timeget(*args):
        print("時刻計測開始")
        a = time.perf_counter()
        print("計測開始")
        func(*args)
        print("計測終了")
        b = time.perf_counter()
        result = b - a
        print("result:", result)
        return result
    return timeget

@deco
def funcA(max_range=100000):
    sum = 0
    for i in range(0, max_range):
        sum += i
    print("sum:", sum)

# @deco
# def functime():
#     return 0

# funcA()
funcA()
funcA(10000000)
# print(time.perf_counter())
# print(help(time.perf_counter))
