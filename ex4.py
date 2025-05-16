# (1)
prob = 79
money = 4999

if prob >= 80:
    print("天気が悪いので今日は家で過ごしましょう")
elif prob >= 40 and money >= 5000:
    print("雨が降りそうなので今日は映画を見に行きましょう")
elif prob < 40 and money >= 5000:
    print("天気がいいので今日は遠出しましょう")
else:
    print("今日は近場で遊びましょう")

# (2)
n = 1
sum = 0
while n <= 100:
    sum += n
    n += 2
print("合計:" + str(sum))

# (3)
sum = 0
for i in range(1, 100, 2):
    sum += i
print("合計:" + str(sum))

# (4)
print([i for i in range(1, 11) if i%2 == 0])
