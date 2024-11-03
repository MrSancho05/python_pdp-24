# task 1
numbers = [10,20,30,40,50]
numbers[0] = 100
numbers.append(60)
print(numbers)
print(len(numbers))

# task 2
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.append('kiwi')
fruits[1] = 'mango'
fruits.sort()
print(fruits)

# task 3
students = ['Ali', 'Olim', 'Zarina','Jasur', 'Sabrina']
print(students[2])
print(students[0])
print(students[-1])

# task 4
my_tuple = (5, 10, 15, 20, 25)
print(my_tuple[2])
print(len(my_tuple))

# task 5
my_tuple = (1,2,3)
my_list = [1,2,3]
my_list.append(4)
print(my_list)
print(f"{my_tuple} ga hech narsa qo'shma!")

# task 6
colors = ['red', 'green', 'blue']
colorsList = list(colors)
colorsList.append('yellow')
colorsTuple = tuple(colorsList)
print(colorsTuple)

# task 7
numbers = [5, 10, 15, 20, 25]
numbers.append(30)
numbers.reverse()
my_tuple = (10,20,30,40)
my_list = list(my_tuple)
my_list.reverse()
my_tuple2 = tuple(my_list)
print(numbers)
print(my_tuple2)

# task 8
num_list = [10,20,30,40]
num_tuple = (50,60,70,80)
num_list2 = list(num_tuple)
num_list.extend(num_list2)
print(num_list)
print(num_list[0])
print(num_list[-1])

# task 9
nested_tuple = (1, 2, (3, 4, 5), 6, 7)
print(nested_tuple[2])
for x in nested_tuple:
    print(x)

# task 10
numbers = [2, 4, 6, 8, 10]
numbers2 = []
for x in numbers:
    numbers2.append(x * 2)
print(numbers2)

# task 11
my_list = ['apple', 'banana', 'cherry', 'date', 'fig']
del my_list[2]
del my_list[-1]
print(my_list)

# task 12
ages = [34, 23, 45, 27, 56, 18]
ages.sort()
print(ages) 
ages.reverse()
print(ages) 

# task 13
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
numbers2 = list(set(numbers))
print(numbers2)

# task 14
numbers = (10, 50, 25, 5, 100, 75)
print(numbers[-2])
print(numbers[-3])

# task 15
my_list = [10, 20, 30, 40, 50, 60]
result = list(zip(my_list[::2], my_list[1::2]))
print(result)


# task 16
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
alphabetL = alphabet[0:3]
alphabetL2 = alphabet[4:7]
alphabetL_tuple = tuple(alphabetL)
alphabetL_tuple2 = tuple(alphabetL2)
print(alphabetL_tuple)
print(alphabetL_tuple2)

# task 17
names = ['Ali', 'Olim', 'Zarina', 'Jasur']
for name in names:
    print(f'{name} - talaba')

# task 18
temperatures = (22, 25, 28, 30, 27, 23)
for temp in temperatures:
    print(temp)

# task 19
my_list = [1, 5, 'banana', 10, 'apple', 20]
total_sum = sum(i for i in my_list if type(i) == int)
print(total_sum)

# task 20
my_list = [10, 20, 30]
my_tuple = (40, 50, 60)
f = my_list[0]
my_list[0] = my_tuple[0]
my_list2 = list(my_tuple)
my_list2[0] = f
print(my_list)
print(my_list2)
