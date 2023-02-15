import re
names = '关羽; 张飞, 赵云,马超, 黄忠  李逵'
namelist = re.split(r'[;,，\s]\s*', names)
print(namelist)
