import os
Path1 = 'd:\\董老师作业\\董文杰\\'
#  os.path.exists() 判断目录是否存在
fpath1 = os.path.exists(Path1)
print(fpath1)
# 如目录不存在则创建目录
if fpath1 == False:
    # os.makedirs() 创建目录
    os.makedirs(Path1)

# os.path.split(os.path.realpath(__file__))[0] 当前目录
path1 = os.path.split(os.path.realpath(__file__))[0] + "\\" + "message.txt"

# open() 操控文件
file = open(path1, 'w+', encoding='UTF-8')
file.write()

fileContent = open(path1, 'r+', encoding='UTF-8')
# read()读取
print(fileContent.read())
fileContent.close()
file.close()
