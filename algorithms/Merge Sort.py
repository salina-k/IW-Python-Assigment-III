def merge_sort(n):
    length = len(n)
    if length > 1:
        mid = len(n) // 2
        left_list = n[:mid]
        right_list = n[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                n[k] = left_list[i]
                i += 1
                k += 1
            else:
                n[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            n[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            n[k] = right_list[j]
            j += 1
            k += 1
    return n


print(merge_sort([5, 8, 4, 10, 3, 2, 9]))


