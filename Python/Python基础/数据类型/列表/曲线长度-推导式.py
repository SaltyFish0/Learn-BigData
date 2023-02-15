import math

# n为切割的分数
n = 10000
width = 2 * math.pi / n
# 方法一：利用for循环构建核心数据结构
x = []
y = []
for i in range(n):
    x.append(i*width)
for i in x:
    y.append(abs(math.sin(i)))
S = sum(y) * width
print(S)


# 方法二：利用列表推导式构建核心数据结构
s = [abs(math.sin(i * width))*width for i in range(n)]
print(sum(s))
