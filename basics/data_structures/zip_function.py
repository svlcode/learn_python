list1 = [1, 2, 3]
list2 = [10, 20, 30]

# desired output [(1, 10), (2, 20), (3, 30)]

result = list(zip(list1, list2))
print(result)

result = list(zip("abc", list1, list2))
print(result)
