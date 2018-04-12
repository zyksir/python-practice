#0001   使用 Python 生成 200 个激活码
 #_*_ coding:utf-8 _*_
import random, string

f = open("5.txt","w")
for i in range(10):
    chars = string.digits + string.ascii_letters
    s = [random.choice(chars) for i in range(10)]
    f.write(''.join(s)+'\n')
f.close()

'''
about random
random.random(): randomly create a float number in [0,1.0]
random.uniform(a,b):randomly create a float number between a and b
random.randint(a,b):randomly create a int number between a and b
random.choice([...]) choose one thing from [...]
random.randrange(a,b,c) is equal to random.choice( range(10,100,2) )
'''