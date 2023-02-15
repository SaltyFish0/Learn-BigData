# 中括号创建列表
all_in_list = [0.25, 'hello', 'True', [2.3, 1.5]]
# list方法转换列表
list_examle = list('ABCD')

# 列表的索引及切片操作
# 索引返回的类型为具体的值
print(all_in_list[0])  # 索引操作
print(all_in_list[-1])
# 切片返回的类型还是列表
print(all_in_list[:3])  # 取前三个元素
# 切片操作  从左往右  左闭右开
print(all_in_list[-3:])  # 取后三个元素

print(all_in_list[:])  # 所有元素


# 增删改查
# 为列表新增元素
# append将待添加元素作为整体添加值末尾
all_in_list.append(0.78)  # 列表末尾追加一个元素
all_in_list.append([1, 2])
# extend将待添加元素分别追加至目标的末尾
all_in_list.extend([1, 2])
# insert将待添加元素插入至指定位置
all_in_list.insert(0, 'SaltyFish')
# 将两个列表中的元素进行合并
all_in_list + all_in_list

# 删除列表中的元素
all_in_list.remove([2.3, 1.5])  # 删除列表中指定元素
del all_in_list[0:2]  # 删除指定位置元素|多个元素
del all_in_list  # 删除列表本身


# 修改列表中的元素
all_in_list = [0.25, 'hello', 'True', [2.3, 1.5]]
all_in_list[0] = 125  # 通过赋值来修改列表中的元素
