#  查找一个匹配项
# search： 查找任意位置的匹配项
# match： 必须从字符串开头匹配
# fullmatch： 整个字符串与正则完全匹配
import re
text = "你去b，你去b"
pattern = r'你去b，你去b'
a = '山东省临沂市蒙阴县'
b = r'省(.*市)'
# 查找任意位置
# group()
print('search：', re.search(pattern, text).group())
# 字符串开头匹配
print('match：', re.match(pattern, text).group())
print('match：', re.match(b, a).group())

# 整个字符串与正则完全匹配
print('fullmatch：', re.fullmatch(pattern, text).group())


# 查找多个匹配项
# findall： 从字符串任意位置查找，返回一个列表
# finditer：从字符串任意位置查找，返回一个迭代器

# 两个方法基本类似，只不过一个是返回列表，一个是返回迭代器。我们知道列表是一次性生成在内存中，而迭代器是需要使用时一点一点生成出来的，内存使用更优。
print('findall：', re.findall(pattern, text))
print('finditer', list(re.finditer(pattern, text)))
# 如果可能存在大量的匹配项的话，建议使用finditer函数，一般情况使用findall函数基本没啥影响。


# 分割
# re.split(pattern, string, maxsplit=0, flags=0)

# pattern：相当于str.split()中的sep，分隔符的意思，不但可以是字符串，也可以为正则表达式: '[ab]'，表示的意思就是取a和b的任意一个值
# string：要进行分割的字符串
# maxsplit：分割的最大次数，默认值为0，表示分割次数无限制，能分几次分几次；取负数，表示不分割；若大于0，表示最多分割maxsplit次；
# flags：该参数可以用来修改pattern表达式的功能，比如忽略大小写 re.IGNORECASE(简写：re.I)，即当flags = re.IGNORECASE, pattern = [A-Z]不但能匹配到大写字母，也能匹配到小写字母；

s = '1,2,3,4,a,5,6,7,8,b,9,10,11,12'
print(re.split(',[a-b],', s, maxsplit=1, flags=0))


# 替换
# 替换主要有sub函数 与 subn函数，他们功能类似！

# re.sub(pattern, repl, string, count=0, flags=0)
# repl替换掉string中被pattern匹配的字符， count表示最大替换次数，flags表示正则表达式的常量。
# sub函数中的入参：repl替换内容既可以是字符串，也可以是一个函数哦！ 如果repl为函数时，只能有一个入参：Match匹配对象。
s = '1,2,3,4,a,5,6,7,8,b,9,10,11,12'
print(re.sub(',[a-b],', '我', s))

# re.subn(pattern, repl, string, count=0, flags=0) 函数与 re.sub函数 功能一致
# 返回一个元组包含替换完成后的字符串和替换次数)。
s = '1,2,3,4,a,5,6,7,8,b,9,10,11,12'
print(re.subn(',[a-b],', '我', s))
