from functools import reduce

# Python中，也有几个定义好的全局函数方便使用的，filter, map, reduce　　
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# filter 过滤
# print(list(filter(lambda x: x % 3 == 0, foo)))
# print([i for i in foo if i % 3 == 0])

# map 遍历每个值，返回列表
# print(list(map(lambda x: x * 2 + 10, foo)))
# print([i*2+10 for i in foo])

# reduce 遍历每个值，返回单个值
print(reduce(lambda x, y: x + y, foo))
print(sum(foo))

# https://blog.csdn.net/huang_shao1/article/details/82228450
