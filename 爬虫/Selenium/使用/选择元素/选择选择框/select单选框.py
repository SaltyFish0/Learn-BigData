from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入Select类
# Select有很多内置函数，可以自己学习
from selenium.webdriver.support.ui import Select
wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
# 单选
select = Select(wd.find_element(By.CSS_SELECTOR, '#ss_single'))
# 文本选择
select.select_by_visible_text("小江老师")

# 多选
select1 = Select(wd.find_element(By.CSS_SELECTOR, '#ss_multi'))
# 清除所有已选项
select1.deselect_all()
# 文本选择
select1.select_by_visible_text('小雷老师')
select1.select_by_visible_text('小凯老师')
