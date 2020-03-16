# pip install xlrd -i https://pypi.tuna.tsinghua.edu.cn/simple
from utils import log
"""
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
	城市信息
-->
{
	"1" : "上海",
	"2" : "北京",
	"3" : "成都"
}
</citys>
</root>
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
    # keys  ['id', 'city']
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

def copy_dict(map):
    o = map
    new_obj = {}
    for k, v in o.items():
        new_obj[k] = v
    return new_obj
    pass


def some_students(sheet, row, col, student):
    list = []
    for i in range(1, row): # 从第二行开始
        stu, keys = student
        s = copy_dict(stu)
        for j in range(col):
            k = keys[j]
            v = sheet_value(sheet, i, j)
            s[k] = v
        list.append(s)
    return list


def load_students(filename):
    sheet = new_of_sheet(filename)
    (row, col) = row_and_col(sheet)
    log('row', row)
    student = new_of_student(sheet, col)
    students = some_students(sheet, row, col, student)
    log('citys', students)
    return students

def write_to_xml(xlscontent):

    xmlfile = md.Document()    #创建新xml文件

    root = xmlfile.createElement('root') #创建节点
    students = xmlfile.createElement('citys') #创建节点

    xmlfile.appendChild(root)  #在文件中添加root节点
    root.appendChild(students) #在root下添加students节点

    comment = xmlfile.createComment('城市信息 ') #创建评论
    students.appendChild(comment)  #在students标签下添加comment

    xmlcontent = xmlfile.createTextNode(str(xlscontent))  #创建文本节点
    students.appendChild(xmlcontent)   #在students标签下添加文本内容

    with open('city.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding = 'utf-8')) #写入文件



'''
2020/03/16 14:21:37 citys [
  {'id': '1', 'city': '上海'},
  {'id': '2', 'city': '北京'},
  {'id': '3', 'city': '成都'}
]
'''
def main():
    filename = "../task_else/city.xls"
    stus = load_students(filename)
    # log('stus', stus)
    write_to_xml(stus)
    pass


if __name__ == '__main__':
    main()