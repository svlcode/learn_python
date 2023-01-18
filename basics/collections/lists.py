x = [4, True, 'hi']
y = 'hi'
print(len(x))
print(len(y))

x.append('Hello')
# print(x)

for i in x:
    print(i)

# extend list by appending another list
x.extend([4, 5, 6])
print(x)

# remove last item from a list
last_item = x.pop()
print(x)

# remove item at index 1
item_at_index = x.pop(1)
print(x)

# remove first occurence of value
x.remove(4)
print(x)
