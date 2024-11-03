# tuples
nums = [1,2,3,4,5,6]
print(type(nums))

ty = tuple(nums)
print(type(ty))

infoPerson = ("Ali", 1991, 33, True, "Namangan")

s = "Hello"
s1 = "Hell"

print(hex(id(s)))
print(hex(id(s1)))

fruits = ["apple", "cherry", "lemon", "orange"]
ff = fruits
ff[0] = "olma"
print(ff)
print(fruits)

# 1
fruits = ["apple", "banana", 'cherry', 'orange', 'kiwi']
print(fruits[0])
print(fruits[-1])
print(fruits[2])

# 2
nums = [1,2,3,4,5,6,2]
print(nums.count(2))
print(nums.index(5))

# 3 
colors = ('red', 'blue', 'green')
color = list(colors)
color.append('yellow')
print(tuple(color))

# 4
letters = ('a', 'b', 'c', 'd', 'e')
llist = list(letters)
llist.reverse()
print(llist)