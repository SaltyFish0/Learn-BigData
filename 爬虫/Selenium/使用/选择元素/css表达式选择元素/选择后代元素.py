from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 查找类为plant的元素
# 注意表达式写法
element1 = wd.find_elements(
    By.CSS_SELECTOR, '#container>#layer1>#inner11>span')
for i in element1:
    print(i.get_attribute('outerHTML'))
print()
# 注意表达式写法
element2 = wd.find_elements(By.CSS_SELECTOR, '#container span')
for i in element2:
    print(i.get_attribute('outerHTML'))
print()
# 混用
element3 = wd.find_elements(
    By.CSS_SELECTOR, '#container>#layer1 span')
for i in element3:
    print(i.get_attribute('outerHTML'))
