import re
path1 = r'E:\work area\SaltyFish\Python-a\备赛\文件操控\1.txt'
path2 = r'E:\work area\SaltyFish\Python-a\备赛\文件操控\2.txt'

rule1 = re.compile('\\n')
rule2 = re.compile('[0-9]+')
rule3 = re.compile('[^0-9]+')

data_1 = []
list_id = []
list_name = []

[data_1.append(i) for i in open(path1, 'r+', encoding='UTF-8')]
data_1 = [re.sub(rule1, '', i) for i in data_1]
print(data_1)
data_1.reverse()
print(data_1)
# list_id = [re.findall(rule2, i)[0] for i in data_1]
# list_name = [re.findall(rule3, i)[0] for i in data_1]
#
# result = open(path2, 'w+', encoding='UTF-8')
#
# for i, n in zip(list_id[::-1], list_name[::-1]):
#     line = i + ' ' + n + '\n'
#     result.write(line)