scores = {'数学': 95, '语文': 89, '英语': 90}
# print([i for i in scores])

# keys() 方法用于返回字典中的所有键（key）；
# values() 方法用于返回字典中所有键对应的值（value）；
# items() 用于返回字典中所有的键值对（key-value）。
# print(scores.keys())

# 也可放在list函数里面转换为list类型
# print(list(scores.keys()))
# print([i for i in scores.keys()])
# # print([i for i in scores.values()])
# print([i for i in scores.items()])

# copy()
# copy() 方法返回一个字典的拷贝，也即返回一个具有相同键值对的新字典
# b = scores.copy()
# b['数学'] = 90
# print(b)
# print([i for i in scores.items()])
# copy() 方法所遵循的拷贝原理，既有深拷贝，也有浅拷贝。拿拷贝字典 a 为例，copy() 方法只会对最表层的键值对进行深拷贝，也就是说，它会再申请一块内存用来存放 {'one': 1, 'two': 2, 'three': []}；而对于某些列表类型的值来说，此方法对其做的是浅拷贝，也就是说，b 中的 [1,2,3] 的值不是自己独有，而是和 a 共有。

# update()
#  update() 方法可以使用一个字典所包含的键值对来更新己有的字典。
# scores.update({'计算机': '满分'})
# print('update', scores)

# pop() 和 popitem()
# pop() 和 popitem() 都用来删除字典中的键值对，不同的是，pop() 用来删除指定的键值对，而 popitem() 用来随机删除一个键值对
# scores.pop('计算机')
# print('pop', scores)
# scores.popitem()
# print('popitem', scores)
# 其实，说 popitem() 随机删除字典中的一个键值对是不准确的，虽然字典是一种无须的列表，但键值对在底层也是有存储顺序的，popitem() 总是弹出底层中的最后一个 key-value，这和列表的 pop() 方法类似，都实现了数据结构中“出栈”的操作。

# setdefault()
# dictname.setdefault(key, defaultvalue)
# setdefault() 方法用来返回某个 key 对应的 value
# 说明，dictname 表示字典名称，key 表示键，defaultvalue 表示默认值（可以不写，不写的话是 None）。
# 当指定的 key 不存在时，setdefault() 会先为这个不存在的 key 设置一个默认的 defaultvalue，然后再返回 defaultvalue。

# 也就是说，setdefault() 方法总能返回指定 key 对应的 value：

# 如果该 key 存在，那么直接返回该 key 对应的 value；
# 如果该 key 不存在，那么先为该 key 设置默认的 defaultvalue，然后再返回该 key 对应的 defaultvalue。


scores.setdefault('语文')
print(scores)
scores.setdefault('数学', 99)
print(scores)
scores.setdefault('计算机', 99)
print(scores)
