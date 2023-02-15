import numpy as np
arr1 = np.arange(1, 11)
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(arr1)
# print(arr2)
# 开始 结束 步长
# arr1 = arr1[2:7:2]
# print(arr1)
# 一维和数组方式一样
# 二维切片

#
arr2 = np.arange(20).reshape(4, 5)
# print(arr2.ndim)
# 单个值按行
# print(arr2[2])
# 两个值为行列
# print(arr2[2][0:3])


# 高级操作
print(arr2)
# 所有行都要，第一列  (第一列的所有行)
print(arr2[..., 1])
print(arr2[...][1])
# 第一行的所有列
print(arr2[1][...])
print(arr2[1, ...])
