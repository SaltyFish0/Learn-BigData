string = "Go salted fish, go world"
# 键不能相同，如有相同则后者覆盖前者
# 只能用不可变的数据类型来做字典键，list不可用做字典键
dict_first = {
    'the': 2,
    3.4: [2.5, 4],
    'the': 3,

}


# 字典增删改查
dict_first['the']  # 通过键来索引对应的值
dict_first['the'] = 5  # 修改字典中的值
dict_first['world'] = 2.5  # 修改字典中的值
# update在字典末尾追加一个或多个元素
dict_first.update({'hellow world': 3, 4.5: [2.3, 1.2]})

del dict_first['world']  # 删除字典中指定的键值对

dict_first.keys()  # 把字典中所有键取出
dict_first.values()  # 把字典中所有值取出
dict_first.items()  # 把字典中所有项取出，结果不是字典类型，而是dict_items类型


{i: i for i in range(1, 10)}  # 字典推导式
