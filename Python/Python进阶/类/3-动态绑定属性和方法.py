class Student:
    # __init__方法中传入的属性是所有实例化对象公用的
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name+"在吃饭")


stu1 = Student('张三', 20)
stu2 = Student('李四', 22)


def show():
    print("定义在类之外的称为函数")


# 为stu1动态绑定方法
stu1.show = show
# 为stu2动态绑定属性
stu2.gender = '女'
stu1.show()
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)
