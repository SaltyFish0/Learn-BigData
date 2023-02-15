from selenium import webdriver
from selenium.webdriver.common.by import By
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
element = wd.find_element(By.CSS_SELECTOR, '#s_checkbox')
input1 = element.find_elements(By.TAG_NAME, 'input')
for i in input1:
    print(i.get_attribute('checked'))
    if i.get_attribute('checked'):
        i.click()
input2 = element.find_element(By.CSS_SELECTOR, '[value="小雷老师"]')
input2.click()
