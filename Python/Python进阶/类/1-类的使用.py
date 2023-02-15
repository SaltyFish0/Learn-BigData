# 定义类

class Student:  # 类名首字母大写，其余小写
    # 初始化
    def __init__(self, name, age):
        self.name = name  # self.name称为实体属性，进行了一个赋值的操作，将局部变量的name赋值给实体属性
        self.age = age

    native_pace = "吉林"  # 直接写在类里的变量，称为类属性

    def eat(self):  # 实例方法
        print(self.name, '在吃饭')

    @staticmethod  # staticmethod后为静态方法
    def method():
        print('staticmethod')

    @classmethod  # classmethod为类方法
    def cm(cls):
        print('classmethod')


# 类之外定义的称为函数，类之内定义的称为方法(实例方法
print(Student.__name__)


# 创建Student类的对象 | 类的实例化
stu1 = Student('张三', 20)
print(id(stu1))
print(type(stu1))
print(stu1.name)

stu1.eat()  # 调用eat方法
Student.eat(stu1)  # = stu1.eat()
# 类名.方法名(类的对象) => 实际上就是方法定义处的self
