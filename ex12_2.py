import datetime
import os

def listup_old_files(path, n_days):
    datetime_delta = datetime.timedelta(days=n_days)
    now = datetime.datetime.now()
    for i in os.listdir(path):
        path_time = datetime.datetime.fromtimestamp(os.path.getmtime(i))
        if path_time < (now - datetime_delta):
            print(i)

listup_old_files(".", 1)

# current_dir = "."
# # 更新日時を取得
# print(datetime.datetime.fromtimestamp(os.path.getmtime("ex12_1.py")))
# datetime_delta = datetime.timedelta(days=10)
# now = datetime.datetime.now()
# print(f"現在:{now}")
# print(f"10日前:{now - datetime_delta}")
# print(datetime.datetime.fromtimestamp(os.path.getmtime("ex12_1.py"))-datetime_delta)
#
# # 現在のディレクトリのファイル・ディレクトリが載っているリストを表示
# print(os.listdir("."))

