# SaltyFish
import jieba
import os
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"text.txt"
txt = open(path, "r", encoding='utf-8').read()
words = jieba.lcut(txt)


print(type(words))


# counts = {}

# for word in words:
#     if len(word) == 1:
#         print(len(word))
#         continue
#     else:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(len(counts)):
#     word, count = items[i]
#     # print("{0:<5}{1:>5}".format(word, count))
