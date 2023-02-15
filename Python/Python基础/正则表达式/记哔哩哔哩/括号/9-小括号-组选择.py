import re
salty = '''苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的'''
# r = re.compile(r'^(.*)，', re.M)
# for i in r.findall(salty):
#     print(i)

# r = re.compile(r'^(.*)(，)', re.M)
# for i in r.findall(salty):
#     print(i)

message = '''
张三，手机号码15945678901
李四，手机号码13945677701
王二，手机号码13845666901
'''
r = re.compile(r'^(.+)，.+?(\d{11})$', re.M)
for i in r.findall(message):
    print(i)
