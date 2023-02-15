import requests
import chardet

url = 'http://www.tipdm.com/tipdm/index.html'
# 设置请求头
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
rq = requests.get(url, headers=head, timeout=2)
rq.encoding = chardet.detect(rq.content)['encoding']
print(rq.text[:10])
print(chardet.detect(rq.content)['encoding'])
