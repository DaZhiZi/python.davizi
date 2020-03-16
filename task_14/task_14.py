from utils import log
"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，如下图所示：

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


def load_citys(filename):
    data = load_file(filename)
    # log('data', data)
    students = []
    # 第一行
    # {'id': ['Name', 'Math','Chinese' , 'English']}
    inform = {'id': "city"}
    students.append(inform)
    for k, v in data.items():
        stu = {}
        stu[k] = v
        students.append(stu)
    return students

'''
2020/03/16 13:26:10 
citys [
   {
        'id': 'city'
   },
   {
        '1': '上海'
   },
   {
        '2': '北京'
   },
   {
         '3': '成都'
   },
]
'''

# citys = [
#     {
#         'id': ['city','jkdu', 'wwdu']
#     },
# ]
def new_of_xls(sheetname):
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    city = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
    sheet = city.add_sheet(sheetname, cell_overwrite_ok=True)
    return (city, sheet)

def wirte_of_citys(students, sheet):
    for i in range(len(students)):
        row = students[i]
        for k, v in row.items():
            sheet.write(i, 0, str(k))
            col = v
            log('col', col)
            sheet.write(i, 1, str(col))


def save_citys(read_file, save_file):
    citys = load_citys(read_file)
    log('citys', citys)

    (city, sheet) = new_of_xls(sheetname='city')

    wirte_of_citys(citys, sheet)

    city.save(save_file)



def main():
    read_file = '../task_else/city.txt'
    save_file = 'city.xls'
    save_citys(read_file, save_file)
    pass


if __name__ == '__main__':
    main()