from itertools import count
import os
import re
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"w.txt"
file = open(path, 'r+', encoding='utf-8')
text = file.read().lower()
text = re.sub('[.?,;\"–\“\”\‘\’\n]', '', text)
# print(text)
arr = text.split(' ')
print(type(arr))
pattern = re.compile('[a-z]+')
arr1 = []
for i in arr:
    i = pattern.findall(i)
    print(str(i))
    arr1.append(str(i))

# print(arr1)
# print(type(arr1))


word_dict = {}
for i in arr1:
    count = 0
    # print(i)
    for j in arr1:
        if(i == j):
            count += 1
    word_dict[i] = count
print(word_dict)
word_dict = {k: v for k, v in sorted(
    word_dict.items(), key=lambda item: item[1], reverse=True)}
print(word_dict)
