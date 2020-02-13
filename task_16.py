# pip install xlrd -i https://pypi.tuna.tsinghua.edu.cn/simple
from utils import log
"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>

https://www.cnblogs.com/beginner-boy/p/7239696.html
"""
import xlrd
import xml.dom.minidom as md

def load_file(filename):
    import json
    p = filename
    with  open(p, 'rb') as f:
        data = f.read().decode('utf-8')
    # log('type data', type(data))
    return json.loads(data)


def new_of_sheet(filename):
    file = filename  # 打开指定路径中的xls文件
    student = xlrd.open_workbook(file)  # 得到Excel文件的book对象，实例化对象
    sheet = student.sheet_by_index(0)  # 通过sheet索引获得sheet对象
    return sheet


"""
    data = [
        {
            "Id": 1,
            "Name": 'gua',
            "Math": 103,
            "Chinese": 90,
            "English": 73,
        },
        {
            "Id": 2,
            "Name": 'gua',
            "Math": 103,
            "Chinese": 90,
            "English": 73,
        },
    ]
"""
def row_and_col(sheet):
    row = sheet.nrows  # 获取行总数
    col = sheet.ncols  # 获取列总数
    return (row, col)

def sheet_value(sheet, x, y):
    v = sheet.cell_value(x, y)
    return v

def new_of_student(sheet, col):
    # keys  ['id', 'Name', 'Math', 'Chinese', 'English']
    # keys = []
    # for c in range(col):
    #     v = sheet_value(sheet, 0, c)
    #     keys.append(v)
    stu = {}
    keys = []
    for c in range(col):
        v = sheet_value(sheet, 0, c)
        keys.append(v)
        stu[v] = ''
    return stu, keys


def some_students(sheet, row, col, student):
    list = []
    for i in range(1, row): # 从第二行开始
        stu, keys = student
        for j in range(col):
            k = keys[j]
            v = sheet_value(sheet, i, j)
            stu[k] = v
        list.append(stu)
    return list

def load_students(filename):
    sheet = new_of_sheet(filename)
    (row, col) = row_and_col(sheet)
    log('row', row)
    student = new_of_student(sheet, col)
    students = some_students(sheet, row, col, student)
    return students

def write_to_xml(xlscontent):

    xmlfile = md.Document()    #创建新xml文件

    root = xmlfile.createElement('root') #创建节点
    students = xmlfile.createElement('students') #创建节点

    xmlfile.appendChild(root)  #在文件中添加root节点
    root.appendChild(students) #在root下添加students节点

    comment = xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]') #创建评论
    students.appendChild(comment)  #在students标签下添加comment

    xmlcontent = xmlfile.createTextNode(str(xlscontent))  #创建文本节点
    students.appendChild(xmlcontent)   #在students标签下添加文本内容

    with open('students.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding = 'utf-8')) #写入文件


"""
2020/02/13 15:16:47 stus [{'id': '3', 'Name': '王五', 'Math': '60', 'Chinese': '66', 'English': '68'}, {'id': '3', 'Name': '王五', 'Math': '60', 'Chinese': '66', 'English': '68'}, {'id': '3', 'Name': '王五', 'Math': '60', 'Chinese': '66', 'English': '68'}]
"""

def main():
    filename = "student.xls"
    stus = load_students(filename)
    # log('stus', stus)
    write_to_xml(stus)
    pass


if __name__ == '__main__':
    main()