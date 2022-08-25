from distutils.command.build_scripts import first_line_re


class Student:

    number_of_students = 0
    school = 'Online School'

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} major!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} going to {self.school}'

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)

student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student('John', 'John', 'Math')
new_student = 'Adil.Yutzy.English'
student_3 = Student.split_students(new_student)
print(student_3.fullname_major_school())


'''student_1 = Student()
student_2 = Student()

student_1.first_name = 'Eric'
student_1.last_name = 'Roby'
student_1.major = 'Computer Science'

student_2.first_name = 'John'
student_2.last_name = 'Miller'
student_2.major = 'Math'

print(student_1.first_name)
print(student_2.first_name)'''
