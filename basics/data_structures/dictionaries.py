# dictionaries are like objects in JavaScript

x = {'key': 4}
print(x['key'])

x[2] = 'dfdf'

print(x)

del x[2]
print(x)

x[5] = 'bla'
print(list(x.values()))
print(list(x.keys()))

if 5 in x:
    print('5 is in dictionary')

for key, value in x.items():
    print(key, value)

for key in x:
    print(key, x[key])


x = {i: 0 for i in range(100) if i % 5 == 0}
print(x)
