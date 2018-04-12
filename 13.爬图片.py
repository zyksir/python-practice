#!/usr/bin/python
# coding=utf-8

"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
"""

import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def catch_tieba_pics(url,num):
    content = urllib.request.urlopen(url)
    bs = BeautifulSoup(content, 'lxml')
    os.mkdir('pic_download')
    os.chdir(os.path.join(os.getcwd(),'pic_download'))
    for i in bs.find_all('img', {"class": "BDE_Image"}):
        num+=1
        #urllib.request.urlretrieve(i['src'], '%s.jpg' % num)
        download_pic(i['src'],num)
    print('down ' + str(num) + ' pictures in total')


def download_pic(url,num):
    image_content = urllib.request.urlopen(url).read()
    #file_name = os.path.basename(urllib.parse.urlsplit(url)[2])
    file_name = str(num)+'.jpg'
    output = open(file_name, 'wb')
    output.write(image_content)
    output.close()

catch_tieba_pics('http://tieba.baidu.com/p/2166231880',0)
'''
将数据下载到本地
urlretrieve(url,
            filename=None, //本地路径
            reporthook=None, 
            data=None)
'''