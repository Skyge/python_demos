# -*- coding:utf-8 -*-
# 2017/10/13 18:12
# version 3.0
'''
    generate a series of code
'''

import random
import string

chars = string.ascii_letters + string.digits

def get_code():
    '''
       获得四个字母和数字的随机组合
       >>>get_code()
       ak7h
       
       >>>get_code()
       CgJ0
    '''
    return "".join([random.choice(chars) for i in range(4)])

def concatenate(length):
    '''
       生成的每个激活码中有几组
       >>>concatenate(4)
       5jSI-1205-IjN2-Thn3
       
       >>>concatenate(2)
       erz7-k9Ux
    '''
    return "-".join([get_code() for i in range(length//4)])


def generate_code(quantity=1,length=16):
    '''
        生成quantity组,长度为length位的激活码
    '''
    for i in range(quantity):
        content = concatenate(length)
        print(content)
        save_code(content)
    


def save_code(content):
    with open('Result Code.txt', 'a') as file:
        file.write(content + '\n')

if __name__ == '__main__':
    generate_code(3,16)

