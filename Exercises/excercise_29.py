# -*- coding:utf-8 -*-
# 2018/02/08


'''
Question:
    Divide two integers without using multiplication,
    division and mod operator.

    If it is overflow, return MAX_INT.
'''

def divide(dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
    

if __name__ == "__main__":
    dividend, divisor = 15856898989, 4
    solution = divide(dividend, divisor)
    print(solution)
    

