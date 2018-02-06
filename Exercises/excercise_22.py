# -*- coding:utf-8 -*-
# 2018/02/06
# version 1.0

'''
Question:
    Given n pairs of parentheses,
    write a function to generate all combinations of well-formed parentheses.
'''

def generate_parenthesis(num):
    """
    For example, given num = 3,
    a solution set is:["((()))",
                       "(()())",
                       "(())()",
                       "()(())",
                       "()()()"
                       ]
    """
    def generate(temp, left, right, parens=[]):
        if left:         generate(temp + "(", left-1, right)
        if right > left: generate(temp + ")", left, right-1)
        if not right:    parens +=temp,
        return parens
    return generate("", num, num)

if __name__ == "__main__":
    num = 3
    solution = generate_parenthesis(num)
    print(solution)
    

