# -*- coding:utf-8 -*-
# 2018/01/29
# version 1.0

'''
Question:
    Given an integer, convert it to a roman numeral.
    Input is guaranteed to be within the range from 1 to 3999.
Note:
    I(1)、V(5)、X(10)、L(50)、C(100)、D(500)和M(1000)
'''

def int_to_roman(digit):
    if 0 < digit and digit < 4000:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        try:
            return M[digit//1000] + C[(digit%1000)//100] + X[(digit%100)//10] + I[digit%10]
        except:
            print("请输入正确范围的整数！")
    else:
        print("请输入正确范围的整数！")

if __name__ == "__main__":
    digit = 2586
    solution = int_to_roman(digit)
    print(solution)
    

