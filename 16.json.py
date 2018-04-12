#!/usr/bin/python
# coding=utf-8

"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]
"""
import xlwt
import json

def save_number_info(path, excel_name):
    with open(path,'r') as f:
        text = f.read()
        content = json.loads(text)
        #content = json.load(f)
    Workbook = xlwt.Workbook()
    ws = Workbook.add_sheet('numbers',cell_overwrite_ok=True)
    row = 0
    col = 0
    for i in content:
        for k in i:
            ws.write(row,col,k)
            col+=1
        row += 1
        col = 0
    Workbook.save(excel_name)


def main():
    save_number_info(r'.\__pycache__\number.txt',r'.\__pycache__\number.xls')

main()

'''
json模块：字符串和python数据类型间进行转换
dumps把数据类型转换成字符串
dump把数据类型转换成字符串并存储在文件中
loads把字符串转换成数据类型
load把文件打开从字符串转换成数据类型
'''