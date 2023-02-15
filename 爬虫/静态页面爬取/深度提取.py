import pandas as pd
from lxml import etree
import requests
import chardet

url = 'http://www.tipdm.com/tipdm/index.html'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
rqq = requests.get(url, headers=head, timeout=2)
html = etree.HTML(rqq.content, etree.HTMLParser())
s1 = html.xpath('/html/head/title')
s2 = html.xpath(
    '/html/body/header/div/nav/ul/li/a[@href="http://www.tipdm.com:80/xkjs/index.jhtml"]/text()')
print(s2)
