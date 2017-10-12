# -*- coding:utf-8 -*-
# 2017/10/12 22:12
# version 2.0
'''
    generate a series of code
'''

import random
import string


def generate_code(length):
    '''
       >>>gen_code()
       
       k7lKLQWLwo8KrGu6
       
    '''
    chars = string.ascii_letters + string.digits
    
    return ''.join([random.choice(chars) for i in range(length)])


def save_code(content):
    with open('Result Code.txt', 'a') as file:
        file.write(content + '\n')

if __name__ == '__main__':
    for i in range(5):
        content = generate_code(16)
        print (content)
        save_code(content)

