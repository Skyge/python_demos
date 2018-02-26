# -*- coding:utf-8 -*-
# 2018/02/01
# version 1.0

'''
Question:
    Given an array S of n integers,
    are there elements a, b, c, and d in S
    such that a + b + c + d = target?
    Find all unique quadruplets in the array which gives the sum of target.

Note:
    The solution set must not contain duplicate quadruplets.
'''

def find_N_sum(nums, target, N, temp_res, results):
    """
    For example：given array S = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:[[-1,  0, 0, 1],
                       [-2, -1, 1, 2],
                       [-2,  0, 0, 2]]
    """
    nums = sorted(nums)
    if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
        return

    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                results.append(temp_res + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif s < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(len(nums)-N+1):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                find_N_sum(nums[i+1:], target-nums[i], N-1, temp_res+[nums[i]], results)

    
    return results

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    N = 4
    results = []
    solution = find_N_sum(nums, target, N, [], results)
    print(solution)
    

