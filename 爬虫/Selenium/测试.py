from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.get('https://www.runoob.com/')
a = driver.find_element(
    By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/a[1]/h4')
b = driver.current_window_handle
# b = driver.current_url
print(b)
a.click()
driver.switch_to.window(b)
