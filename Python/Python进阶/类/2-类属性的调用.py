class Student:
    # 初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    native_pace = "吉林"

    def eat(self):
        print(self.name, '在吃饭')

    @staticmethod
    def method():  # 静态方法无任何默认参数
        print('staticmethod 进行修饰')

    @classmethod  # 类方法会带cls这个默认参数
    def cm(cls):
        print('classmethod 进行修饰')


print(Student.__name__)


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = "天津"
print(stu1.native_pace)
print(stu2.native_pace)
print('-'*100)
Student.cm()  # 使用cm访问类方法
Student.method()  # 使用类名直接使用静态方法
