# -*- coding:utf-8 -*-
# 2018/01/31
# version 1.0

'''
Question:
    Given an array S of n integers,
    find three integers in S such that the sum is closest to a given number,
    target. Return the sum of the three integers.
    You may assume that each input would have exactly one solution.
'''



def three_sum_closest(nums, target):
    """
        For example, given array S = {-1 2 1 -4}, and target = 2.

        The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    """
    res = []
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s != target:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                return res

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 2
    solution = three_sum_closest(nums, target)
    print(solution)
    

