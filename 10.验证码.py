 #_*_ coding:utf-8 _*_
'''
#0010 :验证码生成
'''
from PIL import Image, ImageDraw, ImageFont,ImageFilter
import random,string

def rndColor_255():
	return  ( random.randint(0,255),random.randint(0,255),random.randint(0,255) )

def rndColor_127():
	return  ( random.randint(0,127),random.randint(0,127),random.randint(0,127) )

def create_verification_code():
	width = 240
	height = 60
	chars = string.digits + string.ascii_letters
	img = Image.new(mode = 'RGB',size=(width,height),color=(255,255,255))
	draw = ImageDraw.Draw(img,mode = 'RGB')
	myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
	for x in range(width):
		for y in range(height):
			draw.point( (x,y),fill = rndColor_255()  )
	for i in range(5):
		char = random.choice(chars)
		draw.text( [i*60 + 10,5],char,font=myfont,color=rndColor_127() )
	img = img.filter( ImageFilter.CONTOUR )
	img = img.filter( ImageFilter.BLUR )
	img = img.filter( ImageFilter.MinFilter(size = 5) )
	img.save('10.jpg','jpeg')
	img.show('10.jpg')

def main():
	create_verification_code()

main()

'''
about ImageFilter:
• BLUR：模糊滤波
• CONTOUR：轮廓滤波
• DETAIL：细节滤波
• EDGE_ENHANCE：边界增强滤波
• EDGE_ENHANCE_MORE：边界增强滤波（程度更深）
• EMBOSS：浮雕滤波
• FIND_EDGES：寻找边界滤波
• SMOOTH：平滑滤波
• SMOOTH_MORE：平滑滤波（程度更深）
• SHARPEN：锐化滤波
• GaussianBlur(radius=2)：高斯模糊
	>radius指定平滑半径。
• UnsharpMask(radius=2, percent=150, threshold=3)：反锐化掩码滤波
	>radius指定模糊半径；
	>percent指定反锐化强度（百分比）;
	>threshold控制被锐化的最小亮度变化。
• Kernel(size, kernel, scale=None, offset=0)：核滤波
	当前版本只支持核大小为3x3和5x5的核大小，且图像格式为“L”和“RGB”的图像。
	>size指定核大小（width, height）；
	>kernel指定核权值的序列；
	>scale指定缩放因子；
	>offset指定偏移量，如果使用，则将该值加到缩放后的结果上。
• RankFilter(size, rank)：排序滤波
	>size指定滤波核的大小；
	>rank指定选取排在第rank位的像素，若大小为0，则为最小值滤波；若大小为size * size / 2则为中值滤波；若大小为size * size - 1则为最大值滤波。
• MedianFilter(size=3)：中值滤波
	>size指定核的大小
• MinFilter(size=3)：最小值滤波器
	>size指定核的大小
• MaxFilter(size=3)：最大值滤波器
	>size指定核的大小
• ModeFilter(size=3)：波形滤波器
选取核内出现频次最高的像素值作为该点像素值，仅出现一次或两次的像素将被忽略，若没有像素出现两次以上，则保留原像素值。
	>size指定核的大小
'''