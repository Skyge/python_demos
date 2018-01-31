# -*- coding:utf-8 -*-
# 2018/01/31
# version 1.0

'''
Question:
    Given an array S of n integers,
    are there elements a, b, c in S such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

Note:
    The solution set must not contain duplicate triplets.
'''

'''
def three_sum(sequences):
    two_sum = []
    for i in range(len(sequences)-1):
        for j in sequences[i+1:]:
            temp = sequences[i] + sequences[j]
            if (0-temp) in sequences[i+1:]:
                two_sum.append(tuple(sorted([sequences[i],sequences[j],0-temp])))
    return(list(set(two_sum)))
'''

def three_sum(nums):
    """
    For example:
        Input: S = [-1, 0, 1, 2, -1, -4]
        Output:[
                  [-1, 0, 1],
                  [-1, -1, 2]
                ]
    """
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res

if __name__ == "__main__":
    sequences = [-1, 0, 1, 2, -1, -4]
    solution = three_sum(sequences)
    print(solution)
    

