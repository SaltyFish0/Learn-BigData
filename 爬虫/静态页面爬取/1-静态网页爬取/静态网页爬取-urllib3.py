from socket import timeout
import urllib3
http = urllib3.PoolManager()
# 设置请求头
head = {'User-Agent': 'Windows NT 6.1; Win64; x64'}
rq = http.request(
    'GET', url="http://www.tipdm.com/tipdm/index.html", headers=head, timeout=0.4)
print('服务器响应码：', rq.status)
print('响应实体：', rq.data)
