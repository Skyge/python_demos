# -*- coding:utf-8 -*-
# 2018/01/26
# version 1.0

'''
Question:
    Determine whether an integer is a palindrome.
    Do this without extra space.
'''

def judge_palindrome(digits):
    if digits < 0:
        return False

    ranger = 1
    while digits / ranger >= 10:
        ranger *= 10

    while digits:
        left = digits // ranger
        right = digits % 10
        if left != right:
            return False
            
        digits = (digits % ranger) // 10
        ranger /= 100

    return True

if __name__ == "__main__":
    digits = 596848695
    solution = judge_palindrome(digits)
    print(solution)
