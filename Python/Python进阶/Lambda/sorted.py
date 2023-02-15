# lambda 表达式是 Python 中一类特殊的定义函数的形式，使用它可以定义一个匿名函数。与其它语言不同，Python 的 lambda 表达式的函数体只能有单独的一条语句，也就是返回值表达式语句。

#  使用 lambda 表达式对一维数组进行倒序排序
nums = [2, 3, 0, 1, 5, 4]
# print(sorted(nums, key=lambda a: a))

# 按照二维矩阵下标为 1 的列进行排序
matrix = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# print(sorted(matrix, key=lambda a: a[1]))

# 以 age 的降序进行排序
array = [{"age": 20, "name": "a"}, {
    "age": 25, "name": "b"}, {"age": 10, "name": "c"}]
print(sorted(array, key=lambda a: a['age']))


d1 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18},
      {'name': 'darl', 'score': 28}, {'name': 'christ', 'score': 28}]
# print(d1[0]['name'])
# print(d1[0]['score'])
print(sorted(d1, key=lambda a: a['score']))


print(sorted(d1, key=lambda a: a['score'], reverse=True))
