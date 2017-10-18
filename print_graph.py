# -*- coding:utf-8 -*-
#2017/10/18
#version 1.1
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
    print('打印直角三角形：')
    i = 0
    while i < rows:
        j = 0
        while j <= i:
            print ('*',end = ' ')
            j += 1
        print('')
        i += 1
 
if __name__ == '__main__':
    right_triangle(5)



def equilateral_triangle(rows):
    '''
        >>>hollow_equilateral_triangle(4)
            *
           ***
          *****
         *******
    '''
    print('打印等腰三角形：')
    for i in range(rows):
        print(' '*(rows-i-1) + '*'* (2*i+1))

if __name__ == '__main__':
    equilateral_triangle(4)



def hollow_equilateral_triangle(rows):
    '''
        >>>hollow_equilateral_triangle(5)
            *
           * *
          *   *
         *     *
        * * * * * 
    '''
    print('打印空心等腰三角形：')
    for i in range(rows):
        if i == 0:
            print(' '*(rows-1) + '*')
        elif i != (rows-1):
            print(' '*(rows-i-1) + '*',end = '')
            print(' '*(2*i-1) + '*')
        elif i == (rows-1):
            print('* '*i + '*')

if __name__ == '__main__':
    hollow_equilateral_triangle(9)

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
    print('打印矩形：')
    for i in range(width):
        print('* '* length)

if __name__ == '__main__':
    rectangle(4,3)

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
    print('打印菱形：')
    for i in range(length*2-1):
        if i == 0:
            print(' '*(length-1) + '*')
        elif i <= (length-1):
            print(' '*(length-i-1) + '*',end = '')
            print(' '*(2*i-1) + '*')
        elif i < (length-1)*2:
            print(' '*(i-length+1) + '*',end = '')
            print(' '*(2*(2*(length-1)-i)-1) + '*')
        elif i == (length-1)*2:
            print(' '*(length-1) + '*')
        

if __name__ == '__main__':
    diamond(5)      
