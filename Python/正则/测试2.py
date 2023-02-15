import re
str = "test1 [zhongkuohao1] test2 [zhongkuohao2] test3 [zhognkuohao3] test4"

# search只找一个符合条件span，带？是非贪婪匹配，找到满足条件最短span。不带？是贪婪匹配，找到最长span
query = re.search("\[.*\]", str, re.I | re.M)
# [zhongkuohao1] test2 [zhongkuohao2] test3 [zhognkuohao3]
print(query.group())

query = re.search("\[.*?\]", str, re.I | re.M)
print(query.group())
# [zhongkuohao1]

# findall是找到所有符合条件的span，返回是list
query = re.findall("\[.*\]", str, re.I | re.M)
# ['[zhongkuohao1] test2 [zhongkuohao2] test3 [zhognkuohao3]']
print(query.group())


query = re.findall("\[.*?\]", str, re.I | re.M)
print(query.group())
# ['[zhongkuohao1]', '[zhongkuohao2]', '[zhognkuohao3]']
