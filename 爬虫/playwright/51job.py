from playwright.sync_api import sync_playwright
from lxml import etree
import time

play = sync_playwright().start()
browser_type = play.webkit
browser = browser_type.launch(headless=False)
page = browser.new_page()
BASE_URL = "https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="

# //span[@class="jname at"]


def request(Url):
    page.goto(Url)
    page.wait_for_load_state(state='networkidle')


def pageUrl(i):
    return f'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,{i}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='


def getInfo():
    html = page.content()
    html = etree.HTML(html, parser=etree.HTMLParser(encoding='utf-8'))
    infoList = html.xpath('//div[@class="j_joblist"]/div[@class="e"]')

    elList = [i.xpath("a[@class='el']")[0] for i in infoList]
    erList = [i.xpath("div[@class='er']")[0] for i in infoList]

    岗位 = [i.xpath('p/span[@class="jname at"]/text()')[0] for i in elList]
    薪资 = [i.xpath('p[@class="info"]/span[@class="sal"]/text()')[0]
          for i in elList]

    公司 = [i.xpath('a[@class="cname at"]/text()')[0] for i in erList]

    result = []

    for a, b, c in zip(岗位, 薪资, 公司):
        result.append({
            '岗位': a,
            '薪资': b,
            '公司': c,
        })
    return result


page.goto(pageUrl(1))
time.sleep(5)
print(pageUrl(1))
print(getInfo())

for i in range(2, 10):
    request(pageUrl(i))
    print(pageUrl(i))
    print(getInfo())
