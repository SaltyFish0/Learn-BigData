# coding=utf8
# 上述标签定义了本文档的编码，与Python 2.x兼容。

import re
regex = r"<h2.*?>.*?<\/h2>"
test_str = ("<h2 class=\"jjj\" abcde>fghi</h2>\n"
            "<h2 class=\"jjj\" abcde>fghi</h2>")
subst = "我"
# 您可以通过改变第4个参数来手动指定替换的数量
result = re.sub(regex, subst, test_str, 2)
if result:
    print(result)
