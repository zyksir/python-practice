#!/usr/bin/python
# coding=utf-8

"""
第 0013 题：敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
    当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
    当用户输入敏感词语，则用 星号 * 替换，
    例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

def test_words(path,word):
    with open(path) as f:
        word_list = f.read().split('\n')
        if word in word_list:
            print("Freedom")
        else:
            print("Human Rights")

def change_words(path,sentence):
    with open(path) as f:
        word_list = f.read().split('\n')
        #print(word_list)
    for word in word_list:
        if sentence.find(word)!= -1:
            replace_str = '*'*len(word)
            sentence = sentence.replace(word,replace_str)
            break
    print(sentence)

def main():
    path = r'__pycache__\filtered_words.txt'
    while True:
        zyk_say = input("please input one word:")
        if zyk_say == 'exit':
            return 0
        else:
            change_words(path,zyk_say)

main()
