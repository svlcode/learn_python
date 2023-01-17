x = "hello"
y = 'hello'
print((x == y) and x == "HELLO".lower() or y == "heLlO".lower())

print(f'ord("a") = {ord("a")}')
print(f'ord("b") = {ord("b")}')

print('ab' > 'b')

x = 7
y = 8
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2

result4 = result1 or not result2 or result3
print(result4)