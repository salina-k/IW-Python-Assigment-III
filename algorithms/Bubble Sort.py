def bubble_sort(n):
    while True:
        corrected = False
        for i in range(0, len(n)-1):
            # sorting in ascending order
            if n[i] > n[i+1]:
                (n[i], n[i+1]) = (n[i+1], n[i])
                corrected = True
        if not corrected:
            return n


print(bubble_sort([5, 8, 4, 10, 3, 2, 9]))
