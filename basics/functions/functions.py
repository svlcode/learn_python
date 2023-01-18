# functions are actually objects.
# this means you can actually return them.

def func():
    print('hello')
    # define a function inside another function

    def func():
        print('world')
    func()


func()


def sum(a, b):
    def inner_sum():
        return a + b
    return inner_sum


callback = sum(2, 3)
print(callback())

# this function returns a tuple


def operations(a, b, z=None):
    if z is None:
        print('z is None')

    return a + b, a*b, a/b


sum, product, division = operations(3, 2)

print(sum, product, division)

x = 'vio'


def fun(name):
    global x  # this is almost never used
    x = name


fun('aly')
print(x)


def fun():
    raise Exception('bad')
    print('hello')


