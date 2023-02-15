names = ['LL', 'Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
# print([i.upper() for i in names if len(i) > 3])
# 滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：


# 求(x,y),其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表:
list = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5)if y % 2 == 1]
# print(list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
# 此处if主要起条件判断作用，data数据中只有满足if条件的才会被留下，最后统一生成为一个数据列表。
# print([i for i in list if i <= 4])
# print([i if i % 2 == 0 else i*2 for i in range(1, 101)])

# 多重判断(三元运算符嵌套使用)
# print([-i if i > 80 else i*2 if i > 60 else -i if i >
#       40 else i for i in range(1, 101)])


# 字典推导式
d = {'d1': 2, 'd2': 4, 'd4': 1, 'd3': 3}
print(sorted(d.items(), key=lambda a: a[1]))
print({i for i in d.items()})
for i, j in d.items():
    print(j)


li = [i*i for i in range(1, 10) if i % 2 != 0]
print(li)
