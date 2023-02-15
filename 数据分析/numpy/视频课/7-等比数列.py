import numpy as np
# logspace
# logspace 注意各参数作用
arr1 = np.logspace(0, 9, 10, base=2)
print(arr1)
# arr1 = np.logspace(A, B, C, base=D)
# A : 为生成数组的起始值为D的A次方
# B : 生成数组的结束值为D的B次方
# C : 总共生成C个数
# D : 指数型数组的底数(D的N次方)为D,当省略Base=D时，默认底数为10

# 除了 0 以外的任何数的 0 次方都是 1
arr2 = np.linspace(0, 9, 10)
print(arr2)
