from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
wd = webdriver.Firefox()

BeforeUrl = '2.51 GIv:/ 别给自己设限 你有无限可能～%化妆  https://v.douyin.com/Ym5aYqH/ 复制此链接，打开Dou音搜索，直接观看视频！'
pattern = re.compile('https.*/')
AfterUrl = pattern.findall(BeforeUrl)[0]

wd.get(AfterUrl)
wd.implicitly_wait(10)
music = wd.find_element(By.TAG_NAME, 'audio')
musicUrl = music.get_attribute('src')
res = requests.get(musicUrl)
with open('E:\work area\SaltyFish\抖音\音乐\\'+'a.mp3', mode='wb') as f:
    f.write(res.content)
