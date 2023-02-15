import requests
proxies = {'http': 'http://120.210.219.74:8080'}
a = requests.get('http://www.tipdm.org', proxies=proxies)
proxies(a)
