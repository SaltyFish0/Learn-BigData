lyric = "There is no fate but what we make for ourselves  for for."
lyric = lyric.lower()  # 将所有字母转换为小写形式
words = lyric.split()  # 将字符串拆分成单词
word_freq = {}  # 统计词频列表
for word in words:
    if word in word_freq.keys():  # 判定值是否已存在
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)
