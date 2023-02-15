import numpy as np
# arange
# 需掌握方法参数信息

# 注意array(range(3.1))和arange的区别
# arange可遍历浮点型，array则会报错
arr1 = np.arange(3.1)
# arr2 = np.array(range(3.1))
print(arr1)
# print(arr2)

arr3 = np.arange(0, 30, 3)
print(arr3)
# 也可写为
arr3 = np.arange(30, step=3)
print(arr3)

# 200米长，每隔三米插一面旗
# 会不会插到终点
# 共多少面旗帜
arr4 = np.arange(0, 200, 3)
print(arr4)
print(len(arr4))
