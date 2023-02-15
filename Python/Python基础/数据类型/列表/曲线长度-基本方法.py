import math

# n为切割的分数
n = 10000
width = 2 * math.pi / n
x = []
y = []
for i in range(n):
    x.append(i*width)
for i in x:
    y.append(abs(math.sin(i)))
S = sum(y)*width
print(S)
