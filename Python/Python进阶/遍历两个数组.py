name_list = ['张三', '李四', '王五']
age_list = [54, 18, 34]
# zip
# zip() 函数是 Python 内置函数之一，它可以将多个序列（列表、元组、字典、集合、字符串以及 range() 区间构成的列表）“压缩”成一个 zip 对象。所谓“压缩”，其实就是将这些序列中对应位置的元素重新组合，生成一个个新的元组。
for name, age in zip(name_list, age_list):
    print(name, ":", age)
print([x for x in zip(name_list, age_list)])

# 下标
n = 0
for i in name_list:
    print(i, "：", age_list[n])
    n += 1
