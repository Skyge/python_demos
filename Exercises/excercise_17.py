# -*- coding:utf-8 -*-
# 2018/02/02
# version 1.0

'''
Question:
    Given a digit string,
    return all possible letter combinations that the number could represent.

    A mapping of digit to letters is just like on the telephone buttons.
'''

from functools import reduce

def letter_combinations(digits):
    """
    Example:
    
        Input:Digit string "23"
        
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    """
    if "" == digits: return []
    maps = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
             }
    return reduce(lambda comb, digit: [x + y for x in comb for y in maps[digit]], digits, [""])
'''
if "" == digits: return []
    maps = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    ret=[""]
    for c in digits:
        tmp=[]
        for y in ret:
            for x in maps[c]:
                tmp.append(y+x)
        ret=tmp
    
    return ret
'''

if __name__ == "__main__":
    digits = "23"
    solution = letter_combinations(digits)
    print(solution)
    

