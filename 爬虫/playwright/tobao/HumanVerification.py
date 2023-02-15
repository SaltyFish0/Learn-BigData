"""
各种验证方式。。。
"""


def SwipeVerification(selector, play_w_page):
    """
    滑动验证, 用于处理天猫反爬


    参数说明：
        selector -> 选择器，请输入需要移动的按钮元素
        play_w_page -> 页面
    """

    if play_w_page.query_selector(selector):
        print('检测到滑动验证')
        slide_btn = play_w_page.locator(selector)
        btn_box = slide_btn.bounding_box()
        # 中心点位置 x=x+width/2 y=y+height/2
        x = btn_box['x'] + btn_box['width'] / 2  # x轴中心点
        y = btn_box['y'] + btn_box['height'] / 2  # y轴中心点
        move_x = x + 300  # x轴移动位置
        # 鼠标移动到中心点
        play_w_page.mouse.move(x, y)
        # 按下鼠标
        play_w_page.mouse.down()
        # 拖动到指定位置
        play_w_page.mouse.move(move_x, y)
        # 释放鼠标
        play_w_page.mouse.up()
        print('滑动完成')
