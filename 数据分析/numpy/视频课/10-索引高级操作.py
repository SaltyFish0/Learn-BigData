from re import X
import numpy as np
# 数组索引
arr1 = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr1)
y = arr1[[0, 1, 1], [0, 0, 0]]
# print(y)
arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(arr2)
x = arr1[[0, 0, 0, 0], [0, 0, 0, 0]]
y = arr1[[1, 1, 1, 1], [1, 0, 0, 0]]
print(x)
print(y)
