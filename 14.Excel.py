#!/usr/bin/python
# coding=utf-8

"""
第 0014 题：纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
第 0015 题：纯文本文件 city.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
"""
import xlwt
import re

def save_student_info(path):
    data_table = xlwt.Workbook(encoding='utf-8')
    new_excel = data_table.add_sheet('stduent', cell_overwrite_ok=True)
    with open(path) as f:
        input = f.read()
        info = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)]')
        row = 0
        for i in info.findall(input):
            for j in range(len(i)):
                new_excel.write(row, j, i[j])
            row += 1
    data_table.save(r'.\__pycache__\student.xls')

def save_city_info(path):
    data_table = xlwt.Workbook(encoding='utf-8')
    new_excel = data_table.add_sheet('city', cell_overwrite_ok=True)
    with open(path) as f:
        input = f.read()
        info = re.compile(r'"(\d+)".*?"(.*?)"')
        row = 0
        for i in info.findall(input):
            for j in range(len(i)):
                new_excel.write(row, j, i[j])
            row += 1
    data_table.save(r'.\__pycache__\city.xls')

def main():
    save_student_info(r'.\__pycache__\student.txt')
    save_city_info(r'.\__pycache__\city.txt')

main()

'''
xlwt：Excel 读写：
f = xlwt.Wordbook()
sheet1 = f.add_sheet(u'sheet1',cell_overwrite = True) #后一个参数代表是否覆盖原单元格内容
sheet1.write(0,0,'some text') #(r1,c1)
f.save('test1.xls')

字体风格设置：
style = xlwt.XFSstyle()
font = xlwt.Font()
font.name = 'Tahoma'
font.bold = True
font.italic = True
font.underline = True
style.font = font
sheet.write(r, c,text, style )

合并单元格：
write_merge(self, r1, r2, c1, c2, label="", style=Style.default_style)
'''