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
