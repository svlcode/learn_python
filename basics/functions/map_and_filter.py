x = [*range(10)]

mp = list(map(lambda i: i + 3, x))
print(mp)

evens = [*filter(lambda i: i % 2 == 0, mp)]
odds = [*filter(lambda i: i % 2 != 0, mp)]

print('evens: ',evens)
print('odds', odds)
x = "test"