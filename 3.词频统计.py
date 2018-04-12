 #0004 任一个英文的纯文本文件，统计其中的单词出现的个数。
 #_*_ coding:utf-8 _*_
import re
from operator import itemgetter, attrgetter
def replace_with_blank(line):
    for ch in line:
        if ch in "!~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, " ")
    return line

def main():
    words={}
    filename = "3book.txt"
    infile = open(filename,'r')
    text = infile.read()
    #print(text)
    word_list = re.findall(r'[a-zA-Z0-9]+',text)
    for word in word_list:
        if word in words:
            words[word]+=1
        else:
            words[word]=1
    
    #sorted_words = sorted(words.items(),key = lambda d :d[1],reverse= True)
    sorted_words = sorted( words.items(), key=itemgetter(1,0) )
    print("the most immportant word is :"+sorted_words[0][0])
    for key, value in words.items():
        print('%s:%s'%(key,value))
main()

'''
文件操作：
open(path,mode)
file.read(num):读取num个字符，缺省为全部读取
file.close()
import os
os.mkdir(dir_name)/os.rmdir(dir_name)
os.rename(current_file_name,new_file_name)
os.remove(file_name)
'''

'''
import turtle 
##全局变量##
#词频排列显示个数
count = 10
#单词频率数组-作为y轴数据
data = []
#单词数组-作为x轴数据
words = []
#y轴显示放大倍数-可以根据词频数量进行调节
yScale = 6
#x轴显示放大倍数-可以根据count数量进行调节
xScale = 30
################# Turtle Start  ####################  
#从点(x1,y1)到(x2,y2)绘制线段
def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto (x1, y1)
    t.pendown()
    t.goto (x2, y2)

# 在坐标(x,y)处写文字
def drawText(t, x, y, text):
    t.penup()
    t.goto (x, y)
    t.pendown()
    t.write(text)
 
def drawGraph(t):
    #绘制x/y轴线
    drawLine (t, 0, 0, 360, 0)
    drawLine (t, 0, 300, 0, 0)
 
    #x轴: 坐标及描述
    for x in range(count):
        x=x+1 #向右移一位,为了不画在原点上
        drawText(t, x*xScale-4, -20, (words[x-1]))
        drawText(t, x*xScale-4, data[x-1]*yScale+10, data[x-1])
    drawBar(t)
 
#绘制一个柱体
def drawRectangle(t, x, y):
    x = x*xScale
    y = y*yScale#放大倍数显示
    drawLine(t, x-5, 0, x-5, y)
    drawLine(t, x-5, y, x+5, y)
    drawLine(t, x+5, y, x+5, 0)
    drawLine(t, x+5, 0, x-5, 0)
     
#绘制多个柱体
def drawBar(t):
    for i in range(count):
        drawRectangle(t, i+1, data[i])    
################# Turtle End  ####################
 
         
#对文本的每一行计算词频的函数
def processLine(line, wordCounts):
    #用空格替换标点符号
    line = replacePunctuations(line)
   #从每一行获取每个词
    words = line.split() 
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
         	wordCounts[word] = 1
 
#空格替换标点的函数
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, " ")
    return line
def main():
    #用户输入一个文件名
    filename = input("enter a filename:")#.strip()
    infile = open(filename, "r")
     
    #建立用于计算词频的空字典
    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)
         
    #从字典中获取数据对
    pairs = list(wordCounts.items())
 
    #列表中的数据对交换位置,数据对排序
    items = [[x,y] for (y,x)in pairs] 
    items.sort() 
 
    #输出count个数词频结果
    for i in range(len(items)-1, len(items)-count-1, -1):
        print(items[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
         
    infile.close()
     
    #根据词频结果绘制柱状图
    turtle.title('词频结果柱状图')
    turtle.setup(900, 750, 0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawGraph(t)

about turtle:
画布(canvas)
turtle.screensize(800, 600, "green")
turtle.screensize() #返回默认大小(400, 300)

画笔控制命令:
turtle.down() #移动时绘制图形,缺省时也为绘制
turtle.up() #移动时不绘制图形
turtle.pensize(width) #绘制图形时的宽度
turtle.color(colorstring) #绘制图形时的颜色
turtle.fillcolor(colorstring) #绘制图形的填充颜色
turtle.fill(Ture)turtle.fill(false)

运动命令:turtle.forward(degree) #向前移动距离degree代表距离
turtle.backward(degree) #向后移动距离degree代表距离
turtle.right(degree) #向右移动多少度
turtle.left(degree) #向左移动多少度
turtle.goto(x,y) #将画笔移动到坐标为x,y的位置
turtle.stamp() #复制当前图形
turtle.speed(speed) #画笔绘制的速度范围[0,10]整数
turtle.clear() 清空turtle画的笔迹
turtle.reset() 清空窗口，重置turtle状态为起始状态
turtle.undo()  (未测试)撤销上一个turtle动作 
turtle.isvisible() (未测试)返回当前turtle是否可见 
turtle.stamp() (未测试)复制当前图形 
turtle.write('vshmily') 写字符串'vshmily'
turtle.write(s[,font=("font-name",font_size,"font_type")])  (未测试)写文本，s为文本内容，font是字体的参数，里面分别为字体名称，大小和类型；font为可选项, font的参数也是可选项
turtle.circle(77)  画一个半径为77的园
turtle.circle(77, steps=3)  三边形，画一个半径为77的园的内切多边形
turtle.circle(77, 300) 圆弧为300度
'''

  

