class Car:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 加__外部不能引用

    def show(self):
        print(self.name, self.__age)


car = Car('宝马X5', 20)
car.show()
print(car.name)
# dir()
print(dir(car))
print(car._Car__age)  # 在类的外部可以通过_Car__age来访问私有变量
