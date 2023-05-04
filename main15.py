"""class Student:
    def __init__(self,name,sex,score):
        self.name = name
        self.sex = sex
        self.score = score
    def __str__(self):
        return f"学生姓名：{self.name}，性别：{self.sex}，分数：{self.score}"
class StudentManager:
    def __init__(self):
        self.number = -1
        self.student_list = []
    def add_student(self,student):
        self.student_list.append(student)
    def __iter__(self):
        return self
    def __next__(self):
        if self.number < len(self.student_list)-1:
            self.number += 1
            return self.student_list[self.number]
        else:
            raise StopIteration
'''第三关：创建StudentManager类的对象student_class，并向其属性self.student_list中添加Student类对象，添加完成后，遍历student_class
student_class = StudentManager()
student_class.add_student(Student("小千","男",90))
student_class.add_student(Student("小锋","女",89))
student_class.add_student(Student("小狮","男",87))
student_class.add_student(Student("小明","女",93))
for item in student_class:
    print(item)
'''
'''对第三关的student_class中的Student对象按照分数进行排序，使用sorted()函数。
student_class = StudentManager()
student_class.add_student(Student("小千","男",90))
student_class.add_student(Student("小锋","女",89))
student_class.add_student(Student("小狮","男",87))
student_class.add_student(Student("小明","女",93))
sort_student = sorted(student_class,key=lambda item:item.score)
for item in sort_student:
    print(item)
'''
'''student_class = StudentManager()
student_class.add_student(Student("小千","男",90))
student_class.add_student(Student("小锋","女",89))
student_class.add_student(Student("小狮","男",87))
student_class.add_student(Student("小明","女",93))
filter_student = filter(lambda item:item.sex == "女",student_class)
for item in filter_student:
    print(item)

student_class = StudentManager()
student_class.add_student(Student("小千","男",90))
student_class.add_student(Student("小锋","女",89))
student_class.add_student(Student("小狮","男",87))
student_class.add_student(Student("小明","女",93))
filter_student = filter(lambda item:item.sex == "女",student_class)
for item in filter_student:
    print(item)
'''
"""
'''将StudentManager类中的__iter__()和__next__()方法去掉，改为生成器函数的形式
class Student:
    def __init__(self,name,sex,score):
        self.name = name
        self.sex = sex
        self.score = score
    def __str__(self):
        return f"学生姓名：{self.name}，性别：{self.sex}，分数：{self.score}"
class StudentManager:
    def __init__(self):
        self.number = -1
        self.student_list = []
    def add_student(self, student):
        self.student_list.append(student)
    def student_generator(self):
        for item in self.student_list:
            yield item
student_class = StudentManager()
student_class.add_student(Student("小千","男",90))
student_class.add_student(Student("小锋","女",89))
student_class.add_student(Student("小狮","男",87))
student_class.add_student(Student("小明","女",93))
for item in student_class.student_generator():
    print(item)
print("student_class中的Student对象按照分数排序后：")
sort_student = sorted(student_class.student_generator(),key=lambda item:item.score)
for item in sort_student:
    print(item)
print("筛选出student_class中性别为女的Student对象：")
filter_student = filter(lambda item:item.sex == "女",student_class.student_generator())
for item in filter_student:
    print(item)
'''
