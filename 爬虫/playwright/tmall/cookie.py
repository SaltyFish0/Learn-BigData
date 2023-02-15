"""
获取cookie
"""
# -*- coding: utf-8 -*-
import json
import os
import sys
from playwright.sync_api import sync_playwright


def __loginAccountPassword(login_page):
    print('使用淘宝用户名和密码登录')
    user_name = input('UserName:')
    password = input('Password:')
    login_page.fill("[id=fm-login-id]", user_name)
    login_page.fill("[id=fm-login-password]", password)
    # login_page.locator("[id=fm-login-id]").fill(user_name)
    # login_page.locator("[id=fm-login-password]").fill(password)
    # ！！！！iframe 滑动验证！！！！
    # iframe = login_page.query_selector('iframe[id=\"baxia-dialog-content\"]').content_frame()
    # slide_button = iframe.locator('//*[@id="nc_1_n1z"]').bounding_box()
    # if login_page.query_selector('.baxia-dialog-content'):
    #     print('nc_1_n1z')
    # ===============================
    login_page.click('.fm-btn')
    login_page.wait_for_selector('text=我的淘宝')


def __loginPhoneSMS(login_page):
    print('使用手机验证码登录')
    phone_code = input('手机号码：')
    login_page.click('.sms-login-tab-item')
    login_page.locator('[id=fm-sms-login-id]').fill(phone_code)
    login_page.click('.send-btn-link')
    sms_code = input('验证码已发送，请查收：')
    login_page.locator('#fm-smscode').fill(sms_code)
    login_page.click('.fm-btn')
    login_page.wait_for_selector('text=我的淘宝')


def __loginPhoneAPP(login_page):
    login_page.click('.icon-qrcode')
    print('打开 淘宝App | 天猫App扫一扫登录, 请在30秒内完成')
    login_page.wait_for_selector('text=我的淘宝')


def getCookie() -> dict:
    """
    获取cookie, 建议使用APP登录.......
    :return: cookie 淘宝用户登录数据
    """
    if not os.path.exists('login_data.json'):

        print('目录不存在cookie，登录淘宝获取')
        print('0 -> 用户名密码登录 | 1 -> 手机验证码登录 | 2 -> 手机APP扫描验证码登录')
        login_code = int(input('选择登陆方式：'))
        if login_code != 0 and login_code != 1 and login_code != 2:
            print('检测输入内容')
            sys.exit(1)

        with sync_playwright() as p:

            login = p.webkit.launch(headless=False)
            context = login.new_context()
            login_page = context.new_page()
            login_page.goto('https://login.taobao.com/')

            if login_code == 0:
                __loginAccountPassword(login_page)
            elif login_code == 1:
                __loginPhoneSMS(login_page)
            elif login_code == 2:
                __loginPhoneAPP(login_page)
            if login_page.title() == '我的淘宝':
                print('登录成功！cookie存储在login_data.json')
                return context.storage_state(path='login_data.json')
            else:
                login_page.screenshot(path='error.png')
                print('登录失败, 请检查截图错误信息')
                sys.exit(1)
    else:
        print('目录存在cookie')
        return json.loads(open('login_data.json', 'r').read())
