import matplotlib.pyplot as plt
import requests

# 此网站已经切换为了人民邮电的网站
rqq = requests.get('https://www.ptpress.com.cn/kaptcha.jpg')

with open('./captcha.jpg', 'wb') as f:
    f.write(rqq.content)

pic = plt.imread('./captcha.jpg')
plt.imshow(pic)
plt.show()
a = input('请输入验证码：')
