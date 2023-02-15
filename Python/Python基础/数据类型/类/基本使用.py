# 创建Human类
from matplotlib.pyplot import cla

# 创建类


class Human:
    # 构造方法(实例化类时自动执行)
    def __init__(self, age, gender):
        self.age = age  # 类的属性
        self.gender = gender
    # 创建方法(如果没有调用就不会执行)

    def sqrt(self, x):  # 类的方法
        return x**2


# 类的使用
zhangfei = Human(age=23, gender='男')  # 类的实例化
print(zhangfei.age)  # 对象属性
print(zhangfei.gender)
print(zhangfei.sqrt(10))  # 调用对象方法


曹操 = Human(age=36, gender='男')  # 类的实例化
print(曹操.age)
print(曹操.gender)
print(曹操.sqrt(7))

print(type(曹操))
