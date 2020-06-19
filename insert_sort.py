def insert_sort(list_a):
    for i in range(1, len(list_a)):                # inset a non-sorted element into a sorted list, from the second element
        for j in range(i, 0, -1):
            if list_a[j] < list_a[j-1]:
                list_a[j], list_a[j-1] = list_a[j-1], list_a[j]
    return list_a

list_a = [2, 8, 1, 9, 6, 5, 3]
print(insert_sort(list_a))
