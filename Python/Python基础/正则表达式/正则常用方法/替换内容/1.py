import re
str = '上海交通大学 Shanghai Jiao Tong University 一流大学A类/985/211'
pattern = ".*?大学"
subst = ""
school = re.sub(pattern, subst, str, 1)
print(school)
