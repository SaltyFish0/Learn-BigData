from itertools import count
import os
import re

path1 = os.path.split(os.path.realpath(__file__))[0] + "\\" + "body.txt"
file1 = open(path1, 'r+', encoding='utf-8')
a1 = file1.read()
h3Rule = re.compile(r'<h3 data-v-7f1a77ef.*>[^*]*?</h3>')
spanRule = re.compile(r'<span data-v-7f1a77ef.*>[^*]*?</span>')
endRule = re.compile(r'left:(.*?)px;\">([^*]*?)</span>')
pxRule = re.compile(r'\d+')
textRule = re.compile(r'[\u4e00-\u9fa5\-（），]')
# 提取h3标签
h3List = h3Rule.findall(a1)
spanList = []
for i in h3List:
    spanList.append(spanRule.findall(i))
# 提取span标签
endList = []
# 长度数组
longList = []
pxList = []  # 偏移度
charList = []  # 文字

for i in spanList:
    longList.append(len(i))
    for j in i:
        pxList.append(pxRule.findall(endRule.findall(j)[0][0]))
        charList.append(textRule.findall(endRule.findall(j)[0][1]))
# 二维转一维
pxList = [i for i in pxList for i in i]
for i in charList:
    if len(i) == 0:
        i.append(" ")

charList = [i for i in charList for i in i]

# 0 4                 4
# 4 4+14              14
# 4+14 4+14+9         9
# 4+14+9 4+14+9+12    12


dict1 = []
pivot = 0
# print(longList, pxList, charList)
for i in range(len(longList)):
    dict1.append({})
    for j in range(longList[i]):
        dict1[i][charList[pivot]] = int(pxList[pivot])
        pivot += 1
        # print(dict1)
for i in dict1:
    str1 = ''
    for k, v in sorted(i.items(), key=lambda a: a[1]):
        str1 += k
    print(str1)
