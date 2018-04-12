#!/usr/bin/python
# coding=utf-8

"""
第 0017 题(0018,0019)： 将第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
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
"""
import xlrd
from lxml import etree


def get_xls_data(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    content = {}
    for i in range(sheet.nrows):
        content[i + 1] = sheet.row_values(i)[1:]
    return content

def read_excel(filename):
    excel = xlrd.open_workbook(filename)
    sheet = excel.sheet_by_index(0)
    '''
    data  = {}
    for i in range(sheet.nrows):
        data[sheet.row_values(i)[0]] = sheet.row_values(i)[1:]
    '''
    data  = []
    for i in range(sheet.nrows):
        temp = [ int(x) for x in sheet.row_values(i) ]
        data.append(temp)
    return data

def save_to_xml(data,new_filename):
    root = etree.Element('root')
    students = etree.SubElement(root,'students')
    #students.append(etree.Comment(u"""学生信息表 "id" : [名字, 数学, 语文, 英文]"""))
    #students.append(etree.Comment(u"城市信息"))
    students.append(etree.Comment(u"数字信息"))
    students.text = str(data)

    xml = etree.ElementTree(root)
    xml.write(new_filename, pretty_print = True, xml_declaration = True,encoding = 'utf-8')

def main():
    content = read_excel(r'.\__pycache__\number.xls')
    save_to_xml(content,r'.\__pycache__\number.xml')

main()