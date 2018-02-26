# -*- coding:utf-8 -*-
# 2018/01/29
# version 1.0

'''
Question:
    Write a function to find the
    longest common prefix string amongst an array of strings.
'''
'''
def longest_common_prefix(sequences):
    longest_common = []
    comman_prefix = list(zip(*sequences))
    for i in comman_prefix:
        if len(set(i)) > 1:
            return ""
        else:
            longest_common.append(i[0])
    return "".join(longest_common)
'''
def longest_common_prefix(sequences):
    if not sequences:
        return ""
           
    for i, letter_group in enumerate(zip(*sequences)):
        if len(set(letter_group)) > 1:
            return sequences[0][:i]
    else:
        return min(sequences)


if __name__ == "__main__":
    sequences = ["as", "ascii", "ascend"]
    solution = longest_common_prefix(sequences)
    print(solution)
    

