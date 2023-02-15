from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 查找类为plant的元素
element1 = wd.find_element(By.CSS_SELECTOR, '.plant')
print(element1.get_attribute('outerHTML'))
# 查找标签为div的元素
element2 = wd.find_elements(By.CSS_SELECTOR, 'div')
print()
for element in element2:
    print(element.get_attribute('outerHTML'))
