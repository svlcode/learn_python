numbers = [23, 65, 2, 67, 25, 1, 7]
# changes the sort order of the original list
numbers.sort(reverse=True)

# sorting any iterable and returning a new list of elements sorted
new_list = sorted(numbers)
# original list remains unchanged
print(numbers)
print(new_list)


items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12)
]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

items.sort(key=lambda item: item[1])
