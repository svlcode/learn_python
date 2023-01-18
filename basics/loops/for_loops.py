for i in range(10):
    print(i)

# range function:
# range(stop)
# range(start, stop)
# range(start, stop, step)

print('range')
for i in range(2, 10, 2):
    print(i)

print('backwards')
for i in range(10, -1, -1):
    print(i)

# access by index
x = [1, 2, 5, 7, 457, 2, 7]
for i in range(len(x)):
    print(x[i])


# alternative using enumerate
x = [6, 4, 5, 7, 457, 2, 7]
for i, value in enumerate(x):
    print(f'item at index {i} is {value}')