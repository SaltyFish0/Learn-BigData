import os
path1 = os.path.split(os.path.realpath(__file__))[0] + "\\" + "words.txt"
file = open(path1, 'r+', encoding='UTF-8')
all_lines = file.readlines()
all_words = []

for line in all_lines:
    all_words.append(line)

all_words.sort()

file = open(path1, 'w+', encoding='UTF-8')
[file.write(i) for i in all_words]
print(len(all_words))
file.close()