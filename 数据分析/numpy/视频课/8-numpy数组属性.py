import numpy as np
arr1 = np.arange(0, 10)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# shape 个数
print(arr1.shape)
print(arr2.shape)
# ndim 维度
print(arr1.ndim)
# dtype 类型
print(arr1.dtype)
# itemsize 占用多少字节
print(arr1.itemsize)


# reshape
# 元素个数能整份的情况下，使用reshape调整数组维度
arr3 = np.arange(20).reshape((4, 5))

# resize
arr4 = np.array([[0, 1], [2, 3]])
a = np.resize(arr4, (2, 3))
print(a)

arr5 = np.arange(20)
print(arr5.dtype)
# astype 类型转换
print(arr5.astype('float64').dtype)
