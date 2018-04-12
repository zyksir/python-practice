#!/usr/bin/python
# coding=utf-8

"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，
然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。
写代码，对每月通话时间做个统计。
此处改为统计流量
"""
import xlrd

def save_number_info(path):
    excel = xlrd.open_workbook(path)
    sheet = excel.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    total = 0
    print( sheet.row(1) )
    print( sheet.row_slice(1) )
    print( sheet.cell_type(1,1) )
    for i in range(1,nrows):
        total += int(sheet.cell_value(i,6))
    print('本月已用流量'+str(total//1024)+'M')



def main():
    save_number_info(r'.\__pycache__\201802.xls')

main()

'''
xlrd:excel操作模块

ctype:  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

获取工作表：
data.sheets()[0]
data.sheet_by_index(sheet_indx))
data.sheet_by_name(sheet_name))
其他：
data.sheet_names()[0]

行的操作：列的操作同理
nrows = table.nrows  #获取该sheet中的有效行数
table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
table.row_len(rowx) #返回该列的有效单元格长度

单元格的操作
table.cell(rowx,colx)   #返回单元格对象
table.cell_type(rowx,colx)    #返回单元格中的数据类型
table.cell_value(rowx,colx)   #返回单元格中的数据
table.cell_xf_index(rowx, colx)   # 暂时还没有搞懂
'''
