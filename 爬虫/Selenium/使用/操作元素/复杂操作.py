from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 没细讲，有需自己看
wd = webdriver.Firefox()
wd.implicitly_wait(5)
wd.get('https://www.baidu.com/')
ac = ActionChains(wd)

ac.move_to_element(
    wd.find_element(By.CSS_SELECTOR, '[name="tj_briicon"]')
).perform()
