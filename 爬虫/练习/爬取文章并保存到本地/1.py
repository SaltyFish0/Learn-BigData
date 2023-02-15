import requests
from lxml import etree
import os
import re
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"sss.txt"
file = open(path, 'w+', encoding='utf-8')

rqq = requests.get('https://www.51test.net/show/10059145.html')
html = etree.HTML(rqq.content)
p = html.xpath('/html/body//p/text()')

pattern = re.compile('(从我们.*发挥出自己的能力。)')
result = pattern.findall(str(p))

regex = r"\', \'\\\\u3000\\\\u3000"
result = re.sub(regex, '\n', str(result))
file.write(str(result))
file.close()
