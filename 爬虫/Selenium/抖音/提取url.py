import re
beforeUrl = '2.38 ZMJ:/ 平淡的日子里也泛着光捏%%生活碎片%%记得开心  https://v.douyin.com/YaHMt4G/ 复制此链接，打开Dou音搜索，直接观看视频！'
pattern = re.compile('https.*/')
result = pattern.findall(beforeUrl)
print(result[0])
