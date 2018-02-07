# -*- coding:utf-8 -*-
# 2018/02/07
# version 1.0

'''
Question:
    Given a linked list, swap every two adjacent nodes and return its head
'''

def swap_pair(sequence):
    """
    For example:
    Given 1->2->3->4,
    you should return the list as 2->1->4->3.
    """
    swap_element = []
    odd = sequence[::2]
    even = sequence[1::2]
    for i in even:
        for j in odd:
            swap_element.append(i)
            swap_element.append(j)
            odd.pop(0)
            break
    return swap_element
    

if __name__ == "__main__":
    sequence = [1,2,3,4]
    solution = swap_pair(sequence)
    print(solution)
    

