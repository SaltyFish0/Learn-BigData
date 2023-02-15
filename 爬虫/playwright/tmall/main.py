#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""爬取天猫分类列表, 有的页面因为结构不同所以忽略"""

__author__ = 'YKKKKKK'

from playwright.sync_api import sync_playwright, Playwright, Browser
import re
import cookie
import saveData
import HumanVerification

BASE_URL = 'https://www.tmall.com/'


# 页面跳转
def PageGoTo(url: str):
    print(f'当前跳转的网址:{url}')
    PAGE1.goto(url)
    PAGE1.wait_for_load_state('networkidle')
    HumanVerification.SwipeVerification('#nc_1_n1z', PAGE1)
    print('加载完毕')

# 获得分类URL


def getCategoryURL():
    detail_url = {}
    for i in PAGE1.query_selector_all('//html/body/div[1]/div[3]/div[2]/div[1]/div/a'):
        detail_url[i.text_content()] = i.get_attribute('href')
    return detail_url


# 各分类商品数据
def getCategoryData(flag: bool):
    data = []
    if flag:
        try:
            # 等待元素出现, 如果5秒内未出现则略过
            PAGE1.wait_for_selector(
                '//div[@class="product-iWrap"]', timeout=5000)
            item = PAGE1.query_selector_all('//div[@class="product-iWrap"]')
            for i in item:
                data.append({
                    'img_src': 'https:' + i.query_selector('//*[@class="productImg-wrap"]/a/img').get_attribute('src'),
                    'price': i.query_selector('//*[@class="productPrice"]/em').get_attribute('title'),
                    'product_name': i.query_selector('//*[@class="productTitle"]/a').get_attribute('title'),
                    'product_link': 'https:' + i.query_selector('//*[@class="productTitle"]/a').get_attribute('href'),
                    'shop_name': i.query_selector('//a[@class="productShop-name"]').text_content(),
                    'shop_link': 'https:' + i.query_selector('//a[@class="productShop-name"]').get_attribute('href'),
                    # 'product_transaction': i.query_selector('//*[@class="productStatus"]/span[1]').text_content(),
                    # 'comment': i.query_selector('//*[@class="productStatus"]/span[2]').text_content()
                })
        except:
            print('未检测到商品列表')
    else:
        try:
            # 等待元素出现, 如果5秒内未出现则略过
            PAGE1.wait_for_selector('//*[@class="itemLink"]', timeout=50000)
            item = PAGE1.query_selector_all('//div[@class="item"]')
            for i in item:
                data.append({
                    # css行内样式imgSrc
                    'img_src': 'https:' + re.findall("url\('(.*)_\.webp'\)", i.query_selector('//*[@class="itemCover"]').get_attribute('style'))[0],
                    'price': i.query_selector('//*[@class="itemPrice"]/span[2]').text_content(),
                    'product_name': i.query_selector('//*[@class="itemTitle"]').text_content(),
                    'product_link': 'https:' + i.query_selector('//*[@class="itemLink"]').get_attribute('href'),
                    'shop_name': i.query_selector('//*[@class="shopTitle"]').text_content(),
                    'shop_link': 'https:' + i.query_selector('//a[@class="shopTitle"]').get_attribute('href'),
                })
        except:
            print('未检测到商品列表')
    return data


def main():
    cookies = cookie.getCookie()
    with sync_playwright() as playwright:
        browser = run(playwright, 0, False)
        global PAGE1
        PAGE1 = browser.new_context(storage_state=cookies).new_page()
        # 先前往天猫首页
        PageGoTo(BASE_URL)
        # 获取分类URL
        detail_url = getCategoryURL()
        for i in detail_url.items():
            category_name = i[0]
            PageGoTo(i[1])
            # 判断URL是是否为搜索类型网页
            category_data = getCategoryData('search' in i[1])
            saveData.save(category_name, category_data)


def run(p: Playwright, browser_type: int = 0, head: bool = True) -> Browser:
    """
    初始化浏览器
    :param p: Playwright
    :param browser_type: 浏览器类型，0 - webkit, 1 - chromium, 2 - firefox
    :param head: 是否显示浏览器
    :return: browser
    """
    browser_type = [p.webkit, p.chromium, p.firefox][browser_type]
    browser = browser_type.launch(headless=head)
    return browser


if __name__ == '__main__':
    main()
