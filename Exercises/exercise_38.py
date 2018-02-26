# -*- coding:utf-8 -*-
# 2018/02/17


'''
Question:
    The count-and-say sequence is the sequence of integers
    with the first five terms as following:
    1. 1
    2. 11
    3. 21
    4. 1211
    5. 111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s"or 21.

    Given an integer N,generate the Nth term of the count-and-say sequence.

'''
"""
def countAndSay(num):
    s = "1"
    for _ in range(num-1):
        s = "".join(str(len(group)) + digit
                    for group, digit in re.findall("((.)\\2*)", s))

    return s
"""
import re

def countAndSay(num):
    s = "1"
    for _ in range(num-1):
        s = re.sub("(.)\\1*", lambda m:str(len(m.group(0))) + m.group(1), s)
    return s

if __name__ == "__main__":
    num = 5
    solution = countAndSay(num)
    print(solution)
    

