import os
import jieba
import re

path1 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"good.txt"
path2 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"bad.txt"

file1 = open(path1, 'r+', encoding='UTF-8')

good = file1.read()

# 正则去除符号
good = re.sub(
    '[.?,;\"–\“\”\‘\’\n\《\》\（\）\(\)\，\。\？\'\'\：！、【】\[\]\…]', '', good)


goodlist = jieba.lcut(good, cut_all=True)

# strip
#  strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
stopwords = [line.strip() for line in open(
    path1, encoding="UTF-8").read()]

good_count = {}
for word in goodlist:
    if word not in stopwords:
        # 不统计字数为一的词
        if len(word) == 1:
            # continue
            continue
        else:
            # get
            good_count[word] = good_count.get(word, 0) + 1

gooditems = list(good_count.items())
# sort
gooditems.sort(key=lambda x: x[1], reverse=False)
print(gooditems)
