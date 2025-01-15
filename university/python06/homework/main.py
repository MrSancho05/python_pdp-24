# homework
import math
x = int(input("Enter a number: "))
print(~x)
check = ~x > 0
# print(math.fabs(~x))
print(check, ~x * check)
print(not check, ~x * -1)