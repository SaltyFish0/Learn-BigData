import requests
import json
import pandas as pd
rqq = requests.get('http://www.ptpress.com.cn/bookinfo/getBookListForWS')
data = json.loads(rqq.content.decode('utf-8'))
authors = [i['author'] for i in data['data']]
prices = [i['price'] for i in data['data']]
bookNames = [i['bookName'] for i in data['data']]
# 格式转换
print(pd.DataFrame(({'书名': bookNames, '作者': authors, '价格': prices})))
