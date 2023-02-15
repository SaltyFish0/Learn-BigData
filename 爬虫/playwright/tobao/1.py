from playwright.sync_api import sync_playwright
import time
import HumanVerification

play = sync_playwright().start()
browser_type = play.firefox
browser = browser_type.launch(headless=False)
context = browser.new_context()
page = context.new_page()

LOGIN_URL = 'https://login.taobao.com/'


def request(url):
    page.goto(url)
    page.wait_for_load_state(state="networkidle")
    flag = page.query_selector_all(
        'xpath=html[@data-dpr="1"]')
    if(len(flag) == 1):
        HumanVerification.SwipeVerification('#nc_1_n1z', page)
    time.sleep(3)


request(LOGIN_URL)
page.wait_for_selector('text=我的淘宝')
if(page.title() == '我的淘宝'):
    request('https://www.taobao.com/')

# page.pause()


def getInfo():
    商品列表 = page.query_selector_all('xpath=//div[@data-category="auctions"]')
    商品 = []
    for i in range(len(商品列表)):
        图片链接 = 商品列表[i].query_selector('xpath=//img').get_attribute('src')
        文本信息 = 商品列表[i].query_selector(
            'xpath=//a[@class="J_ClickStat"]').inner_text()
        商品.append({'图片链接': 图片链接, '文本信息': 文本信息})
    return print(商品)


Lists = page.query_selector_all(
    'xpath=//*[@role="menubar"]/li/a[@data-cid="1"]')

Alist = [i.get_attribute("href") for i in Lists]
for i in Alist:
    request(i)

    getInfo()
