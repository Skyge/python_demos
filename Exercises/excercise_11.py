# -*- coding:utf-8 -*-
# 2018/01/27
# version 1.0

'''
Question:
    Given n non-negative integers a1, a2, ..., an,
    where each represents a point at coordinate (i, ai). n vertical lines are
    drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container,
    such that the container contains the most water.
Note:
    You may not slant the container and n is at least 2.
'''

def max_area(height):
    L, R, width, area = 0, len(height) - 1, len(height) - 1, 0
    for w in range(width, 0, -1):
        if height[L] < height[R]:
            area, L = max(area, height[L] * w), L + 1
        else:
            area, R = max(area, height[R] * w), R - 1
    return area


if __name__ == "__main__":
    sequences = [9, 5, 9]
    solution = max_area(sequences)
    print(solution)
    

