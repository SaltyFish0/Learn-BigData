from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
driver = webdriver.Firefox()
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
try:
    WebDriverWait(driver, 16).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '成功'))
except Exception as _:
    print('SaltyFish is the eternal SaltyFish')
html = driver.page_source
pattern = re.compile('<div class=\"content\">(.*?)</div>')
reResult = pattern.findall(html)
print(reResult[0])
driver.quit()
