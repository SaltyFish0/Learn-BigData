from playwright.sync_api import sync_playwright
import time
play = sync_playwright().start()
browserList = [play.webkit, play.chromium, play.firefox]

browser_type = browserList[2]
browser = browser_type.launch(headless=False)
page = browser.new_page()

bas_url = r'https://www.mi.com/shop/search?keyword=%E6%BF%80%E5%85%89%E6%8A%95%E5%BD%B1'


def request(url):
    page.goto(url)
    page.wait_for_load_state(state='networkidle')


request(bas_url)
flag = page.query_selector_all('//div[@class="mi-pagenav"]')
if len(flag) == 1:
    numFlag = page.query_selector('//div[@class="mi-pagenav"]/a[last()-2]').inner_text()
    for i in range(int(numFlag)):
        rightbtn = page.query_selector('//div[@class="mi-pagenav"]/a[last()]')
        print(i)
        rightbtn.click()
        page.wait_for_timeout(1000)

        titleList = page.query_selector_all('//h2[@class="title"]')
        titleList = [i.inner_text() for i in titleList]
        print(titleList)
else:
    print(2)
