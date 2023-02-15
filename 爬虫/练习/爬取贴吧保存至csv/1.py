import requests
from lxml import etree
import csv
import os
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"贴吧.csv"

rqq = requests.get('https://tieba.baidu.com/p/7440489272')

html = etree.HTML(rqq.content, etree.HTMLParser(encoding='utf-8'))
# /html/body/div[4]/div/div/div[2]/div/div[4]/div[1]/div[3]/div[1]/div[2]/ul/li[3]/a
names = html.xpath('/html/body//ul/li[@class="d_name"]/a/text()')
# print(names)

# /html/body/div[4]/div/div/div[2]/div/div[4]/div[1]/div[3]/div[1]/div[3]/div[1]/cc
content = html.xpath('/html/body//cc/div[@style="display:;"]/text()')
# print(content)


file = open(path, 'w+', encoding='gb2312', newline="")
csv_writer = csv.writer(file)
for i, j in zip(names, content):
    csv_writer.writerow([i, j])
