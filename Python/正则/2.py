import re
str = '3室2厅1卫'


reRule = re.compile(r'(.)室')
print(re.findall(reRule, str)[0])