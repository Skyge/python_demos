# 2018/03/13
# version 1.0
"""
    Given a set of candidate numbers (C) (without duplicates)
    and a target number (T),
    find all unique combinations in C where the candidate numbers sums to T.

    The same repeated number may be chosen from C unlimited number of times.

    Note:
        - All numbers (including target) will be positive integers.
        - The solution set must not contain duplicate combinations.
"""
def combinationSum(candidates, target):
    """
    For example: given candidate set [2, 3, 6, 7] and target 7,
    
    A solution set is: 
        [
          [7],
          [2, 2, 3]
        ]
    """
    result = []
    candidates = sorted(candidates)
    
    def dfs(tmp, tmp_result):
        if  not tmp:
            result.append(tmp_result)
            return 

        for num in candidates:
            if num > tmp:
                break
            if tmp_result and num < tmp_result[-1]:
                continue
            else:
                dfs(tmp - num, tmp_result + [num])
                
    dfs(target, [])
    
    return result

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(combinationSum(candidates, target))
