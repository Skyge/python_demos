# -*- coding:utf-8 -*-
# 2018/03/03

def quickSort(lists, left, right):
    """
    快速排序:

        通过一趟排序将要排序的数据分割成独立的两部分，
        其中一部分的所有数据都比另外一部分的所有数据都要小，
        然后再按此方法对这两部分数据分别进行快速排序，
        整个排序过程可以递归进行，以此达到整个数据变成有序序列

    """
    # 判断left是否大于等于right,如果为True,直接返回
    if left >= right:
        return lists
    # 设置基准数
    low = left
    high = right
    base = lists[low]
    while low < high:
        # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
        while low < high and lists[high] >= base:
            high -= 1
        # 如找到,则把第high个元素赋值给第个元素low,此时表中low,high个元素相等
        lists[low] = lists[high]
        # 同样的方式比较前半区
        while low < high and lists[low] <= base:
            low += 1
        lists[high] = lists[low]
    # 做完第一轮比较之后,列表被分成了两个半区,并且low=high,需要将这个数设置回base
    lists[low] = base

    # 递归前后半区
    quickSort(lists, left, low - 1)
    quickSort(lists, high + 1, right)
    return lists

if __name__ == '__main__':
    lst = [1,4,46,28,2,16,71,23,35]
    print(quickSort(lst, 0, len(lst)-1))

