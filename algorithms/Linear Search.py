def linear_search(list1, n):
    for i in list1:
        if n == list1[i]:
            return f'{n} is in the list'
        else:
            return f'{n} is not in the list'


num = int(input("Enter the item you want to search: "))
print(linear_search([5, 8, 4, 10, 3, 2, 9], num))
