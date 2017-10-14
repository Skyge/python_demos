# -*- coding:utf-8 -*-
#2017/10/14
#version 1.0
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


        
