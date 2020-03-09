from utils import log, random_num

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge

思路：
- 读取数据：
    - 读取 filtered_words.txt：
        - lines
            - line
                - word
                
- 用户输入词语：
    - 打印出 Freedom
    - 打印出 Human Rights
    
-  监听    
"""
from utils import load_lines


def words_from_file(filename):
    file = filename
    lines = load_lines(file)
    words = []
    for i in range(len(lines)):
        word = lines[i].strip('\n')
        words.append(word)
    return words


def bind_input(words):  # input event
    value = input('请不要输入敏感词语>>>')
    if value in words:
        log('Freedom')
        return True
    log('Human Rights')
    return False
    pass


def main():
    file = '../task_else/filtered_words.txt'
    words = words_from_file(file)
    while True:
        bind_input(words)
    pass


if __name__ == '__main__':
    main()
