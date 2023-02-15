import requests
import matplotlib.pyplot as plt
from http.cookiejar import LWPCookieJar

s = requests.Session()

s.cookies = LWPCookieJar('cookie')
url = 'http://www.tipdm.org/login.jspx'

login = {'username': 'pc2019',
         'password': 'pc2019',
         }
rqq = s.post(url, data=login)
print(rqq.url)  # 检测正常登录
s.cookies.save(ignore_discard=True, ignore_expires=True)  # save cookies
