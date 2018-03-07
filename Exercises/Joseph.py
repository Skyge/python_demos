# -*- coding:utf-8 -*-
# 2018/03/07
# version1.1

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

if __name__ == '__main__':
    num = int(input("请输入参与人数："))
    target = int(input("请输入出列号码："))
    print(josephus(num, target))
