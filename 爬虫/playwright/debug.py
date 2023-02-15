from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")
    # Click text=百度首页设置登录新闻hao123地图贴吧视频 图片网盘更多翻译学术文库百科知道健康营销推广直播音乐查看全部百度产品 >设置登录关闭热搜开启热搜牛年贺岁，登录设
    page.locator(
        "text=百度首页设置登录新闻hao123地图贴吧视频 图片网盘更多翻译学术文库百科知道健康营销推广直播音乐查看全部百度产品 >设置登录关闭热搜开启热搜牛年贺岁，登录设").click()
    # Click input[name="wd"]
    page.fill('input[name=\"wd\"]', '你好').click()
    # Press Enter
    page.locator("input[name=\"wd\"]").press("Enter")
    page.wait_for_url("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%BD%A0%E5%A5%BD&fenlei=256&rsv_pq=9309266e0003a777&rsv_t=84bb8Ydt8uQ5zSRjMYdhWQx%2F9FvG6ZTn27EK2vJERJ0z4Nw8ukGA2IeBM%2Bc&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E4%25BD%25A0%25E5%25A5%25BD&rsp=4&inputT=7145&rsv_sug4=9737&rsv_jmp=fail")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
