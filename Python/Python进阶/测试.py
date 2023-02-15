import random
dict1 = []
textList = ['最', '美', '的', '情', '诗', '是', '你', '的', '名', '字']
for i in range(0, 10):
    dict1.append({})

for i in dict1:
    for j in range(len(textList)):
        a = random.randint(0, 100)
        i[textList[j]] = a
for i in dict1:
    # print(sorted(i.items(), key=lambda v: v[1]))
    str1 = ''
    for k, v in sorted(i.items(), key=lambda v: v[1]):
        str1 += k+str(v)+" "
    print(str1)
