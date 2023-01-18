# tupples are immutable (paranteses are optional)
x = (4, 5, 0, 2)
x = 4, 5, 0, 2

# error: x[0] = 45
# error: x.append(5)

print(x[0])

# lists inside lists
x = [[], (), [[2, 1], [], (3, 5, 7)]]


# function with multiple returns
def calculate_sum(a, b) -> tuple:
    c = a + b
    return a, b, c

a, b, c = calculate_sum(2, 4)
print(a, b, c)


# create a tuple from an iterable
my_tuple = tuple(['vio', 28, True])
print(my_tuple)


if "vio" in my_tuple:
    print('"vio" is in the tuple')
else:
    print('"vio" is NOT in the tuple')

x = tuple(i for i in range(100) if i % 5 == 0)
print(x)