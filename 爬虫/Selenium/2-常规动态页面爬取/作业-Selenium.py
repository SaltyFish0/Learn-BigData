# SaltyFish
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
from lxml import etree
from bs4 import BeautifulSoup
# 打开窗口
driver = webdriver.Firefox()
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
try:
    # WebDriverWait 阻塞程序运行，参数二为最大时长
    # until 满足条件后执行后面的代码，如条件不满足会抛出超时异常
    # text_to_be_present_in_element 指定条件，判断某个元素中是否含有指定的文本
    WebDriverWait(driver, 16).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '成功'))
except Exception as _:
    print('SaltyFish is the eternal SaltyFish')
html = driver.page_source
# 正则提取内容
pattern = re.compile('<div class=\"content\">(.*?)</div>')
reResult = pattern.findall(html)
print(reResult[0])
# xpath提取内容
xhtml = etree.HTML(html, etree.HTMLParser())
xpathResult = xhtml.xpath('//*[@class="content"]/text()')
print(xpathResult[0])
# bs提取内容
bhtml = BeautifulSoup(html, 'lxml')
bsResult = bhtml.select('.content')[0].text
print(bsResult)
# 关闭所有窗口
driver.quit()
