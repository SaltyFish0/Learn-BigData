import os
import re
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"Walden.txt"
f = open(path, mode='r')  # 读取文本文件
txt = f.read()


lyric = txt.lower()
lyric_new = re.sub('[，,:\"“”\'-?？.;《》&]', "", lyric)  # 去除多余的符号
words = lyric_new.split()
word_freq = {}

# for word in words:
#     if(word in word_freq.keys()):
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1

for word in words:
    if(word not in word_freq.keys()):
        word_freq[word] = 1
    else:
        word_freq[word] += 1
# print(word_freq)

# 排序
# print(word_freq.items())
result = sorted(word_freq.items(), key=lambda x: x[1], reverse=False)


print(result)

f.close()
