def linear_search(list1, n):
    start = 0
    end = len(list1) - 1
    while start <= end:
        mid = start + (end-start) // 2
        mid_value = list1[mid]
        if mid_value == n:
            return mid
        elif n < mid_value:
            end = mid - 1
        else:
            start = mid + 1
    return None


num = int(input("Enter the item you want to search: "))
print(linear_search([5, 8, 4, 10, 3, 2, 9], num))
