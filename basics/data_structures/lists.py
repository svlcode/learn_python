
# repeat elements in a list
zeros = [0] * 5

# combine lists
combined = zeros + ["1", "a", "b"]
print(combined)

# combine lists
result = [1, 2, 3] + [4, 5, 6]
print(result)

# create a list of numbers from 0 to 19
numbers = list(range(20))

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

# slicing lists
letters = ['a', 'b', 'c', 'd']
letters[0] = "A"
print(letters)

print(letters[0:-1])

# delete a range of elemets
del letters[0:3]
print(letters)

# remove all
letters.clear()
