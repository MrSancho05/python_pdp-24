# s = 0
# counter = 10
# while counter > 0:
#     s += counter
#     print(s)
#     counter -= 1
# print(s)

s = 1
# def sumNums(f):
#     global s
#     if f > 0:
#         s += f
#         sumNums(f - 1)
#     return s

# print(sumNums(10))

def sumNums(f):
    
    if f > 0:
        return f + sumNums(f - 1)
    else:
        return 0

sum = sumNums(10)
print(sum)