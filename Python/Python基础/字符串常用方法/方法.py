from unicodedata import name


str1 = 'pyt'
str2 = 'pyton1'
# in 判断字符串str2是否包含另一个字符串str1，结果是True或False
print('in', str1 in str2)

# not in 判断一个字符串str2是否不包含另一个字符串str1，结果是True或False
print('not in', str1 not in str2)
print('len', len(str1))
str3 = "1234"

# max(字符串) min(字符串)用于获取字符串中排序最大/小的字符
print('max', max(str3))
print('min', min(str3))

# 字符串.islower()/字符串.isupper() 判断字符串是否是全小/大写字母组成，结果是True或False
print('islower', str1.islower())
print('isupper', str1.isupper())

# 字符串.isdigit()/字符串.isalpha()/字符串.isalnum() 判断字符串是否是全数字/全字母/全数字或全字母或全数字字母，结果是True或False
print('isdigit', str1.isdigit())
print('isalpha', str1.isalpha())
print('isalnum', str1.isalnum())

str4 = "Saltyfish"
# 字符串.istitle() 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
print('istitle', str4.istitle())
# startswith(字符串)/endswith(字符串) 判断字符串是否以指定字符串开始/结尾，结果是True或False
print('startswith', str4.startswith('Salty'))
print('endswith', str4.endswith('Salty'))
# 支持索引操作
# 从字符串的第0个索引到底长度个索引，是否用Salty开
print('startswith', str4.startswith('Salty', 0, len(str4)))
print('endswith', str4.endswith('i', 0, 7))

# 字符串.lower()/upper()
# 字符串中所有字母转小写/大写字母，返回一个新的字符串

# 字符串.swapcase()
# 字符串中字母大写转小写，小写转大写

# 字符串.title()
# 字符串中每个单词首字母大写，其余字母小写 （区分特殊字符或者数字）
# 字符串.capitalize()
# 字符串首个字母大写，其余字母全部小写


# 字符串.lstrip(要删的字符)
# 删除左侧的字符，无参数就是去除左侧空格
# 字符串.rstrip(要删的字符)
# 删除左侧的字符，无参数就是去除右侧空格

# 字符串.strip(参数)
# 含义：去掉字符串左右两侧在参数字符串中包含的所有字符
# 参数的含义：包含了若干个字符的字符串，如果不写参数的话是去空格，默认只能去前后空格
str5 = ' * salty fish *'
print('rstrip', str5.lstrip())
print('rstrip', str5.rstrip('*'))

print('title', str5.title())
print('capitalize', str5.capitalize())
print('strip', str5.strip('* '))

# 字符串.ljust(len,str)/字符串.rjust(len,str)
# 含义：使用指定字符在原始字符串右侧/左侧补充到长度为指定值
# 参数：len:补充字符后的字符串长度
# 参数：str:补充的字符，如果使用多个字符组成的字符串将报错
print(str5)
print(len(str5))
print('ljust', str5.ljust(16, '6'))
print('rjust', str5.rjust(16, 'a'))

# 字符串.center(len,str)
# 含义：使用指定字符在原始字符串两侧补充到长度为指定值，右侧补充数量≥左侧补充数量
# 参数：len:补充字符后的字符串长度
# 参数：str:补充的字符，如果使用多个字符组成的字符串将报错
print('center', str5.center(18, '6'))

# 字符串.split(str)
# 含义：使用参数作为分割线将原始字符串拆分成若干个字符串并组织成列表返回
# 参数：比对字符串
print(str5)
print('split', str5.split(' '))
print('split', str5.split('*'))


# 要加的字符串.join(改变的字符串)
# 含义：将原始字符串填充到参数的每个字符之间组成新的字符串返回
# 参数：待填充的字符串
str6 = '1'.join(str5)
print('join', str6)

# 要查的字符串.find(查什么,begin,end)
# 要查的字符串.index(查什么,begin,end)
# 含义：从左侧查找字符串从指定开始位置到指定结束位置间第一次出现的索引位置
# 参数：begin: 开始索引，整数, 该值要小于end，否则结果为-1
# 参数：end: 结束索引，整数, 改制要小于begin，否则结果为-1

# find返回值：结果是一个int整数，如没有查找到返回-1
# index返回值：结果是一个int整数，如没有查找到会报错
print(str5)
print('find', str5.find('f'))
print('find', str5.find('f', 5, 13))
print('index', str5.index('f'))

# 字符串.count(str)
# 含义：查询指定字符串在原始字符串中出现的次数
# 参数：被查询的字符串
# 返回值：结果是一个int整数
print(str5)
print('count', str5.count('s'))

# 字符串.replace(old_str, new_str, num)
# 含义：使用新字符串替换原始字符串中的指定字符串信息
# 参数：old_str: 被替换的字符串
# 参数：new_str: 新字符串
# 参数：num：替换数量
# 返回值：结果是一个字符串
print(str5)
print(str5.replace('s', '艾斯'))
