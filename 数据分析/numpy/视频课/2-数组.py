import numpy as np
# Numpy 数组中的元素必须是相同类型的，每个元素都占有大小相同的内存块

# 如果列表中元素类型不想同，则取占用内存空间最大的元素为数组类型。
a0 = np.array([1, '2', 4.3])
# 运行结果全部改为字符串类型
print(a0)
print(a0.dtype)
# 也可指定类型
a0 = np.array([1, '2', 4.3], dtype=int)
print(a0)

# 多维数组，嵌套类型不一样时,也是取占用字节最大的元素
arr0 = np.array([[1, 2, 3], ('1', '2', '3')])
print(arr0)
# print(arr0.shape)


# 创建数组
# np.array
# 参数的作用，不同类型的转换
# np.array(数组序列（必选，dtype 数据类型（可选，copy 是否能被复制（可选，order 以何种内存布局创建数组（可选，ndmin 数组的维度（可选，)

# 创建元组类型数组
a1 = np.array((1, 2, 3, 4, 5))
print(a1)
# range
a2 = np.array(range(10))
print(a2)

# 创建10以内的偶数数组
a3 = [i for i in range(10) if i % 2 == 0]
print(a3)
