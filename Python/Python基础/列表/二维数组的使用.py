# __author__ = 'LaoYue'
# -*- coding: utf-8 -*-

array = ['aa', 'bb', 'cc', 'dd']
matrix = [array] * 3
print('扩充后的数组：', matrix)

matrix1 = [['aa', 'bb'], ['cc', 'dd'], ['ee', 'ff']]
print('数组matrix1[0][1]', matrix1[0][1])
print('数组matrix1的长度：', len(matrix1))

# 打印二维数组的行
for i in range(len(matrix1)):
    print(matrix1[i])

# 打印二维数组的每一个值
for i in range(len(matrix1)):
    for k in range(len(matrix1[i])):
        print(matrix1[i][k])
