# 迭代
# 遍历一个可迭代对象的过程叫做迭代
# 可迭代对象
# 可以放在for循环后的叫做可迭代对象


# 迭代器
# 迭代器是一种支持next()操作的对象，当执行next()操作时，返回其中一个元素
l1 = [1, 2, 3]
a = iter(l1)
# iter next
print(next(a))
print(next(a))


# 生成器是属于一种特殊的迭代器 生成器是根据一定算法规律生成的
# yield和return相似
# def foo():
#     print('111')
#     yield
#     print('222')
#     yield
#     print('333')
#     yield


# 如果函数里面被定义了yield，那么这个函数就是一个生成器
# 可以通过next来使用这个生成器
# f = foo()
# for i in f:
# 打印时发现生成器返回None，是因为没有定义具体的值
# print(i)

# 用法 根据一定算法规律生成的可以使用yield来代替return
# def foo():
#     for i in range(10):
#         yield i * 2


# for i in foo():
#     print(i)
