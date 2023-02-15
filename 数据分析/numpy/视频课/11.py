import numpy as np
Z = np.zeros((8, 8), dtype=int)
Z[:4] = 1

print(Z)

# 布尔值索引
X = np.arange(0, 10)
print(X)
print(X > 6)
X = np.arange(0, 100)
# 提取数组中所有奇数
print(X[X % 2 == 0])
X[X % 2 == 0] = -1
print(X)
# 支持加多个条件
