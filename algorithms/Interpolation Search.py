def interpolation(list1, n):
    start = 0
    end = len(list1) - 1
    while start <= end and list1[start] <= n <= list1[end]:
        if start == end:
            if list1[start] == n:
                return start
            return -1
        pos = start + ((n - list1[start]) // (list1[end] - list1[start])) * (end - start)
        if list1[pos] == n:
            return pos
        elif n > list1[pos]:
            start = pos + 1
        else:
            end = pos - 1
    return None


num = int(input("Enter a num: "))
print(interpolation([1, 3, 7, 10, 19], num))
