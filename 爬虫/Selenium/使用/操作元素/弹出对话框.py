import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Alert 信息框
# Confirm 选择框
# Prompt 输入框
wd = webdriver.Firefox()
wd.implicitly_wait(5)
wd.get('https://cdn2.byhy.net/files/selenium/test4.html')

# 点击Alert按钮
wd.find_element(By.ID, 'b1').click()
# 对话框文本信息
print(wd.switch_to.alert.text)
time.sleep(1)
# 点击OK按钮
wd.switch_to.alert.accept()

# 点击Confirm按钮
wd.find_element(By.ID, 'b2').click()
print(wd.switch_to.alert.text)
time.sleep(1)
# wd.switch_to.alert.accept()
# 点击取消按钮
wd.switch_to.alert.dismiss()

# Prompt
# 获取，点击 确认 取消和前面一样。
# 输入使用
wd.find_element(By.ID, 'b3').click()
# 获取 alert 对象
alert = wd.switch_to.alert
alert.send_keys('web自动化 - selenium')
alert.accept()  # OK
