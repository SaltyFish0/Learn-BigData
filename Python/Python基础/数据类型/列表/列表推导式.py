List = [1, 2, 3, 4, 5]

# 做一个包含0-9的列表
x = []
for i in range(10):
    x.append(i)


b = [i for i in range(0, 11)]  # 列表推导式
# 前面部分为返回值，后面部分为说明
c = [i**2 for i in range(0, 11)]

# 从1到10所有偶数
d = [i for i in range(1, 10) if i % 2 == 0]
# 从1到10所有奇数
e = [i for i in range(1, 10) if i % 2 != 0]
# 从1到10所有偶数的平方
D = [i**2 for i in range(1, 10) if i % 2 == 0]
