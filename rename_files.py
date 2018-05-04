import os

FILE_PATH = ''

PER = ''


def rename():
    i = 0
    path = FILE_PATH
    file_list = os.listdir(path=path)
    for file in file_list:
        i = i + 1
        old_name = os.path.join(path, file)
        if os.path.isdir(old_name):  # 如果是文件夹则跳过
            continue
        new_name = os.path.join(path, PER + file)
        os.rename(old_name, new_name)
    print("file count is : " + str(i))


if __name__ == '__main__':
    rename()
