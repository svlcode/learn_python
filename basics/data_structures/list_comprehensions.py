# [expression for item in items]

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 14)
]

# get the prices of the products greater or equal to 10
prices = [item[1] for item in items if item[1] >= 10]
print(prices)


# find the name of the product which has a price which is multiple of 7
product = [name for name, price in items if price % 7 == 0]
# if product is not an empty list [] (because [] is Falsy)
if product:
    print(product[0])
