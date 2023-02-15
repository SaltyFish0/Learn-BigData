from playwright.sync_api import sync_playwright
import os
import json

BASE_URL = 'https://antispider1.scrape.center/'
TOTAL_PAGE = 10

BROWSER_OPTION = {
    'headless': False,  # 有头模式
    # 'proxy': {    # 代理
    #     'server': ''
    # }
}
PLAY = sync_playwright().start()  # 启动同步 playwright
# 0 -> webkit | 1 -> chromium | 2 -> firefox
BROWSER_TYPE = [PLAY.webkit, PLAY.chromium, PLAY.firefox][0]
BROWSER = BROWSER_TYPE.launch(**BROWSER_OPTION)  # launch **BROWSER_OPTION
PAGE = BROWSER.new_page()  # newPage


# 跳转页面并等待网络活动停止
def PageGoTo(path):
    print('当前跳转的URL:', path)
    PAGE.goto(path)
    PAGE.wait_for_load_state(state="networkidle")
    # PAGE.wait_for_selector('.m-b-sm', state='visible')
    print('网络资源加载完毕')


# 获取页面URL
def getPageURL(page_id):
    path = f'{BASE_URL}/page/{page_id}'
    return path


# 获取详情URL
def getDetailURL():
    return [BASE_URL + i.get_attribute('href') for i in PAGE.query_selector_all('//a[@class="name"]')]


# 抓取详情信息
def getDetailInfo():
    info = PAGE.query_selector('//div[contains(@class, "item el-row")]')
    return {
        '电影名称': info.query_selector('h2').text_content(),
        '分数': info.query_selector('.score').text_content(),
        '封面链接': info.query_selector('img').get_attribute('src'),
        '标签': info.query_selector('.categories').text_content().replace(' ', ''),
        '信息': [i.text_content() for i in info.query_selector_all('.info')],
        '剧情简简介': info.query_selector('.drama').text_content()
    }


# 存储数据
def loadsData(data):
    os.makedirs('影视', exist_ok=True)
    path = '影视/' + data['电影名称']
    PAGE.screenshot(path=f'{path}.png')
    with open(f'{path}.txt', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


def main():
    for page_id in range(1, TOTAL_PAGE + 1):
        print(f'======第{page_id}页======')
        PageGoTo(getPageURL(page_id))
        for detail_url in getDetailURL():
            PageGoTo(detail_url)
            data = getDetailInfo()
            print(data)
            loadsData(data)
    PLAY.stop()
    print(f'{BROWSER_TYPE.name}已停止')
    print(f'数据存储到了--{os.getcwd()}\\影视')


if __name__ == '__main__':
    main()

# 键盘 散热器 摆件
