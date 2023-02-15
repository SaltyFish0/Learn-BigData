# SaltyFish
import os
import re
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"messg.txt"
file = open(path, 'r+', encoding='utf-8')
text = file.read().lower()
text = re.sub('[.?,;\"–\“\”\‘\’\n]', '', text)
# print(type(text))
arr = text.split(' ')
BeforeWord = {}
# print(BeforeWord)
# a = 0
for i in arr:
    count = 0
    for j in arr:
        if(i == j):
            count += 1
    BeforeWord[i] = count
print(BeforeWord)
LaterWord = {k: v for k, v in sorted(
    BeforeWord.items(), key=lambda item: item[1], reverse=True)}
# print(LaterWord)
# for i, j in LaterWord.items():
#     a += 1
#     print('本篇诗词中出现最多的单词是', i, "出现了", j, "次")
#     if(a == 1):
#         break
print('本篇诗词中出现最多的单词是', list(LaterWord.keys())[
      0], "出现了", list(LaterWord.values())[0], "次")
file.close()
