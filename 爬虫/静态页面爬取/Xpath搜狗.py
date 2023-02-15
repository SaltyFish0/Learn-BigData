import pandas as pd
from lxml import etree
import requests
import chardet

url = 'https://weixin.sogou.com/'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
rqq = requests.get(url, headers=head, timeout=2)
html = etree.HTML(rqq.content, etree.HTMLParser(encoding='utf-8'))
s1 = html.xpath('//*[@id="topwords"]/li/a[@title]/text()')
a = [html.xpath('//*[@id="topwords"]/li['+str(i) +
                ']/a[@title]/text()')for i in range(1, 11)]
print(s1)
print(a)

#
# ×¿Êý
