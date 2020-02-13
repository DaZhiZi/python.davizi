import time


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def ensure(condition, message):
    if not condition:
        log('xxxxx 测试失败', message)
    else:
        log('>>>>> 测试成功', message)


def isEquals(a, b, message):
    import json
    if json.dumps(a) == json.dumps(b):
        log('***  {} 测试成功, 大侄子牛逼呀'.format(message))
    else:
        log('xxxxx 测试失败 结果（{}）  预期（{}）, {}'.format(a, b, message))


import random


def random_num(num1, num2):
    return random.randint(num1, num2)


def exchange(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

"""
    s1 s2 都是 string
    但 s2 的长度是 1

    返回 s2 在 s1 中的下标, 从 0 开始, 如果不存在则返回 -1
"""


def find(s1, s2):
    index = -1
    for i in range(len(s1)):
        if s1[i] == s2:
            index = i
            break
    # log('index', index)
    return index


def test_find():
    msg = 'find'
    isEquals(find('gua', 'a'), 2, msg)


"""
下面给出一个例子作为后面作业的参考
返回字符串的小写形式的函数
注意, 这里假设了 s 字符串全是大写字母

"""


def lower_case(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        u = lower[find(upper, s)]
        result += u
    log('result', result)
    return result


def test_lower_case():
    msg = 'lower_case'
    isEquals(lower_case('GUA'), 'gua', msg)


"""
定义一个函数
参数是一个字符串 s
返回大写后的字符串
注意, 假设 s 字符串全是小写字母

注意, 自行实现测试函数, 之后的题目都要求自行实现测试函数
"""


def upper_case(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        u = upper[find(lower, s)]
        result += u
    log('result', result)
    return result


def test_upper_case():
    msg = 'upper_case'
    isEquals(upper_case('gua'), 'GUA', msg)


"""
实现 lowercase1
它能正确处理带 小写字母 的字符串
"""


def lower_case1(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        if s in upper:
            u = lower[find(upper, s)]
            result += u
        else:
            result += s
    # log('result', result)
    return result


def test_lower_case1():
    msg = 'lower_case1'
    isEquals(lower_case1('xiao-gUA'), 'xiao-gua', msg)


"""
实现 uppercase1
它能正确处理带 大写字母 的字符串
"""


def upper_case1(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(len(str)):
        s = str[i]
        if s in lower:
            u = upper[find(lower, s)]
            result += u
        else:
            result += s
    log('result', result)
    return result


def test_upper_case1():
    msg = 'upper_case1'
    isEquals(upper_case1('xiao-gUA'), 'XIAo-GUA', msg)



def load_file(file_path):
    p = file_path
    with  open(p, 'r') as f:
        data = f.read()
    # log('type data', type(data))
    return data

def floor(num):
    import math
    return math.floor(num)

def abs(num):
    if num < 0:
        return -num
    return num

def load_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        return data