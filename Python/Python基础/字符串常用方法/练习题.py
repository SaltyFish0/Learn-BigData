from itertools import count
from pprint import pformat


name = 'aleX leNb '
# (1)移除name变量对应的值得两边的空格，并输出处理结果
# strip
# print(name.strip())

# (2)移除name变量左边的'al'，并输出处理结果
# name = name[1:]
# print(name)

# lstrip
# print(name.lstrip('al'))

# (3)移除name变量右边的'Nb'，并输出处理结果
# name = name[:-3]
# print(name)

# rstrip
# print(name.rstrip('al'))

# (4)移除name变量开头的a与最后的b，并输出处理结果
# strip
# print(name.strip('a b'))

# (5)判断name变量是否已'al'开头，并输出结果
# startswith
# print(name.startswith('al'))

# (6)判断name变量是否已'Nb'结尾，并输出结果
# endswith
# print(name.endswith('Nb '))

# (7)将name变量对应的值中的所有的'l'替换成‘p’, 并输出结果
# replace
# print(name.replace('l', 'p'))

# (8)将name变量对应的值中第一个的'l'替换成‘p’, 并输出结果
# replace
# print(name.replace('l', 'p', 1))


# (9)将name变量对应的值根据所有的'l'分割, 并输出结果
# split
# print(name.split('l'))

# (10)将name变量对应的值根据第一个'l'分割, 并输出结果
# split
# print(name.split('l', 1))


# (11)将name变量对应的值变成大写, 并输出结果
# upper
# print(name.upper())

# (12)将name变量对应的值变成小写, 并输出结果
# lower
# print(name.lower())

# (13)将name变量对应的值首字母'a'大写, 并输出结果
# title
# print(name.title())

# (14)判断name变量对应的值得字母'l'出现几次，并输出结果
# count
# print(name.count('l'))

# (15)判断name变量对应的值前四位字母'l'出现几次，并输出结果
# count
# print(name.count('l', 0, 4))


# (16)从name变量对应的值前找到'N'对应的索引，并输出结果
# index
# print(name.index('N'))

# (17)从name变量对应的值前找到'N'对应的索引(如果找不到则返回-1)，并输出结果
# find
# print(name.find('N'))

# (18)从name变量对应的值前找到'X le'对应的索引，并输出结果
# find
# print(name.find('X le'))

# (19)请输出name变量对应的值的第二个字符
# print(name[2])

# (20)请输出name变量对应的值的前3个字符
# print(name)
# print(name[:3])

# (21)请输出name变量对应的值的后2个字符
# print(name)
# print(name[-3:])


# (22)请输出name变量对应的值中‘e'坐在索引位置字符
# print(name.find('e'))

# (23)获取子序列，去掉最后一个字符


# 2. s = '132a4b5c'
s = '132a4b5c'
# (1)通过对s的切片形成新的字符串s1, s1 = '132'
# print(s[0:3])

# (2)通过对s的切片形成新的字符串s2, s2 = 'a4b'
# print(s[3:6])

# (3)通过对s的切片形成新的字符串s3, s3 = '1245'
# print(s[::2])

# (4)通过对s的切片形成新的字符串s4, s4 = '3ab'
# print(s[1:-2:2])

# (5)通过对s的切片形成新的字符串s5, s5 = 'c'
# print(s[-1:])


# (6)通过对s的切片形成新的字符串s6, s6 = 'ba3'
# print(s[-3::-2])


# 3.实现一个整数加法计数器
# 如：content = input('请输入内容：') #如用户输入5+9或者5+9或者5+9，然后进行分割在进行计算
# str1 = input('请输入内容：')
# print(int(str1.split('+')[0])+int(str1.split('+')[1]))

# 4.计算用户输入的内容中有几个整数，
# 如content = input('请输入内容') #如"fhdal234slfh98769fjdla",统计数字的个数
str2 = 'fhdal234slfh98769fjdla'
count = 0
for i in str2:
    # isdigit
    if i.isdigit():
        count += 1
print(count)
