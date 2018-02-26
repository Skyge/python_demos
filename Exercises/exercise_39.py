# -*- coding:utf-8 -*-
# 2018/02/26


'''
Question:
    Given a set of candidate numbers(C)(without duplicates)
    and a target number(T),
    find all unique combinations in C
    where the candidate numbers sums to T.

    The same repeated number may be chosen from C unlimited number of times.

    Note:
        1.All numbers(including target) will be positive integers.
        2.The solution set must not contain duplicate combinations.

'''
import re

def combinationSum(sequences, target):
    """
    Example:
        [input]:[2,3,6,7], 7
        [output]:[
                   [7],
                   [2,2,3]
                  ]
    """
    s = "1"
    for _ in range(num-1):
        s = re.sub("(.)\\1*", lambda m:str(len(m.group(0))) + m.group(1), s)
    return s


if __name__ == "__main__":
    num = 5
    solution = countAndSay(num)
    print(solution)
    

