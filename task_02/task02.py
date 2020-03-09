from utils import log

"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？

首先要弄清楚激活码的构成，不同软件应用生成的激活码都不同，但相同的是，

生成的激活码是字母和数字的随机组合，可能是大写，也可能是小写，
所以激活码是26个大小写字母和10个数字的随机组合。
以生成一个16位的激活码（区分大小写）为例，
必然会用到python 的random模块，可以将26个大小写字母和10个数字放在一个集合中，
用random随机去取集合中的元素。

生成 200 个激活码:
    生成 1 个激活码
            生成 16 位字符:
                生成 1 位字符：
                    - 字母
                        - 大写
                        - 小写
                    - 数字
                    
                    
random.randint(a,b)：用于生成一个指定范围内的整数。
其中参数a是下限，参数b是上限，生成的随机数n：a<=n<=b
2020/03/02 21:56:28 codes ['M9yavJZpDDN9QC3u', '87LFNnlgWypCg2sK', '0f0kTMkpShpZbPuI', 'NC2aZtyfBSAPRtqk', 'FJcZX1Zgb5Qgbc7B', '8XEwfHz33Gvspn8F', 'dgQI0WLacLKxknmo', 'tGK7yvyyQd1uxRHO', 'GOIE4dCwi7Zgwxqf', 'rmn8DYlHGIFFksu7', 'tq1NMffpqG9ueJ2z', 'v7Rds6kORHsoFjdY', 'kWT5AKoofsmcnLrc', 'QNn8h0gxuj1uI0LO', 'GHBaXXk8LtqjpGrU', 'eQofbuBUJY2rUFGH', 'RwO9lTl2kyq6Bj5X', 'PcjjsC5IsZTGiXyn', 'oMOliCLEOCX0bHAX', 'FeD474HnRAtlmg2D']

"""


def generate_char():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    r = lower + upper + num
    l = len(r) - 1
    import random
    n = random.randint(0, l)
    char = r[n]
    return char


def generate_code():  # 生成 1 个激活码
    chars = ''
    for i in range(16):
        char = generate_char()
        chars += char
    return chars


def generate_codes(num):  # 生成 num 个激活码
    codes = []
    for i in range(num):
        code = generate_code()
        codes.append(code)
    return codes


def main():
    num = 20
    codes = generate_codes(num)
    log('codes', codes)
    pass


if __name__ == '__main__':
    main()
