# -*- coding:utf-8 -*-
# 2018/03/08
# version1.2

'''
def findWho(num):
    """
    17人围成一圈，一次报数，报到3的倍数的人剔除队列，
    剩下的人继续接前面的号数报下去（比如说17号报到17后1号应该接着报18）。 
    求最后剩下的那个人的编号。
    """
    start = 0
    while len(num) != 1:
        tmp = list(range(start + 1, len(num) + start + 1))
        circle = 0
        for i in tmp:
            if not i % 3:
                num.remove(num[tmp.index(i) - circle])
                circle += 1
        start += len(tmp)
   
    return num


if __name__ == '__main__':
    num = list(range(1,18))
    print(findWho(num))
'''
'''
def josephus(num, target):
    """
    问题：将编号为0～（N–1）这N个人进行圆形排列，
    按顺时针从0开始报数，报到M–1的人退出圆形队列，
    剩下的人继续从0开始报数，不断重复。
    求最后出列者最初在圆形队列中的编号。
    """
    if num == 1:
        return 0  
    else:
        return (josephus(num-1, target) + target) % num 
'''
from collections import deque

def josephus(num, target):
    """
    一排人，编号从1开始到17.所有人按序围成一个圈，
    从编号1开始，挨个报数，从1开始，
    报到3则出局，然后再次从1开始报数，直到只剩下一个人，
    请问最后留下的是编号几？
    """
    q = deque(range(1, num + 1))
    while len(q) > 1:
        q.rotate(1 - target)
        q.popleft()
    return q

if __name__ == '__main__':
    num = int(input("请输入参与人数："))
    target = int(input("请输入出列号码："))
    print(josephus(num, target))
