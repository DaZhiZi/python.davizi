from utils import log

"""
**第 0007 题：**有个目录，里面是你自己写过的程序，
统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。


"""

from utils import load_file, lower_case1
import os

"""
codes = {
    "code": 50, 
    "blank": 2,
    "note": 3,
}
"""


def codes_from_file(dir, filename):
    codes = {
        "code": 0,  # 你写过多少行代码
        "blank": 0,  # 空行
        "note": 0,  # 注释
    }
    path = os.path.join(dir, filename)
    lines = load_file(path)
    for line in lines:
        line = line.strip()  # 去掉空格
        if len(line) == 0:
            codes["note"] += 1
        elif line[0] == "#":
            codes["note"] += 1
        else:
            codes["code"] += 1
    return codes


def codes_from_files(dir):
    codes = {
        "code": 0,  # 你写过多少行代码
        "blank": 0,  # 空行
        "note": 0,  # 注释
    }

    files = os.listdir(dir)
    for file in files:
        end = file[file.find('.') + 1::]  # 有可能 文件名 不止一个点 .  我们可以判断后三位 ".py"
        if end == 'py':
            code = codes_from_file(dir, file)
            log('code', code)
            codes["note"] += code["note"]
            codes["blank"] += code["blank"]
            codes["blank"] += code["blank"]
    log('codes', codes)
    return codes


def main():
    dir = 'python_tasks'
    codes = codes_from_files(dir)
    pass


if __name__ == '__main__':
    main()