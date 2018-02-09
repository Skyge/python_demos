# -*- coding:utf-8 -*-
# 2018/02/09


'''
Question:
    Suppose an array sorted in ascending order is rotated
    at some pivot unknown to you beforehand.
    
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    
    You are given a target value to search.
    If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

'''

def search(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
    

if __name__ == "__main__":
    nums, target = [4,5,6,7,0,1,2], 4
    solution = search(nums, target)
    print(solution)
    

