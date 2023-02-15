import re
content = '''绿油油油油油油油'''
# {}规定范围
p = re.compile(r'绿油{2}')
for one in p.findall(content):
    print(one)

tel = '13256778329'
p = re.compile(r'\d{0,11}')
for one in p.findall(tel):
    print(one)
