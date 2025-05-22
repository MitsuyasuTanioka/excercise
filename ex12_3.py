import os

def empty_rmdir(path, rmdir_count):
    for entry in os.listdir(path):
        # print(entry)
        fullpath = os.path.join(path, entry)
        if os.path.isdir(fullpath):
            if len(os.listdir(fullpath)) == 0:
                print(f"{fullpath}を削除")
                os.rmdir(fullpath)
                rmdir_count += 1
            else:
                rmdir_count = empty_rmdir(fullpath, rmdir_count)
                if len(os.listdir(fullpath)) == 0:
                    print(f"{fullpath}を削除")
                    os.rmdir(fullpath)
                    rmdir_count += 1
    return rmdir_count

rmdir_count = 0
rmdir_count = empty_rmdir(".", rmdir_count)
print(f"削除したディレクトリ数: {rmdir_count}")
