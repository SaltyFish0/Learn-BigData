import numpy as np

'''
（1） 创建一个数值从0至1，间隔为0.01的数组。
（2） 生成100个服从正态分布的随机数。
（3） 对创建的两个数组进行四则运算。
（4） 对生成的随机数数组进行简单的统计分析。
'''
result1 = np.arange(0, 1, 0.01)

result2 = np.random.randn(100)

# print(result2 + result1)
# print(result2 - result1)
# print(result2 * result1)
# print(result2 / result1)

# print(np.sort(result2,axis=0))
print(np.mean(result2))