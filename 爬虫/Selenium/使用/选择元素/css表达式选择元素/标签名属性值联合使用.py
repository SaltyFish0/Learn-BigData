from selenium import webdriver
from selenium.webdriver.common.by import By
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 可以使用浏览器 Ctrl+F 来验证表达式是否正确
element3 = wd.find_elements(
    By.CSS_SELECTOR, 'div.footer2 span>a[href]')
for i in element3:
    print(i.get_attribute('outerHTML'))
