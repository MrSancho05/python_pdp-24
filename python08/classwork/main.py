# to'plam
# nums = [1,2,3,4,5,6,7,8,9,10]
# haqiqiySonlar = [3.4, 1.1, 5.2, 6, 9.8]
# letters = ['a', 'b', 'c', 'd', 'a', 'e', 'f']
# fruits = ["apple", "banana", "cherry"]
# animals = ["Cow", "Cat", "Dog", "Duck", "Horse"]
# personInfo = [1991, "Ali", True, 33, 180.56, 95.6]

# print(nums)
# print(haqiqiySonlar)
# print(letters)
# print(fruits)
# print(animals)
# print(personInfo)
# print(type(nums))

fruits = ["apple", "orange", "lemon"]
print(fruits[0])
print(fruits[-1]) # only in python
print(len(fruits))
print(fruits)
fruits[-1] = "banana"
print(fruits)

# element add qilish uchun append
fruits.append("pineapple")
print(fruits)
fruits.insert(0, "kiwi")
print(fruits)

# element o'chirish
fruits.remove("pineapple")
print(fruits)
removedEl = fruits.pop(2) # only in python 
print(fruits)
print(removedEl)
# del fruits[0]
print(fruits)
# del fruits
# print(fruits) # error
# del fruits[0:3]
# print(fruits)

# 2 ta list bir biriga qo'shish uchun
num = [1,2,3]
numS = ["one", "two", "three"]
num.extend(numS)
print(num)
print(numS)

strList = ["cba", "abc", "bca"]
numList = [-5, 10, 1]
strList.sort()
print(strList)
numList.sort()
print(numList)

# strReverse
word = "Hello"
print(word)
strReverse = word[::-1]
strReverse = word[3:-1]
print(strReverse)

word = "Hello wat's up bro!"
print(len(word))

# 2 chi va 4 chi el delete
fruits = ["apple", "orange", "cherry", "date", "banana"]
del fruits[1]
del fruits[2]
print(fruits)

# just sonlarni del
num = [1,2,3,4,5,6,7,8,9,10]
del num[1]
del num[2]
del num[3]
del num[4]
del num[5]
print(num)

# 3 index dan 5 idex gacha
my_list = [10,20,30,40,50,60,70,80]
del my_list[3:6]
print(my_list)

# 4
cities = ["New York", "London", "Tokyo", "Moscow", "Paris"]
cities.remove("Tokyo")
print(cities)

# 5
nums = [5,10,15,20,25]
del nums[0]
del nums[-1]
print(nums)

# 6 
fruits =  ["apple", "banana", "cherry", "lemon", "orange", "pineapple"]
fruit = fruits.pop(1)
print(fruit)

