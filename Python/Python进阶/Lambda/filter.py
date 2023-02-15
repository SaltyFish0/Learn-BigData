# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

# 筛选过滤
original_list = [5, 17, 32, 43, 12, 62, 237, 133, 78, 21]
num = 60
print(list(filter(lambda x: (x > num), original_list)))
# 将满足条件（不可以被2整除）的数字留下
print(list(filter(lambda x: (x % 2 != 0), original_list)))
