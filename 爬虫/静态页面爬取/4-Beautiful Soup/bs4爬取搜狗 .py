import imp


import requests
from bs4 import BeautifulSoup
rqq = requests.get('https://weixin.sogou.com/')
# 转换
soup = BeautifulSoup(rqq.content, 'lxml')
# select（css选择器）提取
# print(soup.select('.hot-news'))
# print(soup.select('#topwords>li>a'))
# for循环＋列表推导式获取想要内容
# print([i.text for i in soup.select('#topwords>li>a')])


# find_all提取
a = soup.find_all(id='topwords')[0]
print([i.text for i in a.find_all('a')])
print([i.string for i in a.find_all('a')])
