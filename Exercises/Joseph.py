# -*- coding:utf-8 -*-
# 2018/03/06
# version1.0


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
