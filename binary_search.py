# 二分查找

def binary_search(alist, target):
    first = 0
    last = len(alist) - 1
    while first <= last:
        midpoint = (last+first) // 2
        if alist[midpoint] == target:
            print(midpoint)
            return True
        elif alist[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return False

binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
