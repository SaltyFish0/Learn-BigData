from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
wd = webdriver.Firefox()

BeforeUrl = '''


3.33 aNw:/ 复制打开抖音，看看【日落时分.的作品】我亲爱的好朋友 想做什么就去做 别畏手畏脚的 无法... https://v.douyin.com/2SnB8eU/




'''
pattern = re.compile('https.*/', flags=re.M)
AfterUrl = pattern.findall(BeforeUrl)[0]

wd.get(AfterUrl)
wd.implicitly_wait(10)
# 判断条件
video = wd.find_elements(By.TAG_NAME, 'video')


def picture(name, flag, mcname):  # 图片
    Divs = wd.find_elements(By.CLASS_NAME, 'qylGvmT4')
    index = 0
    for img in Divs:
        imgSrc = img.find_element(By.TAG_NAME, 'img')
        imgUrl = imgSrc.get_attribute('src')
        # print(imgUrl)
        index += 1
        res = requests.get(imgUrl)

        with open('E:\work area\SaltyFish\抖音\图片\\' + str(name) + str(index)+'.jpg', mode='wb') as f:
            f.write(res.content)

    if(flag):
        music(mcname)



def music(mcname):  # 音乐
    music = wd.find_element(By.TAG_NAME, 'audio')
    musicUrl = music.get_attribute('src')
    res = requests.get(musicUrl)
    with open('E:\work area\SaltyFish\抖音\音乐\\'+str(mcname)+'.mp3', mode='wb') as f:
        f.write(res.content)


def videoFun(name, flag, mcname):  # 视频
    source = video[0].find_element(By.TAG_NAME, 'source')
    SourceUrl = source.get_attribute('src')
    # print(SourceUrl)
    res = requests.get(SourceUrl)

    with open("E:\work area\SaltyFish\抖音\视频\\"+str(name)+".mp4", mode='wb') as f:
        f.write(res.content)

    if(flag):
        with open("E:\work area\SaltyFish\抖音\音乐\\"+str(mcname)+".mp3", mode='wb') as f:
            f.write(res.content)


if len(video) == 0:
    # 图片
    picture('肖生克', False, '音乐')
else:
    # 视频
    videoFun('曙光', False, 'Demons')
