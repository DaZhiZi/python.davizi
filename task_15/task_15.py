from utils import log
"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
id: [num1, num2, num2]

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

"""
import re
import xlwt


def load_file(filename):
    import json
    p = filename
    with  open(p, 'rb') as f:
        data = f.read().decode('utf-8')
    # log('type data', type(data))
    return json.loads(data)


def load_numbers(filename):
    data = load_file(filename)
    # log('data', data)
    students = []
    # 第一行
    # {'id': ['Name', 'Math','Chinese' , 'English']}  这里可以直接当作参数
    inform = {'id': ['num1', 'num2', 'num3']}
    students.append(inform)
    i = 0
    for v in data:
        stu = {}
        k = str(i+1)
        stu[k] = v
        students.append(stu)
        i += 1
    log('students', students)
    return students

def new_of_xls(sheetname):
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    number = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
    sheet = number.add_sheet(sheetname, cell_overwrite_ok=True)
    return (number, sheet)


def wirte_of_numbers(students, sheet):
    for i in range(len(students)):
        row = students[i]
        for k, v in row.items():
            sheet.write(i, 0, str(k))
            col = v
            log('col', col)
            for j in range(len(col)):
                inform = str(col[j])
                sheet.write(i, j + 1, inform)


def save_numbers(read_file, save_file):
    numbers = load_numbers(read_file)
    # log('students', students)

    (city, sheet) = new_of_xls(sheetname='city')

    wirte_of_numbers(numbers, sheet)

    city.save(save_file)



def main():
    read_file = 'number.txt'
    save_file = 'number.xls'
    save_numbers(read_file, save_file)
    pass


if __name__ == '__main__':
    main()