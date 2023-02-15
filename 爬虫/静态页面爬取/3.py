from turtle import st
import requests
from lxml import etree
rqq = requests.get('https://www.runoob.com/python3/python3-examples.html')
# print(rqq.text)
html = etree.HTML(rqq.content, etree.HTMLParser())
lis = html.xpath('/html/body/div[4]/div/div[2]/div/div[3]/div/ul/li/a/text()')
newlis = []
index = 0
for j in range(len(lis)):
    index = index+1
    newlis.append(str(index)+"，"+lis[j])
print(newlis)
