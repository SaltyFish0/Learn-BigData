import re
source = "<html><body><p></p></body></html>"
# *+?都是贪婪的，使用他们时会尽可能多的匹配内容
r1 = re.compile(r'<.*>')
print(r1.findall(source))
# ?可取消贪婪模式
r2 = re.compile(r'<.*?>')
print(r2.findall(source))
