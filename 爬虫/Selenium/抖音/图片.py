from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

wd = webdriver.Firefox()
# https: // www.douyin.com/video/7102298672594947358
wd.get('https://v.douyin.com/Yaa3onQ/')
wd.implicitly_wait(18)
video = wd.find_elements(By.TAG_NAME, 'video')
if len(video) == 0:
    print('图片')
else:
    source = video[0].find_element(By.TAG_NAME, 'source')
    url = source.get_attribute('src')
    print(url)
    res = requests.get(url)

    # with open("b.mp4", mode='wb') as f:
    #     f.write(res.content)
