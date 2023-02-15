import requests
cookie = 'uniqueVisitorId=a2151df1-4833-00ae-72e0-f4b99d2b7be2; pgv_pvid=2326009190; _site_id_cookie=1; clientlanguage=zh_CN; __qc_wId=658; username=pc2019; sso_logout=true; JSESSIONID=F9925FFA300D4AFD87F275194C7837CF'
Cookies = {}
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
# 打断cookie并格式化
for i in cookie.split(';'):
    key, value = i.split('=')
    Cookies[key] = value
print(Cookies)
# 将格式化后的cookie传入到requests
a = requests.get('http://www.tipdm.org/member/index.jspx',
                 cookies=Cookies, headers=head).content.decode('utf-8')
# 会员页面表示登录成功，反之失败
print(a)
