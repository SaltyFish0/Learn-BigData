import pandas as pd

# 修改变量、字符串内容： lambda+Map
# Map 函数简介：
# map是python内置函数，会根据提供的函数对指定的序列做映射。格式是map(function, iterable, ...)
# 第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。

# 把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。


def square(x):
    return x ** 2


print(map(square, [1, 2, 3, 4, 5]))

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 所有数字乘以2
print(list(map(lambda x: x*2, original_list)))
original_list = ['analytics', 'vidhya', 'king', 'south', 'east']
# 所有首字符大写
print(list(map(lambda x: x[0].title()+x[1:],
               original_list)))
# print(list(map(lambda x: x.title(), original_list)))

# 判断内容并输出指定结果
# lambda+Map+if
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
orginal = pd.DataFrame({'num': original_list})
orginal['mark'] = orginal['num'].map(
    lambda x: '不可被2整除' if (x % 2 != 0) else '可以被2整除')
print(orginal)


original_list = ['analytics', 'vidhya', 'king', 'south', 'east']
# for i in range(len(original_list)):
#     original_list[i] = original_list[i].title()

# for i in original_list:
#     i = i.title()
# print(original_list)
