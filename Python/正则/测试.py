import re
reRule = re.compile(r'.*\d')
str1 = '1995-07-15 上映'
# print(re.search(reRule, str1).group())
print(re.findall(reRule, str1))
# print(reRule.findall(str1))
