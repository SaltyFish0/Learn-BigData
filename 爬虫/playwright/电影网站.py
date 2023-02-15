from playwright.sync_api import sync_playwright


play = sync_playwright().start()
browser_type = play.webkit
browser = browser_type.launch(headless=False)
page = browser.new_page()

BASE_URL = "https://antispider1.scrape.center"


def request(BASE_URL):
    page.goto(BASE_URL)
    page.wait_for_load_state(state="networkidle")


def urlPage(i):
    return f'{BASE_URL}/page/{i}'


def urlSubPage(BASE_URL):
    return [BASE_URL+i.get_attribute('href')
            for i in page.query_selector_all('//a[@class="name"]')]


def getMessage(j):
    return {
        '电影名称': page.locator('//h2[@class="m-b-sm"]').text_content(),
        '出版地址': page.locator('//div[@class="m-v-sm info"][1]/span[1]').text_content(),
        '类型': [i.text_content() for i in page.query_selector_all('//button')],
        '时长': page.locator('//div[@class="m-v-sm info"][1]/span[3]').text_content(),
        '剧情介绍': page.locator('//div[@class="drama"]/p').text_content(),
        '网址': j
    }


for i in range(1, 10):
    request(urlPage(i))
    for j in urlSubPage(BASE_URL):
        request(j)
        print(getMessage(j))
