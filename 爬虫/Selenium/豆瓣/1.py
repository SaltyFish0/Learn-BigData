from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import jieba

path1 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"good.txt"
path2 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"bad.txt"

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://movie.douban.com/subject/26266893/comments?status=P')

good = []
bad = []
goodbtn = driver.find_element(
    By.CSS_SELECTOR, '.comment-filter > label:nth-child(2) > span:nth-child(2)').click()

lists = driver.find_elements(By.XPATH, '//*[@class="short"]')
for i in lists:
    good.append(i.text)

badbtn = driver.find_element(
    By.CSS_SELECTOR, '.comment-filter > label:nth-child(4) > span:nth-child(2)').click()

lists = driver.find_elements(By.XPATH, '//*[@class="short"]')
for i in lists:
    bad.append(i.text)
good = str(good)
bad = str(bad)
file1 = open(path1, 'w+', encoding='UTF-8')
file2 = open(path2, 'w+', encoding='UTF-8')
file1.write(good)
file2.write(bad)
