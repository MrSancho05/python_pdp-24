from student import Student

def main():
    student1 = Student('John', 21)
    student2 = Student('Anna', 20)
    student3 = Student('James', 22)

    student1.studentInfo()
    student2.studentInfo()
    student3.studentInfo()
    print(Student.num_id)
    print(Student.name)


if __name__ == '__main__':
    main()