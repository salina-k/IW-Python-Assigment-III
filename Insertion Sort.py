def insertion_sort(n):
    for i in range(1, len(n)):
        element_to_sort = n[i]
        while n[i-1] > element_to_sort and i > 0:
            n[i], n[i-1] = n[i-1], n[i]
            i = i - 1
    
    return n


print(insertion_sort([5, 8, 4, 10, 3, 2, 9]))
