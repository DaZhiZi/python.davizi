from utils import log, random_num, load_lines

"""
第 0012 题： 敏感词文本文件 filtered_words.txt，
里面的内容 和 0011题一样，当用户输入敏感词语，
则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""


def words_from_file(filename):
    file = filename
    lines = load_lines(file)
    words = []
    for i in range(len(lines)):
        word = lines[i].strip('\n')
        words.append(word)
    return words


def join(delimiter, arr):
    r = arr[0]
    for i in range(1, len(arr)):
        a = arr[i]
        r += (delimiter + a)
    log('r', r)
    return r


def split(s, delimiter=' '):
    list = []
    space = len(delimiter)
    start = 0  # 起点
    for i in range(len(s)):
        tmp = s[i: i + space:]
        if tmp == delimiter:
            list.append(s[start: i:])
            start = i + space
    list.append(s[start::])
    log('list', list)
    return list


def replace_all(s, old, new_str):
    r = join(new_str, split(s, old))
    log('r', r)
    return r


def bind_input(words):  # input event
    value = input('请不要输入敏感词语>>>')
    # log('words', words)
    for i in words:
        if i in value:
            # user_input = value.replace(str(i), '*' * len(i))
            # 假如 不使用ｐython 自带replace 内置函数和切片方法
            user_input = replace_all(value, str(i), '*' * len(i))
            log('user_input', user_input)
            return True
    log('value', value)
    return False
    pass


def main():
    file = 'filtered_words.txt'
    words = words_from_file(file)
    while True:
        bind_input(words)
    pass


if __name__ == '__main__':
    main()
