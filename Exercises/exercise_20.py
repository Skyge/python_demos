# -*- coding:utf-8 -*-
# 2018/02/04
# version 1.0

'''
Question:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    The brackets must close in the correct order,
    "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

def is_valid(string):
    stack = []
    valid_dict = {"]":"[", "}":"{", ")":"("}
    for char in string:
        if char in valid_dict.values():
            stack.append(char)
        elif char in valid_dict.keys():
            if stack == [] or valid_dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

if __name__ == "__main__":
    string = "{[([()])]}]"
    solution = is_valid(string)
    print(solution)
    

