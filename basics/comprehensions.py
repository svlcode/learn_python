# comprehensions are used to initialize collections and you
# can think of them being similar to lambdas

import math
x = [x for x in range(5)]
print(x)

x = [x % 2 for x in [y+1 for y in range(6)]]
print(x)

# even numbers
x = [x for x in range(100) if x % 2 == 0]
print(f"even numbers: {x}")

# odd numbers
x = [x for x in range(100) if x % 2 != 0]
print(f"odd numbers: {x}")


# find prime numbers using comprehension
x = [i for i in range(3, 100) if all(i % n != 0 for n in range(2, int(i/2)))]
print(f"prime numbers: {x}")


# convert to binary
x = [[int(b) for b in list('{0:0b}'.format(x))] for x in range(1, 8)]
print(x)


