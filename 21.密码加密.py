#!/usr/bin/python
# coding=utf-8

'''
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？
请使用 Python 对密码加密。
'''

import hashlib
import random

def get_hexsigest(salt,password):
    combined = '%s%s' % (salt,password)
    return hashlib.sha3_384( combined.encode() ).hexdigest()

def hash_password(password):
    salt = get_hexsigest( str(random.random()),str(random.random) )[:9]
    hsh = get_hexsigest(salt, password)
    return '%s$%s' % (salt,hsh)

def check_password(input_password,hsh_password):
    salt,hsh = hsh_password.split('$')
    return hsh == get_hexsigest(salt,input_password)

def main():
    first = input('Please enter your password: ')
    hsh_password = hash_password(first)
    second = input('Please enter it again: ')
    if ( check_password(second,hsh_password) ):
        print('You entered the right password')
    else:
        print(r'Password doesn\'t match')

main()