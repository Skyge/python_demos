# -*- coding:utf-8 -*-
# 2018/01/25
# version 1.0

'''
Question:
    Given a 32-bit signed integer, reverse digits of an integer.
Note:
    Assume we are dealing with an environment which could only hold integers 
    within the 32-bit signed integer range. 
    For the purpose of this problem, 
    assume that your function returns 0 when the reversed integer overflows.
'''

def reverse_digits(integer):   
    """
    Example 2:
	Input: -123
	Output: -321

    Example 3:
	Input: 120
	Output: 21
    """
    s = (integer > 0) - (integer < 0)
    r = int(str(integer * s)[::-1])
    return s * r * (r < 2**31)

if __name__ == "__main__":
    integer = -321
    solution = reverse_digits(integer)
    print(solution)
