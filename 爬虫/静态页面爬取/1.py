import encodings
from lxml import etree
import requests
import chardet

url = 'http://www.tipdm.com/tipdm/index.html'
# 设置请求头
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
rq = requests.get(url, headers=head, timeout=2)
rq.encoding = chardet.detect(rq.content)['encoding']

h = etree.HTML(rq.content, etree.HTMLParser())
# 若HTML中的节点没有闭合，etree模块也提供自动补全功能。调用tostring方法即可输出修正后的HTML代码，但是结果为bytes类型，需要使用decode方法转成str类型。
result = etree.tostring(h, encoding="utf-8").decode('utf-8')
print(result)
