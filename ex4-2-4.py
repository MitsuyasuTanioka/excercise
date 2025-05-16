students_data = [
    {"name": "A", "math": 85, "english": 92, "science": 78},
    {"name": "B", "math": 70, "english": 81, "science": 88},
    {"name": "C", "math": 95, "english": 88, "science": 92},
    {"name": "D", "math": 60, "english": 75, "science": 70},
    {"name": "E", "math": 88, "english": 90, "science": 85},
]

ave = 0
for i in range(0, 5):
    ave += students_data[i]["math"]
ave /= 5
print("平均点:" + str(ave))

max_i = 0
for i in range(0, 5):
    if max_i < students_data[i]["science"]:
        max_i = i
print("名前:" + students_data[max_i]["name"] + " 点数:" + str(students_data[max_i]["science"]))


n = 0
for i in range(0, 5):
    n = students_data[i]["math"] + students_data[i]["english"] + students_data[i]["science"]
    students_data[i]["total"] = n
print(students_data)
