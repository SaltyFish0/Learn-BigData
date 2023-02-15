import requests
from lxml import etree
rqq = requests.get('https://weixin.sogou.com/')
html = etree.HTML(rqq.content, etree.HTMLParser(encoding='utf-8'))
lis = html.xpath('/html/body//ol/li/a/text()')
for i in lis:
    print(i)
