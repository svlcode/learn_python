x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hf', 'hi', 'hello', 'world']
s = "hello"

# slice = x[start:stop:ste]

slice = x[2:]
print(slice)

my_list = list(range(10))

# start at index 4 till 7 (not included)
print(my_list[4: 7])

# start at the beginning till index 5 (not included)
print(my_list[:5])

# start at index 3 till the end
print(my_list[3:])

# start at 4, go to 2, step by -1
print(my_list[4:2:-1])

# reverse the list
print(my_list[::-1])
