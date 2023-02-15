import re
content = '我.我]s/'
# \转义
p = re.compile(r'\..')
print(p.findall(content))
# 反斜杠接字符
# \d 数字
# \D 非数字
# \s 空格、换行
# \S 非空格、换行
# \w 字符
# \W 非字符
p = re.compile(r'\d')
print(p.findall('a111'))
p = re.compile(r'\D')
print(p.findall('a111'))

p = re.compile(r'\D', re.A)
print(p.findall('a111'))
