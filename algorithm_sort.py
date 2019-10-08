# 冒泡排序

def bubble_sort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)- i -1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

alist = [1, 9, 2, 8, 29, 344, 2, 45, 5, 7]
bubble_sort(alist)


# 选择排序

def selection_sort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist

alist = [1, 9, 2, 8, 29, 344, 2, 45, 5, 7]
selection_sort(alist)


# 插入排序

def insert_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and key < alist[j]:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = key
    return alist

alist = [1, 9, 2, 8, 29, 344, 2, 45, 5, 7]
insert_sort(alist)



# 希尔排序

"""希尔排序的原则是首先将序列分组并大致上排好，之后分组数越来越少逐步完全排好，
通过gap来限定分组数目，每个小组的排序使用插入排序的方法。
"""

def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = alist[i]
            j = i 
            while j >= gap and alist[j - gap] > key:
                alist[j] = alist[j-gap]
                j -= gap
            alist[j] = key
        gap = gap // 2
    return alist
            
alist = [1, 9, 2, 8, 29, 344, 2, 45, 5, 7]
shell_sort(alist)       


# 快速排序

"""快速排序采用分而治之的策略，取一个partiion，小于它的都排在左边，大于它的都排在右边，然后以递归的方式将左右两边的
数列继续重排，直到最后完全拍好。"""

def quick_sort(alist, low, high):
    if high > low:
        k = partition(alist, low, high)
        quick_sort(alist, low, k - 1)
        quick_sort(alist, k+1, high)
    return alist
 
def partition(alist, low, high):
    left = low
    right = high
    key = alist[left]
    while left < right:
        while alist[left] <= key:
            left += 1
        while alist[right] > key:
            right -= 1
        if left < right:
            alist[left], alist[right] = alist[right], alist[left]
    alist[low] = alist[right]
    alist[right] = key
    return right

alist = [1, 9, 2, 8, 29, 344, 2, 45, 5, 7]
quick_sort(alist, 0, len(alist)-1)


# 归并排序

"""归并排序是一种通过不断将序列递归的分割成小序列然后再合并的排序方法"""


def merge_sort(alist, comp = lambda x, y: x < y):
    if len(alist) < 2:
        return alist[:]
    mid = len(alist) // 2
    left = merge_sort(alist[:mid], comp)
    right = merge_sort(alist[mid:], comp)
    return merge(left, right, comp)

def merge(item1, item2, comp):
    item = []
    index1, index2 = 0, 0
    while index1 < len(item1) and index2 < len(item2):
        if comp(item1[index1], item2[index2]):
            item.append(item1[index1])
            index1 += 1
        else:
            item.append(item2[index2])
            index2 += 1
    item += item1[index1:]
    item += item2[index2:]
    return item

alist = [1, 9, 2, 8, 29, 344, 2, 45, 5, 7]
merge_sort(alist)