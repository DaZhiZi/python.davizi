from utils import log
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 
里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：

"""
import xlwt
# pip install xlwt -i https://pypi.tuna.tsinghua.edu.cn/simple

'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
默认是ascii。当然要记得在文件头部添加：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
style_compression:表示是否压缩，不常用。
'''

def load_file(filename):
    import json
    p = filename
    with  open(p, 'rb') as f:
        data = f.read().decode('utf-8')
    # log('type data', type(data))
    return json.loads(data)


def load_students(filename):
    data = load_file(filename)
    # log('data', data)
    students = []
    # 第一行
    # {'id': ['Name', 'Math','Chinese' , 'English']}
    inform = {'id': ['Name', 'Math','Chinese' , 'English']}
    students.append(inform)
    for k, v in data.items():
        stu = {}
        stu[k] = v
        students.append(stu)
    return students

def new_of_xls(sheetname):
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    student = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
    sheet = student.add_sheet(sheetname, cell_overwrite_ok=True)
    return (student, sheet)

def wirte_of_students(students, sheet):
    for i in range(len(students)):
        row = students[i]
        for k, v in row.items():
            sheet.write(i, 0, str(k))
            col = v
            log('col', col)
            for j in range(len(col)):
                inform = str(col[j])
                sheet.write(i, j+1, inform)


def save_students():
    filename = 'student.txt'
    students = load_students(filename)
    # log('students', students)
    (student, sheet) = new_of_xls(sheetname='student')
    wirte_of_students(students, sheet)
    student.save('student.xls')


def main():
    save_students()
    pass


if __name__ == '__main__':
    main()