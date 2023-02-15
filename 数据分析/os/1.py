import os
# print(os)
# print(os.system('E:\\百度翻译\\baidu-translate-client\\百度翻译.exe'))
path1 = os.path.split(os.path.realpath(__file__))[0] + "\\" + "body.txt"


print(os.path.split(os.path.realpath(__file__))[0])

print(os.path.abspath())
