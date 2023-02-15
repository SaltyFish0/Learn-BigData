import re
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.get('https://antispider9.scrape.center/')


filmTlist = []  # 上映时间
filmAlist = []  # 地点
reRule = re.compile(r'.*\d')
findfilmLlist = driver.find_elements(
    By.XPATH, '//div[@class="m-v-sm info"]/span[1]')
for i in findfilmLlist:
    if(reRule.findall(i.text)):
        filmTlist.append(reRule.findall(i.text)[0])
    else:
        filmAlist.append(i.text)

findfilmDlist = driver.find_elements(
    By.XPATH, '//div[@class="m-v-sm info"]/span[3]')
filmDlist = [i.text for i in findfilmDlist]  # 时长

findfilmNlist = driver.find_elements(By.CLASS_NAME, 'm-b-sm')
filmNlist = [i.text for i in findfilmNlist]  # 电影名称
print(filmTlist)
print(filmAlist)
print(filmDlist)
print(filmNlist)
print(len(filmTlist))
print(len(filmAlist))
print(len(filmDlist))
print(len(filmNlist))
