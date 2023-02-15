from cgitb import text
import re
# import os
# p = os.getcwd()
# print(type(p))
file = open('D:\Python\messg.txt', 'r+', encoding='utf-8')
txt = file.read().lower()
print(txt)
# 查找有多少to
result = re.findall(' to ', txt)
print(result)
print(len(result))
# 已a开头，并且有三个字母
result = re.findall('a...', txt)
print(result)
print(len(result))
# 过滤中部空格
result = re.findall('a[a-z][a-z]', txt)
print(result)
print(len(result))
# 单词边界
result = re.findall(' a[a-z][a-z] ', txt)
print(result)
print(len(result))
# 单词边界
result = re.findall('(a[a-z][a-z])', txt)
# 去重
result = set(result)
print(result)

file.close()
