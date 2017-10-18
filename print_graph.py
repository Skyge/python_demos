# -*- coding:utf-8 -*-
#2017/10/18
#version 2.0
'''
    generate figure
'''

def right_triangle(rows=5):
    '''
        >>>right_triangle(5)
        
        *
        * *
        * * *
        * * * *
        * * * * *
        
    '''
    i = 0
    while i < rows:
        j = 0
        while j <= i:
            print ('*',end = ' ')
            j += 1
        print('')
        i += 1
 
def equilateral_triangle(rows):
    '''
        >>>hollow_equilateral_triangle(4)
            *
           ***
          *****
         *******
    '''
    for i in range(rows):
        print(' '*(rows-i-1) + '*'* (2*i+1))

def hollow_equilateral_triangle(rows):
    '''
        >>>hollow_equilateral_triangle(5)
            *
           * *
          *   *
         *     *
        * * * * * 
    '''
    for i in range(rows):
        if i == 0:
            print(' '*(rows-1) + '*')
        elif i != (rows-1):
            print(' '*(rows-i-1) + '*',end = '')
            print(' '*(2*i-1) + '*')
        elif i == (rows-1):
            print('* '*i + '*')

def rectangle(length,width):
    '''
        >>>rectangle(5,4)
            * * * * *
            * * * * *
            * * * * *
            * * * * *
        >>>rectangle(3,3)
            * * *
            * * *
            * * *
    '''
    for i in range(width):
        print('* '* length)

def hollow_rectangle_01(length,width):
    '''
        >>>hollow_rectangle(5,4)
            * * * * *
            *       *
            *       *
            * * * * *
        >>>hollow_rectangle(3,3)
            * * *
            *   *
            * * *
    '''
    for i in range(width):
        if i == 0 or i == width-1:
            print('* '* length)
        else:
            print('*'+ ' '*((length-1)*2-1)+'*')

def hollow_rectangle_02(length,width):
    for i in range(width):
        for k in range(length):
            if i > 0 and i != width-1 :
                if k == 0 or k == length-1:
                    print('* ',end='')
                else:
                    print('  ',end='')
            else:
                print('* ',end='')
        print('')

def diamond(length):
    '''
        >>>hollow_equilateral_triangle(5)
            *
           * *
          *   *
         *     *
        *       *
         *     *
          *   *
           * *
            *
    '''
    i=j=k= 1 #i用于控制图形行数，j用于控制空格的个数，k用于控制*的个数
    #菱形的上半部分
    for i in range(length):
        for j in range(length - i):
            print (' ',end='')   
        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2:
                print ('*',end='')
            else:
                print (' ',end='')
        print ('')
    #菱形的下半部分
    for i in range(length):
        for j in range(i):
            print (' ',end='')
            
        for k in range(2 * (length - i) - 1):
            if k == 0 or k == 2 * (length - i) - 2:
                print ('*',end='')
            else:
                print (' ',end='')
        print ('')
        

if __name__ == '__main__':
    print('打印直角三角形：')
    right_triangle(5)
    
    print('打印等腰三角形：')
    equilateral_triangle(4)
    
    print('打印空心等腰三角形：')
    hollow_equilateral_triangle(9)
    
    print('打印实心矩形：')
    rectangle(4,3)
    
    print('打印空心矩形方法1：')
    hollow_rectangle_01(5,4)
    
    print('打印空心矩形方法2：')
    hollow_rectangle_02(5,4)
    
    print ('打印空心菱形，这里去掉if-else条件判断就是实心的')
    diamond(5)      
