from playwright.sync_api import sync_playwright
import time

play = sync_playwright().start()
browser_type = play.webkit
browser = browser_type.launch(headless=False)
page = browser.new_page()
BASE_URL = "https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="


def request(Url):
    page.goto(Url)
    page.wait_for_load_state(state='networkidle')


def pageUrl(i):
    return f'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,{i}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='


def getInfo():
    infoList = page.query_selector_all(
        '//div[@class="j_joblist"]/div[@class="e"]')

    elList = [i.query_selector("xpath=a[@class='el']") for i in infoList]
    erList = [i.query_selector("xpath=div[@class='er']") for i in infoList]

    poseList = [i.query_selector('xpath=p/span[@class="jname at"]').inner_text()
                for i in elList]
    moneyList = [i.query_selector('xpath=p[@class="info"]/span[@class="sal"]').inner_text()
                 for i in elList]
    firmList = [i.query_selector(
        'xpath=a[@class="cname at"]').inner_text() for i in erList]

    result = []
    for p, m, f in zip(poseList, moneyList, firmList):
        result.append({
            '岗位': p,
            '薪资': m,
            '公司': f})
    return result


page.goto(pageUrl(1))
page.wait_for_timeout(5000)
print(pageUrl(1))
print(getInfo())


def main():
    for i in range(2, 10):
        request(pageUrl(i))
        print(pageUrl(i))
        print(getInfo())


main()
