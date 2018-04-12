 #_*_ coding:utf-8 _*_
'''
#0008 & 0009:一个HTML文件，找出里面的正文和链接
'''
from bs4 import BeautifulSoup
import re

def find_the_content(path):
	with open(path,encoding='utf-8') as f:
		text = BeautifulSoup(f, 'lxml')
		content = text.get_text().strip('\n')

		return content

def find_the_link(path):
    links = []
    with open(path,encoding='utf-8') as f:
        bs =BeautifulSoup(f,'lxml')
        for i in bs.findAll('a',attrs={'href':re.compile('^')}):
        	links.append(i.get('href'))
    return links

def main():
	print(find_the_link('8.html'))
	print( find_the_content('8.html') )

main()
'''
findAll(name  = '属性名', 
		attrs = '属性', 
		recursive = '是否递归',
		text = '文本内容',
		limit  = '最多返回前几个',
		**kwargs)
'''
