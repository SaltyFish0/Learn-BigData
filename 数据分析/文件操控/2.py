import re
rule1 = re.compile('[0-9]')
str = '250波西米亚狂想曲'
print(re.findall(rule1, str))