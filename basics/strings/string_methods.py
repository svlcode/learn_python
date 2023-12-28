hello = 'hello'
hello2 = "hello"

if hello == hello2:
    print('the strings are equal')


hello = 'hello World'
print(f'hello variable before operations: "{hello}"')
print('hello.capitalize(): ' + hello.capitalize())
print('hello.upper(): ' + hello.upper())
print('hello.lower(): ' + hello.lower())
print('hello.count("l"): ' + str(hello.count('l')))

# slicing
# string[start:end:step]: Get all characters from start to end - 1

# get the first 5 characters
print('hello[0:5]: ' + hello[0:5])

# get the last 5 characters
print('hello[-5:]: ' + hello[-5:])

# substring
print('hello[2:7:2]: ' + hello[2:7:2])


hello = 'hello'
x = 3
print(hello * x)
