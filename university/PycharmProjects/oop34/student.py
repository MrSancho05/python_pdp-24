class Student:
    num_id = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Student.num_id += 1
        Student.name = name


    def studentInfo(self):
        print(f'{self.name} is {self.age} years old')