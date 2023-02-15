print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = C('Jack', 20)
print(x.__dict__)  # 实例对象的属性
print(C.__dict__)  # 类 对象的属性

print(x.__class__)  # 输出对象所属的类
print(C.__bases__)  # C类的父类类型的元素

print(C.__mro__)  # 类的层次结构

# 方法
a = 20
b = 100
print("s"+"s")


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return '加'


stu1 = Student('张三')
stu2 = Student('李四 ')
print(stu1+stu2)  # 实现了两个对象的加法运算，在类中重写obj __add__方法
print(__name__)
