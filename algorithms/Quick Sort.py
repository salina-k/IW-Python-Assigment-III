def quick_sort(n):
    length = len(n)
    if length <= 1:
        return n
    else:
        pivot = n.pop()
        left_list = []
        right_list = []
        for i in n:
            if i < pivot:
                left_list.append(i)
            else:
                right_list.append(i)
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


print(quick_sort([5, 8, 4, 10, 3, 2, 9]))

