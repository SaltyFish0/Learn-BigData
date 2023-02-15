import re
str = '上海交通大学 Shanghai Jiao Tong University 一流大学A类/985/211'
pattern = re.compile('.*?大学')  # 匹配从ab开始，到ef结束的内容
result = pattern.findall(str)
print(result[0])
