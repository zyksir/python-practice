#0000   在图片右上角加上红色的数字
 #_*_ coding:utf-8 _*_
from PIL import Image, ImageDraw, ImageFont

#adout Image
#从原图中选取左上坐标为(100,100),右下坐标为(200,200)的区域
#对其进行旋转\镜像变化操作
#paste:讲图A到原图中对应位置
#resize:等比例缩放
#rotate:旋转XX度
def Image_fun(img):
    box = ( 100,100,200,200 )
    #region = img.crop(box)
    #region = region.transpose(Image.ROTATE_180)
    #img.paste(region,box)
    #tmp = img.resize( (200,200) )
    #tmp = tmp.rotate(45)
    #tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
    #tmp = img.transpose(Image.FLIP_TOP_BOTTOM)

#about ImageDraw
#Draw:create an object that we can oprate
#line:draw a line that start from (100,200) to (300,400)
#we can draw a circle,a chord etc
#text:add something
#and ImageFont is used specially for text,it can deside the wordtype and the word size
def add_num(img):
    draw = ImageDraw.Draw(img)
    #draw.line([100,200,300,400],fillcolor)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "black"#'#000000'
    width, height = img.size
    draw.text((width-40, 0), '90', font=myfont, fill=fillcolor)
    img.save('1result.jpg','jpeg')
    return 0

def main():
    image = Image.open('1image.jpg')#打开图片
    add_num(image)
    #Image_fun(image)
main()