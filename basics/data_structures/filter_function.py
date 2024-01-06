items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12)
]

result = list(filter(lambda item: item[1] > 9, items))

print(result)
