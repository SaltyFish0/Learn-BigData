from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
wd = webdriver.Firefox()

BeforeUrl = '9.25 bnq:/ 一份来自于晓人的浪漫%%幽灵线东京 %%单机游戏 %%游戏   https://v.douyin.com/YaCA5R3/ 复制此链接，打开Dou音搜索，直接观看视频！'
pattern = re.compile('https.*/')
AfterUrl = pattern.findall(BeforeUrl)[0]

wd.get(AfterUrl)
wd.implicitly_wait(10)
video = wd.find_elements(By.TAG_NAME, 'video')
if len(video) == 0:
    Divs = wd.find_elements(By.CLASS_NAME, 'qylGvmT4')
    index = 0
    for img in Divs:
        imgsrc = img.find_element(By.TAG_NAME, 'img')
        imgUrl = imgsrc.get_attribute('src')
        # print(imgUrl)
        index += 1
        res = requests.get(imgUrl)

        with open('E:\work area\SaltyFish\抖音\图片\\'+str(index)+'.jpg', mode='wb') as f:
            f.write(res.content)
else:
    source = video[0].find_element(By.TAG_NAME, 'source')
    SourceUrl = source.get_attribute('src')
    # print(SourceUrl)
    res = requests.get(SourceUrl)

    with open("E:\work area\SaltyFish\抖音\视频\\a.mp4", mode='wb') as f:
        f.write(res.content)
