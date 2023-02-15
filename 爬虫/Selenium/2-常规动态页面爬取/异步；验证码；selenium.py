from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import base64
import re
import os
import matplotlib.pyplot as plt

# path1 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"myself1.txt"
path1 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"captcha.jpg"

driver = webdriver.Firefox()
driver.get('http://vpn.sdjsxy.cn:5866/https-8443/77726476706e69737468656265737421e4ee538669236c5a6d1090e29b5b/lyuapServer/login?service=http%3A%2F%2Fvpn.sdjsxy.cn:5866%2Flogin%3Fcas_login%3Dtrue')
try:
    WebDriverWait(driver, 40).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "ant-input"), '算术答案'))
except Exception as _:
    print('SaltyFish is the eternal SaltyFish')
html = driver.page_source


pattern = re.compile(
    '<img alt=\"logo\".*?src=\"data:image/png;base64,(.*?)\"', re.DOTALL)
reResult = pattern.findall(html)

p = re.compile(r'\s')
url = re.sub(p, '', reResult[0])

a = base64.b64decode(url)


path1 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"captcha.jpg"
with open(path1, 'wb') as f:
    f.write(a)
pic = plt.imread(path1)
plt.imshow(pic)
plt.show()
