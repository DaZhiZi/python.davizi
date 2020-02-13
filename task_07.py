from utils import log

"""
**第 0007 题：**有个目录，里面是你自己写过的程序，
统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。


"""

import os

"""
codes = {
    "code": 50, 
    "blank": 2,
    "note": 3,
}
"""


def load_file(file_path):
    p = file_path
    with  open(p, 'r') as f:
        data = f.read()
    # log('type data', type(data))
    return data


def codes_from_file(dir, filename):
    codes = {
        "code": 0,  # 你写过多少行代码
        "blank": 0,  # 空行
        "note": 0,  # 注释
    }
    path = os.path.join(dir, filename)
    # log('path', path)
    lines = open(path, 'r', encoding="utf-8").readlines()
    # log('lines', lines)
    # lines = load_file(path)
    for line in lines:
        line = line.strip()  # 去掉空格
        if "#" in line:
            codes["note"] += 1
        elif len(line) == 0:
            codes["blank"] += 1
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
        log('end', end)
        if end == 'py':
            code = codes_from_file(dir, file)
            log('code', code)
            codes["code"] += code["code"]
            codes["blank"] += code["blank"]
            codes["note"] += code["note"]
    log('codes', codes)
    return codes


"""
2020/02/12 18:16:49 end txt
2020/02/12 18:16:49 end txt
2020/02/12 18:16:49 end txt
2020/02/12 18:16:49 end py
2020/02/12 18:16:49 code {'code': 45, 'blank': 14, 'note': 9}
2020/02/12 18:16:49 codes {'code': 45, 'blank': 14, 'note': 9}
"""
"""
第 0008 题：一个HTML文件，找出里面的正文。

第 0009 题：一个HTML文件，找出里面的链接。

写了 ：
https://github.com/DaZhiZi/crawler_py
"""

def main():
    dir = 'task_06_txts'
    codes = codes_from_files(dir)
    pass


if __name__ == '__main__':
    main()
