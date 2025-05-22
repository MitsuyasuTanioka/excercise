import os
import shutil

if os.path.isdir("data"):
    print("ディレクトリはすでに存在します")
else:
    os.mkdir("data")

with open("tmp.txt", "w") as f:
    print("", end="", file=f)

shutil.move("tmp.txt", "data")
