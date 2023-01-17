my_list = list(range(10, 50, 3))

for i in my_list:
    print(i)


# Create an empty list
my_list = []

# Value to begin and end with
start, end = 10, 20

# unpack the result
my_list.extend(range(start, end))
# Append the last value
my_list.append(end)

# Print the list
print(my_list)
