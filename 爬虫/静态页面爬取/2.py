import requests
from lxml import etree
rqq = requests.get('https://www.runoob.com/python3/python3-examples.html')
# print(rqq.text)
html = etree.HTML(rqq.content, etree.HTMLParser())
lis = html.xpath('/html/body/div[4]/div/div[2]/div/div[3]/div/ul/li/a/text()')
links = html.xpath('/html/body/div[4]/div/div[2]/div/div[3]/div/ul/li/a/@href')
phref = "https://www.runoob.com/python3/"
newlis = []
index = 0
for j in range(len(lis)):
    index = index+1
    newlis.append(str(index)+"，"+lis[j])

alllink = [phref+i for i in links]
content = []
for i in alllink[0:4]:
    rqq = requests.get(i)
    html = etree.HTML(rqq.content, etree.HTMLParser())
    message = html.xpath('//*[@id="content"]/p/text()')
    content.append(message[0])
result = dict(zip(newlis, content))
for i in result.items():
    print(i)


# //div[@data-category="auctions"]
