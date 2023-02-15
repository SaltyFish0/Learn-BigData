from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lxml import etree
rq = webdriver.Firefox()
rq.get('http://www.le.com/ptv/vplay/30744694.html?ref=index_focus_1')
try:
    WebDriverWait(rq, 16).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "cmt-content"), '小青蛙'))
except Exception as _:
    print('SaltyFish is the eternal SaltyFish')
html = rq.page_source
xhtml = etree.HTML(html, etree.HTMLParser())
xpathResult = xhtml.xpath('//*[@class="cmt-content"]/text()')
print(xpathResult)
