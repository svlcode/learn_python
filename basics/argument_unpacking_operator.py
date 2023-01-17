# use argument-unpacking operator to unpack the result of the range function
my_list = [*range(10)]
for i in my_list:
    print(i)
