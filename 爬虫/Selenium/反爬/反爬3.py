from selenium import webdriver
from lxml import etree
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
import os
driver = webdriver.Firefox()

path1 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"body.txt"
file1 = open(path1, 'w+', encoding='utf-8')

driver.get('https://antispider3.scrape.center/')
try:
    WebDriverWait(driver, 16).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "char"), '白')
    )
except Exception as _:
    print(1)
html = driver.page_source
xhtml = etree.HTML(html, etree.HTMLParser())
result = etree.tostring(xhtml)
print(result)
