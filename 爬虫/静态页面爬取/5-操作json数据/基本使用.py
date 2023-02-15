import requests
from bs4 import BeautifulSoup
import json
rqq = requests.get('http://www.tipdm.com/tipdm/index.html')
soup = BeautifulSoup(rqq.content, 'lxml')


dat = soup.select('.menu>li>a')

names = [i.text for i in dat]
hrefs = [i['href'] for i in dat]
print(names)
print(hrefs)
with open('./temp.json', 'w+') as f:
    json.dump({'names': names, 'hrefs': hrefs}, f, ensure_ascii=False)
