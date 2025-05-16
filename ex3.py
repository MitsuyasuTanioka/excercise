# (1)
a = [10, 8, 12, 17, 5]
print(a)

# (2)
print(a[len(a)-1:])

# (3)
a.append(13)
print(a)

# (4)
b = sorted(a)
print(b)
print(a)

# (5)
d = {"dog": "犬", "cat": "猫", "bird": "鳥"}
print(d)

# (6)
print(d.get("cat"))

# (7)
print('monkey' in d)
d["monkey"] = "猿"
print(d)
print("monkey" in d)
