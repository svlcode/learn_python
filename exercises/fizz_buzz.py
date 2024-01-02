# def fiz_buzz(input):
#     if input % 3 == 0:
#         if input % 5 == 0:
#             return "fizzbuzz"
#         else:
#             return "fizz"
#     elif input % 5 == 0:
#         return "buzz"
#     else:
#         return input


def fiz_buzz(input):
    result = ""
    if input % 3 == 0:
        result = "fizz"
    if input % 5 == 0:
        result += "buzz"
    return result if result else input


print(fiz_buzz(10))
