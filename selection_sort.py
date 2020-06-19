def selection_sort(list_a=[]):
    for i in range(len(list_a)-1):                     # always index first element as minimum, and then compare with other elements, then return the minimum  
        min_index  = i
        for j in range(i, len(list_a)):
            if list_a[j] < list_a[min_index]:
                min_index = j
        if min_index != i:
            list_a[i], list_a[min_index] = list_a[min_index], list_a[i]
    return list_a

list_a = [2, 8, 1, 9, 6, 5, 3]
print(selection_sort(list_a))
