from utils import log


def randomBetween(num1, num2):
    import random
    n = random.randint(num1, num2)
    return n


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

"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中

1. SQLite是一种轻量级的嵌入式数据库，其数据库就是一个文件。Python中内置SQLite3，无需另外安装。

要操作数据库，首先要连接到数据库，连接称作“Connection”。

连接数据库后，需要打开游标，称为“Cursor”，通过“Cursor”执行SQL语句，获得执行结果
"""
"""
 https://www.cnblogs.com/liez/p/5312279.html
"""
import sqlite3  # 连接到SQLite数据库


def create(cur):
    cur.execute('create table if not exists codes(code char(20) primary key)')
    # 用 execute 执行一条 sql 语句
    print('创建成功')


def insert(cur, item):
    cur.execute('insert into codes values (?)', [item])
    print('插入数据成功')


def select(conn):
    sql = '''
    SELECT
        *
    FROM
        codes
    '''
    cur = conn.execute(sql)
    for row in cur:
        print(row)


def save_codes(num):
    codes = generate_codes(num)  # 获取数据

    conn = sqlite3.connect('test.db')  # 数据库文件是test.db  如果文件不存在，会自动在当前目录创建:
    cur = conn.cursor()  # 创建一个 cursor
    create(cur)  # 创建user表

    for code in codes:  # 插入数据
        insert(cur, code)

    select(conn)  # select 函数查询数据

    conn.commit()  # 提交事务: 必须用 commit 函数提交你的修改 否则你的修改不会被写入数据库
    cur.close()  # 关闭 cursor
    conn.close()  # 关闭 connection 用完数据库要关闭


def main():
    num = 200
    save_codes(num)
    pass


if __name__ == '__main__':
    main()
