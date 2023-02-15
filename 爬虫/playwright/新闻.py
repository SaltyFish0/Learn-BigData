from playwright.sync_api import sync_playwright
import time

play = sync_playwright().start()
play_start = play.chromium
play = play_start.launch(headless=False)
context = play.new_context()
page = context.new_page()

startURL = 'https://spa4.scrape.center/'


def request(URL):
    page.goto(URL)
    page.wait_for_load_state(state='networkidle')

def request1(URL):
    page.goto(URL)
    # page.wait_for_selector(selector='text=原标题')
    page.wait_for_load_state(state='networkidle')


request(startURL)
AllList = page.query_selector_all('//div[@class="el-card__body"]')

Info = []

for i in range(len(AllList)):

    date = AllList[i].query_selector(
        "//span[@data-v-04056655='']").inner_text()

    try:
        img = AllList[i].query_selector("//img").get_attribute('src')
    except:
        img = '空'

    newTitle = AllList[i].query_selector(
        "//a[@class='m-l-sm']").inner_text()

    titleHref = AllList[i].query_selector(
        "//a[@class='m-l-sm']").get_attribute('href')

    Info.append({'date': date,
                 'img': img,
                 'titleHref': titleHref,
                 'newTitle': newTitle
                 })


for i in range(len(Info)):
    request1(Info[i]['titleHref'])
    try:
        oldTitle = page.query_selector(
            '//div[@id="article"]/p[1]').inner_text()
    except:
        oldTitle = '空'

    Info[i]['oldTitle'] = oldTitle.replace('　　原标题：', '')

    print(oldTitle)
    print(Info[i]['titleHref'])
    print()
print(Info)
