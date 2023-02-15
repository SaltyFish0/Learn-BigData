import os
import jieba
import re

path1 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"good.txt"
path2 = os.path.split(os.path.realpath(__file__))[0] + "\\"+"bad.txt"

file1 = open(path1, 'r+', encoding='UTF-8')
file2 = open(path2, 'r+', encoding='UTF-8')

good = file1.read()
bad = file2.read()

# 正则去除符号
good = re.sub(
    '[.?,;\"–\“\”\‘\’\n\《\》\（\）\(\)\，\。\？\'\'\：！、【】\[\]\…]', '', good)
bad = re.sub(
    '[.?,;\"–\“\”\‘\’\n\《\》\（\）\(\)\，\。\？\'\'\：！、【】\[\]\…]', '', bad)


goodlist = jieba.lcut(good, cut_all=True)
badlist = jieba.lcut(bad, cut_all=True)
print(goodlist)
print(badlist)

stopwords = [line.strip() for line in open(
    file1, encoding="UTF-8").read()]

good_count = {}
for word in goodlist:
    good_count[word] = good_count.get(word, 0) + 1
gooditems = list(good_count.items())
gooditems.sort(key=lambda x: x[1], reverse=True)
print(gooditems)
