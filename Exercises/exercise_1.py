# -*- coding:utf-8 -*-
#2018/01/01
#version 1.0

'''
    Given an array of integers,
    return indices of the two numbers such that they add up to a specific target.
    
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
'''

def two_sum(nums, target):
    """
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            print([buff_dict[nums[i]], i])
        else:
            buff_dict[target - nums[i]] = i


if __name__ == "__main__":
    nums = [3,4,5,2]
    target = 6
    two_sum(nums, target)


        
            
        
        
            
