from selenium import webdriver
from selenium.webdriver.common.by import By
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

# wd.switch_to.frame() 切换到frame里面
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, '[src="sample1.html"]'))
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')
for i in elements:
    print(i.get_attribute('outerHTML'))
# wd.switch_to.default_content() 切换回frame外面
wd.switch_to.default_content()
wd.find_element(By.ID, 'outerbutton').click()

# wd.quit()
