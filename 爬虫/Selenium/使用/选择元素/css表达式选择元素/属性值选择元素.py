from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

element1 = wd.find_elements(
    By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
for i in element1:
    print(i.get_attribute('outerHTML'))

element2 = wd.find_elements(
    # 模糊查询？查找所有含有href的标签
    By.CSS_SELECTOR, '[href]')
for i in element2:
    print(i.get_attribute('outerHTML'))

element3 = wd.find_elements(
    # 查找所有含有href的a标签
    By.CSS_SELECTOR, 'a[href]')
for i in element2:
    print(i.get_attribute('outerHTML'))
