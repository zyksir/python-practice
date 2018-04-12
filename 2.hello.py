#2017/9/7.py
# _*_ coding:utf-8 _*_
from turtle import *

def drawSnake(rad,angle,len,neckrad,zyk):
    pencolor("red")
    circle(rad,angle)
    circle(-rad,angle)
    pencolor("blue")
    circle(rad,angle)
    circle(-rad,angle)
    pencolor("yellow")
    circle(rad,angle)
    circle(-rad,angle)
    circle(rad,angle/2)
    fd(rad)
    circle(neckrad,180)
    fd(rad*2/3)

def main():
    val=input()
    f=eval(val)
    print("%.2f"%f)
    setup(1300,800,0,0)
    pythonsize=30
    pensize(pythonsize)
    seth(-40)
    #turtle.circle(60,360)
    drawSnake(40,80,3,pythonsize,111111)

main()
