class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0},我的年龄是{1}'.format(self.name, self.age)


stu = Student('张三', 20)
print(dir(stu))  # Student类继承object类，以下所有方法都是object的
print(stu)  # 重写object中__str__方法，__str__方法为打印内存地址;重写后直接调用会输出重写内容
print(stu.__str__)
