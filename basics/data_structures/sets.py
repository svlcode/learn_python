# use sets if you want to check if an item exists or not
# doesn't care about order or frequency

x = set()
print(type(x))

s = {4, 32, 2, 2}
s.add(5)
print(s)
s.remove(2)
print(s)

# key operation of the sets (because it's done very fast):
print(4 in s)

s2 = {3, 4, 22, 1}

print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))

x = {i for i in range(100) if i % 5 == 0}
print(x)