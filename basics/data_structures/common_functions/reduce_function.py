from functools import reduce

# sum the price of the products with a price greater than 10
items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12),
    ("product4", 14)
]

result = reduce(lambda a, b: a + b,
                [item[1] for item in items if item[1] >= 10])

print(result)

