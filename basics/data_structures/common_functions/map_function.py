items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12)
]


# map function returns a map object which is another iterable
prices = map(lambda item: item[1], items)

print(list(prices))
