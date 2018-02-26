# -*- coding:utf-8 -*-
# 2018/01/23
# version 1.0

'''
    The string "PAYPALISHIRING" is written in a zigzag pattern 
    on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"
'''
   
def convert(s, num_rows):
    """
    Example:

        Input: convert("PAYPALISHIRING", 3) 

        Output: PAHNAPLSIIGYIR"
    """
    if num_rows == 1 or num_rows >= len(s):
        return s

    L = [""] * num_rows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == num_rows -1:
            step = -1
        index += step

    return "".join(L)
        
if __name__ == "__main__":
    solution = convert("PAYPALISHIRING", 3)
    print(solution)
