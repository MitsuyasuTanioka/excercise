def greet(name, time):
    if time == "morning":
        print(name + "さん、おはようございます。")
    elif time == "noon":
        print(name + "さん、こんにちは。")
    elif time == "evening":
        print(name + "さん、こんばんは。")

n = "谷岡 充康"
t = "evening"
greet(n, t)
