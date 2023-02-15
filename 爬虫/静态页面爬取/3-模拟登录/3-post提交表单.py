import requests
# 绘图包
import matplotlib.pyplot as plt
url = "https://www.ptpress.com.cn/login"

code_url = 'https://www.ptpress.com.cn/kaptcha.jpg'
# Session会话操作(防止验证码不一致)
# requests.Session()实例化会话对象
sess = requests.Session()
print(sess)
rq_code = sess.get(code_url)  # 对验证码的网页进行请求发送
with open('./code.jpg', 'wb') as f:
    f.write(rq_code.content)


def get_code():
    # 人为手动识别验证码
    pic = plt.imread('./code.jpg')  # image_read读取图片
    plt.imshow(pic)  # imshow展示图片
    plt.show()
    return input('输入验证码： ')


# 动态验证码
code = get_code()
login_data = {
    'username': '13075392893',
    'password': '38238038',
    'verifyCode': code
}
# 提交登录信息
rq = sess.post(url, data=login_data)
# 查看登录结果，如返回登录界面表示登录失败，如返回主页界面表示登录成功
print(rq.url)
