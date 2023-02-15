import os
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"myself.txt"
file = open(path, 'w+', encoding='UTF-8')
file.write('学号：18\n专业：程序设计\n爱好:.\n')
fileContent = open(path, 'r+', encoding='UTF-8')
print(fileContent.read())
file.close()
