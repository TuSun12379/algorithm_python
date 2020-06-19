def bubble_sort(list_a):
    for i in range(len(list_a)-1, 0, -1):        # the comprision times in every run. n-1 times for first, n-2 for second....
        for j in range(i):                       # comparisions in every run
            if list_a[j] > list_a[j+1]:
                list_a[j+1], list_a[j] = list_a[j], list_a[j+1]
    return list_a
list_a = [2, 8, 1, 9, 6, 5, 3]
print(bubble_sort(list_a))
