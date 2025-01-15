# multiply = lambda x,y: x * y
# print(multiply(5,3))


# bigger = lambda x,y: x if x > y else y
# print(bigger(1,2))


# list = [x for x in range(n) if x % 2 != 0 and x % 3 == 0]
# print(list)

# n = int(input('Enter n: '))
# list = lambda i: [i for i in range(n) if i % 2 == 0 and i % 3 == 0]
# print(list(1))

# def findNumber(x,y):
#     while x > 0:
#         qoldiq = x % 10
#         if qoldiq == y:
#             return True
#         x //= 10
#     return False
# print(findNumber(123,0))

findNumber = lambda x,y: str(x).find(str(y)) > -1 if True else False
print(findNumber(123,3))