import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get(
    'http://www.tipdm.com/tipdm/index.html').content, 'lxml')
print(soup.select('html>head>title')[0].text)
print([i.text for i in soup.select('.menu>li')])
