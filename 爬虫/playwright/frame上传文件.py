from playwright.sync_api import sync_playwright
BROWSER_OPTION = {
    'headless': False,  # 有头模式
    # 'proxy': {    # 代理
    #     'server': ''
    # }
}
PLAY = sync_playwright().start()
BROWSER_TYPE = [PLAY.webkit, PLAY.chromium, PLAY.firefox][0]
BROWSER = BROWSER_TYPE.launch(**BROWSER_OPTION)
PAGE = BROWSER.new_page()

PAGE.goto('http://testingedu.com.cn:8000/Home/user/login.html')
PAGE.fill('//input[@id="username"]', '13800138006')
PAGE.fill('//input[@id="password"]', '123456')
PAGE.fill('//input[@id="verify_code"]', '1111')
PAGE.click('//a[@class="J-login-submit"]')
PAGE.wait_for_timeout(3000)

PAGE.goto('http://testingedu.com.cn:8000/Home/User/info.html')
PAGE.click('//img[@id="preview"]')
PAGE.wait_for_timeout(1000)

PAGE.frame_locator('//*[@id="layui-layer-iframe1"]').\
    locator('//*[@id="filePicker"]/div[2]/input').\
    set_input_files(r'C:/Users/DELL/Desktop/PS/QQ图片20220420113352.jpg')
PAGE.wait_for_timeout(3000)
PAGE.frame_locator('//*[@id="layui-layer-iframe1"]').\
    locator('//div[@class="saveBtn"]').click()

PAGE.click('//*[@class="save"]')
PAGE.wait_for_timeout(3000)
PAGE.close()
