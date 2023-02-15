# 左闭右开
# for i in range(3, 6):
# print(i, end=" ")

# 参数 开始，结束，步长
# for i in range(0, 100, 2):
# print(i)

# 制作\转换列表
# 转元组 tuple（range( ) )
# 转函数set（range( ) )
b = list(range(1, 10))
# print(b)

# 可以在for循环中使用range
for i in range(0, 10, 2):
    print(i)

# range()产生的数字具有可叠加性（iterable），可以通过sum()函数对其进行求和处理
print(sum(range(0, 5)))
