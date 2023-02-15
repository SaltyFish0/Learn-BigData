# sorted()
# list = sorted(iterable, key=None, reverse=False)
# sorted() 函数会返回一个排好序的列表    iterable 表示指定的序列，key 参数可以自定义排序规则；reverse 参数指定以升序（False，默认）还是降序（True）进行排序
# key 参数和 reverse 参数是可选参数，即可以使用，也可以忽略。
a = [5, 3, 4, 6]
# 列表排序
print(sorted(a))
# 元组排序
b = (4, 6, 7, 3)
print(sorted(b))
# 字典默认按照key进行排序
c = ['你', '我', '是', '爹']
d = {}
for i, j in zip(a, c):
    # print(i, j)
    d[i] = j
# print(d)
# print(sorted(d.items()))
# 对集合进行排序
a = {1, 5, 3, 2, 4}
print(sorted(a))
# 字符串进行排序
a = '3895589021'
print(sorted(a))


# 再次强调，使用 sorted() 函数对序列进行排序， 并不会在原序列的基础进行修改，而是会重新生成一个排好序的列表
# 另外在调用 sorted() 函数时，还可传入一个 key 参数，它可以接受一个函数，该函数的功能是指定 sorted() 函数按照什么标准进行排序。例如：

# chars = ['1http://c.biancheng.net',
#  '4http://c.biancheng.net/python/',
#  '3http://c.biancheng.net/shell/',
#  '2http://c.biancheng.net/java/',
#  '5http://c.biancheng.net/golang/']

# 张有志手离开键盘望向窗外，他想起四年前自己十六岁，觉得自己有无限可能

# 自定义按照字符串长度进行排序

# print(sorted(chars, key=lambda x: len(x)))
c = ['爹', '是', '我', '你']
e = {}
for i, j in zip(a, c):
    print(i, j)
    e[j] = i
print('e', e)
# 字典按照key值排序

sorted(e.items(), key=lambda e: e[1], reverse=True)
str = ""
for i in range(0, 4):
    str += sorted(e.items(), key=lambda e: e[1], reverse=True)[i][0]
print(str)
