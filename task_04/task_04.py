from utils import log, load_file, lower_case1
"""
**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
文件:
Hello i am davizi
l love you
思路：
    - 读取数据
    - 转换小写：
        - 转换成   [hello i am davizi, i love you]
            - 转换成   [hello, i, am, davizi, i, love, you]
                - 转换 ｛
                    "hello": 1,
                    "i": 2,
                    ....
                ｝       
"""
def lines_from_data(data):  # [hello i am davizi, i love you]
    lines = data.split('\n')
    # log('lines', lines)
    return lines

def words_from_lines(lines):  # [hello, i, am, davizi, i, love, you]
    l = []
    for line in lines:
        words = line.split(' ')
        for word in words:
            l.append(word)
    return l
    pass

# 'word': num,  key: value
def map_from_list(words):
    map = {}
    for w in words:
        if w in map:
            map[w] += 1
        else:
            map[w] = 1
    return map

def words_num_from_file(filepath):
    r = {}
    data = load_file(filepath)
    d = lower_case1(data)
    l = lines_from_data(d)
    words = words_from_lines(l)
    r = map_from_list(words)
    return r
""" 2020/02/12 14:02:45
words_num {
    'hello': 1, 
    'i': 1, 
    'am': 1, 
    'davizi': 1, 
    'l': 1, 
    'love': 1,
    'you': 1
 }

"""
def main():
    filepath = './task_04.txt'
    words_num = words_num_from_file(filepath)
    log('words_num', words_num)
    pass


if __name__ == '__main__':
    main()