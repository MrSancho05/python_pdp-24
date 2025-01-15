# 1.ekrandan kirib kelgan matni katta, kichik harflarga o'tqazing
matn = input("Enter matn: ")
print(matn.upper())
print(matn.lower())

# 2. 3 xonali sonlar sum > 5 
son = int(input("Enter 3x num: "))
x1 = son % 10
x2 = son // 10 % 10
x3 = son // 100 % 10
print(x1+x2+x3 > 5)

# 3 palidrom som 121, 303, 404
son = int(input("Enter palidrom 3x num: "))
x1 = son % 10
x3 = son // 100 % 10
print(x1 == x3)

# 4 4 xonali sonning 3 va 2 xonalarini almashritib 1 qo'shib chiqaring
son = int(input("Enter 3x num: "))
# 1234
x1 = son % 10
x2 = son // 10 % 10
x3 = son // 100 % 10
x4 = son // 1000 % 10
result = x4 * 1000 + x2 * 100 + x3 * 10 + x1 + 1
print(result)
