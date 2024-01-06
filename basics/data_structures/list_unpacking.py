# unpacking list works only if the number of variables
# matches the number of elements from the list
numbers = [1, 2, 3]
first, second, third = numbers

# another way is to unpack the rest of the elements into another list
numbers = list(range(10))
first, second, *other = numbers
print(first)
print(second)
print(other)

# unpacking the first, middle and the last elements of the list
numbers = list(range(10))
first, *other, last = numbers
print(first)
print(other)
print(last)

# unpack items of a list
items = [0, 'a']
index, letter = items

# unpack tuples
# enumerate gets a tuple with the index and the value
letters = ['a', 'b', 'c']
for index, value in enumerate(letters):
    print(index, value)
