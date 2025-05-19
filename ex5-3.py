def get_max(*args):
    if len(args) == 0:
        return 0
    max = args[0]
    for i in args:
        if max < i:
            max = i
    return max

print(get_max(1, 2, 3, 5, 4))
print(get_max())
