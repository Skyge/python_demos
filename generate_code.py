# -*- coding:utf-8 -*-
# 2017/10/12 19:36
'''
    generate a series of code
'''

import random

all_code = []


#生成26个大写的字母
for x in range(65,91):
    a = str(chr(x))  #生成对应的ASCII码对应的字符串
    all_code.append(a)
    
#生成26个小写字母
for x in range(97,123):
    a = str(chr(x))  #生成对应的ASCII码
    all_code.append(a)
    
#生成10个数字
for x in range(10):
    all_code.append(str(x))
    

#生成16位激活码
def gen_code():
    '''
        >>>gen_code()
        
        k7lKLQWLwo8KrGu6
        
    '''
    s=''
    for x in range(16):
        a = random.choice(all_code)
        s += a
    print(s)

if __name__ == '__main__':
    import os
    for x in range(5):
        gen_code()
    os.system("pause")

