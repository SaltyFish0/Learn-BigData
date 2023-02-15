import numpy as np
arr1 = [1, 2, 3, 4]
arr0 = arr1
arr1[0] = 10
# 引用赋值，内存地址一样
print(arr0)
arr2 = np.array([1, 2, 3, 4])
arr3 = arr2
arr2[0] = 10
# 引用赋值，内存地址一样，修改时一起改变
print(arr3)

# ndmin
# ndmin 改变数组维度
arr4 = np.array([1], ndmin=2)
print(arr4)

# mat
arr5 = np.mat([1, 2, 3, 4, 5])
print(type(arr5))
# subok
# subok，既要复制一份副本，又要保持原类型
# 默认为False
arr5c1 = np.array(arr5, subok=True)
arr5c2 = np.array(arr5)
print(type(arr5c1))
print(type(arr5c2))


# 非引用赋值方法
a = np.array([1, 2, 3, 4, 5])
# 直接使用等号赋值会直接将内存地址传递给参数
b = a
print(id(a), id(b))
# np.array() 赋值可实现非引用赋值
b = np.array(a)
print(id(a), id(b))

# copy()
# copy()方法也可实现非引用赋值
c = a.copy()
print(id(a), id(c))
