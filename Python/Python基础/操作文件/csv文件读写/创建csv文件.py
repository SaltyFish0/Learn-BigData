import re
import os
import requests
from lxml import etree
import pandas as pd
import numpy as np
Path1 = 'd:\\董老师作业\\董文杰\\'
fpath1 = os.path.exists(Path1)
# 如目录不存在则创建目录
if fpath1 == False:
    os.makedirs(Path1)


# 创建文件


def CreateFile(pages):

    path = Path1 + "第"+pages + "页深圳房价.csv"
    urlname = "https://shenzhen.qfang.com/sale/f"+pages
    file = open(path, 'w+', encoding='gb2312', newline="")
    # 请求
    res = requests.get(urlname)
    # 统一编码集
    res.encoding = res.apparent_encoding
    # 解析文档
    res_elements = etree.HTML(res.text)
    print(res_elements)
    table = res_elements.xpath('//table[@class="rk-table"]')
    # 将列表转换为字符串并指定编码集
    table = etree.tostring(table[0], encoding="utf-8").decode()


CreateFile('1')
