import re
content = '''苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的'''
p = re.compile(r'.色')
# r
# .表示匹配除了换行符外的任意单个字符
# findall找到所有符合条件的文本
for one in p.findall(content):
    print(one)
