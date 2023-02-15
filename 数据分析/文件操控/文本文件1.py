import re

path1 = r'E:\work area\SaltyFish\Python-a\备赛\文件操控\1.txt'
path2 = r'E:\work area\SaltyFish\Python-a\备赛\文件操控\2.txt'

rule1 = re.compile('\\n')
rule2 = re.compile('[0-9]{1,3}')
rule3 = re.compile('[0-9]{1,3}(.*)')

data_1 = []
list_id = []
list_name = []
result = {}

[data_1.append(i) for i in open(path1, 'r+', encoding='UTF-8')]

data_1 = [re.sub(rule1, '', i) for i in data_1]
list_id = [re.findall(rule2, i)[0] for i in data_1]
list_name = [re.findall(rule3, i)[0] for i in data_1]

for i, n in zip(list_id, list_name):
    result[int(i)] = n

result = sorted(result.items(), reverse=False)

file = open(path2, 'w+', encoding='utf-8')
for i in range(len(result)):
    file.write(str(result[i][0]) + ' ' + result[i][1] + '\n')
'''
1.txt
前面是序号 后面是对应的电影。现在序号顺序是打乱的，要求将顺序调整为降序排序，并格式化。 
'''