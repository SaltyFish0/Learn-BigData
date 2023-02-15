from selenium import webdriver
from selenium.webdriver.common.by import By
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
element = wd.find_element(By.CSS_SELECTOR, '#s_radio')

# 根据下标选中
# input1 = element.find_elements(By.CSS_SELECTOR, 'input:nth-child(1)')
# input1[0].click()
# print(input1)

# 根据值选中
input2 = element.find_element(By.CSS_SELECTOR, 'input[value="小雷老师"]')
input2.click()
