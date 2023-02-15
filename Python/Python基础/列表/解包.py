# *解包
first, *new, last = [94, 85,99, 9,73, 46]
# print(new)

# 解包压包混合使用
# a = [0, 1, 2]
# b = [1, 2, 3]
# for i, j in zip(a, b):
#     print(i+j)

# 解包压包混合使用
# a = [[1, 2, 3], [4, 5, 6]]
# for x, y in zip(*a):
#     print(x, y)


# _的用法 当一些元素不用时，用_表示是更好的写法，可以让读代码的人知道这个元素是不要的
# person = ('Bob', 20, 50, (11, 20, 2000))
# name, *_, (*_, year) = person
# print(year)

# def myfun(a, *b,c=None):
#      print(a)
#      print(b)
#      print(c)

# 函数传入实参时，可变参数(*)之前的参数不能指定参数名
# myfun(a=1, 2,3,4)
# myfun(1, 2, 3, 4)

# 函数传入实参时，可变参数(*)之后的参数必须指定参数名，否则就会被归到可变参数之中
# myfun(1, 2,3,4)
# myfun(1, 2,3,c = 4)

# 不太理解!
# def mydecorator(func):
#      def wrapper(*args, **kw):
#          print('I am using a decorator.')
#          return func(*args, **kw)
#      return wrapper
#
# @mydecorator
# def myfun(a, b):
#      # @定义myfun相当于myfun = mydecorator(myfun)
#     print(a)
#     print(b)
#
# myfun(1,2)

# 解包作为参数传入函数中
# def myfun(a, b):
#     print(a + b)
# n = [1,2]
# myfun(*n)
#
# bob = {'name': 'Bob', 'age': 30}
# print("{name}'s age is {age}".format(**bob))

