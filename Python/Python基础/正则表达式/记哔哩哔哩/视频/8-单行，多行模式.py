import re
content = '''
001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80
'''
# re.M为匹配模式
# ^为开头 $为末尾
p = re.compile(r'^\d+', re.M)
for one in p.findall(content):
    print(one)
