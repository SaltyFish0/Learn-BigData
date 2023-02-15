import chardet
import requests
url = 'http://www.baidu.com'
rq = requests.get(url)
print(type(chardet.detect(rq.content)))
