# class 子类类名(父类1,父类2...):pass
# Python支持多继承
class Person(object):  # Person 继承 object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):  # format
        print('姓名：{0},年龄：{1}'.format(self.name, self.age))

# 定义子类


class Student(Person):  # Student继承Person
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):  # 重写方法
        # 继续使用父类方法
        super().info()
        # 新增方法
        print(self.score)


class Teacher(Person):  # Student继承Person
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        # super().info()
        # 直接重写，不需父类方法
        print(self.stu_no)


stu = Student('Jack', 20, '1001')
teacher = Teacher('李四', 18, 1)
stu.info()
print('----')
teacher.info()
