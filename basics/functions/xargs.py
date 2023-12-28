
# when we add an asterix to an argument, Python will see that as a tuple
def multiply(*list):
    print(list)
    total = 1
    for number in list:
        total *= number
    return total


# arguments will be packaged as a tuple
print(multiply(4, 5, 7))
