# sync_playwright().start() 初始化？？必须要的一步
# chromium.launch(headless=False) 打开xx浏览器 可设置headless
# new_page() 创建一个新的界面
# title() 显示浏览器标题

# goto() 打开这个网站
# PageGoTo页面导航到此网站

# locator() 定位器
# 定位器代表了一种随时在页面上查找元素的方法。 可以使用 page.locator(selector[, options]) 方法创建定位器

# query_selector_all() 获取元素
# 该方法在页面中查找与指定选择器匹配的所有元素。 如果没有元素匹配选择器，则返回值解析为 [].
# 选择器以// 或者..开头，则会默认为是xpath=selector
# 选择器开始和结束以引号（"或者'），则默认为text=selector
# 其他的默认为是css=selector
# frame_locator() frame定位

# fill() 获取文字并输入文字

# wait_for_timeout() 强制等待，固定的等待时间进行处理
# frame.wait_for_load_state(state,timeout)
# frame.wait_for_selector(selector, timeout)


# set_input_files() 上传文件
# 第一个参数指向类型为的 元素 输入 "file". 可以在数组中传递多个文件。 如果某些文件路径是相对的，则它们相对于当前工作目录进行解析。 空数组清除选定的文件。

# close() 关闭创建的浏览器

# query_selector() 获取文本值/查找文本值
# get_attribute("attribute_name")：获取属性值
# inner_html()：获取html值
# inner_text()：获取内部文本值
