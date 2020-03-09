""""
**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词。

思路: 一个目录都是 txt文件：
            读取多个 txt文件：
                读取一个 txt文件：
                    - task_04.py 中写过这个函数   返回结果是  word: times  单词 ： 出现的次数
                    - 获取 读出字典内的最大值并提取相应的单词
"""
from utils import log, load_file, lower_case1
import os


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
"""
{
    "love": 2,
    "i": 3,
}
"""
def map_from_words(words):
    map = {}
    for w in words:
        if w in map:
            map[w] += 1
        else:
            map[w] = 1
    return map


"""
[
    {
    "word": 'love',
    "time":  2,
    },
    {
    "word": 'str',
    "time":  2,
    },
]
"""
def list_from_map(map):
    list = []
    for k, v in map.items():
        m = {}
        m["word"] = k
        m["time"] = v
        list.append(m)
    return list


def words_from_file(filepath):
    data = load_file(filepath)

    d = lower_case1(data)

    l = lines_from_data(d)

    words = words_from_lines(l)

    map = map_from_words(words)

    list = list_from_map(map)

    return list


def keyword_from_file(dir, filename):
    # key: word  value: times
    path = os.path.join(dir, filename)
    words = words_from_file(path)
    log('words', words)
    word = words[0]
    max_time = words[0]["time"]
    for i, w in enumerate(words):
        time = w["time"]
        if max_time < time:
            word = words[i]
            max_time = time
    return word


def keywords_from_file(dir):
    list = []
    files = os.listdir(dir)
    for file in files:
        keyword = keyword_from_file(dir, file)
        # log('keyword', keyword)
        list.append(keyword)
    return list

"""
bug 
2020/02/12 16:27:21 r
 [
    {'word': 'out.', 'time': 1}, 
    {'word': "we're", 'time': 1},
    {'word': 'people?', 'time': 1}
 ]
 
 right
 2020/03/06 18:50:48 r [
     {'word': 'davizi', 'time': 3},
     {'word': 'programmers', 'time': 3},
     {'word': 'it', 'time': 7}
   ]

"""
def main():
    dir = '../task_06_txts'
    r = keywords_from_file(dir)
    log('r', r)
    pass


if __name__ == '__main__':
    main()
