import requests
from bs4 import BeautifulSoup
# rqq = requests.get('http://www.tipdm.com/tipdm/index.html')
soup = BeautifulSoup(requests.get(
    'http://www.tipdm.com/tipdm/index.html').content, 'lxml')
# print(soup)
# 只能找到首个li

# print(soup.li)
# 获取全部li
# print(soup.findAll('li'))

# find_all方法可通过多种参数遍历搜索文档树中符合条件的所有子节点。
# 获取 nav后对nav里的li进行操作
# a = soup.find_all('nav')
# print(a)
# 输出
# for i in a[0].find_all('li'):
# print(i.string)
# 属性操作link标签
# a = soup.link
# print(a)
# print(a.name)
# print(a.attrs)

# 也可通过键名查找
# a = soup.link
# print(a)
# print(a['type'])
# print(a['href'])

# select - css选择器
# 路径查找
print(soup.select('html>head>title')[0].text)
# print([i.text for i in soup.select('html>head>title')])
# print([i.string for i in soup.select('html>head>title')])
# print(soup.findAll('title')[0].text)


# 类名＋路径查找
print(soup.select('.menu>li'))
# for循环+列表推导式提取
print([i.text for i in soup.select('.menu>li')])
