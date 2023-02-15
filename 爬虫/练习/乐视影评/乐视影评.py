import requests
from lxml import etree
import os
import time

path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"myself.txt"
file = open(path, 'w+', encoding='UTF-8')

time.sleep(3)
rq = requests.get(
    'http://www.le.com/ptv/vplay/30744694.html?ref=index_focus_1')
html = etree.HTML(rq.content)
# p = html.xpath('//*[@class="cmt-content"]')
# print(p)

p = html.xpath('//*/text()')
print(p)
file.write(str(p))
file.close()
# /html/body/div[4]/div[1]/div[7]/div/div/div[4]/div[1]/dl[1]/dd[3]
