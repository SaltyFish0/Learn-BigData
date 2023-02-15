import requests
from bs4 import BeautifulSoup
rqq = requests.get('http://www.tipdm.com/tipdm/index.html')
soup = BeautifulSoup(rqq.content, 'lxml')

# for循环+列表推导式提取
print(soup.head.contents)
print(soup.head.children)
