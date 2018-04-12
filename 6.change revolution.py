#0005   你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
 #_*_ coding:utf-8 _*_
'''
with ... as ... : can handle expection
im.thumbnail( (w,h) ):分别对应着缩略图的宽高，在缩略时，函数会保持图片的宽高比例。
            如果输入的参数宽高和原图像宽高比不同，则会依据最小对应边进行原比例缩放。

'''
from PIL import Image
import os
def change_revolution(path):
    for picname in os.listdir(path):
        picpath = os.path.join( path,picname )
        with Image.open(picpath) as im:
            w,h = im.size
            n = w/1366 if (w/1366) >= (h/640) else h/640
            if n == 0:
                n = 1
            im.thumbnail( (w/n,h/n) )
            im.save("changed"+picname.split('.')[0]+'.jpg' ,'jpeg')
            print("save" + "changed"+picname.split('.')[0]+'jpg' )


def main():
    change_revolution('D:\pycharm+sublime+vscode\Python_Cache\pic')
main()

'''
os.path.getsize()
os.path.join(path, name): connect path and name 
    -->os.path.basename(path) return name
    -->os.path.dirname(path) retune path
    -->os.path.split(path)  return (path,name)
os.listdir() return a list
'''