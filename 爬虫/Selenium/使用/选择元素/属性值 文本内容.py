from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
wd = webdriver.Firefox()
wd.get('https://www.byhy.net/_files/stock1.html')


element1 = wd.find_element(By.ID, '1')
# .text 获取文本信息
# get_attribute 获取属性
# get_attribute('outerHTML') 获取整段HTML内容
# get_attribute('innerHTML') 获取HTML内部内容
print(element1.text)
print(element1.get_attribute('outerHTML'))
print(element1.get_attribute('innerHTML'))

# 输入框
element2 = wd.find_element(By.ID, 'kw')
# send_keys 输入内容
element2.send_keys('咸鱼')
# text无法获取输入框文本信息
# get_attribute('value') 获取输入框文本信息
# print(element2.text)
print(element2.get_attribute('value'))

# 当有文本信息没有完全展示在界面上时，可以使用innerText或textContent
print(element2.get_attribute('innerText'))
print(element2.get_attribute('textContent'))
