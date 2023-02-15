import requests
import re

url = 'https://www.dytt89.com//i/106001.html'
rqq = requests.get(url)

data = rqq.content.decode('gb18030')

print(data)

reRule1 = re.compile(r'◎片　　名.(.*?)<')
