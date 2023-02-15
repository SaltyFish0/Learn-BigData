# value = 8/0
# print(value)
# 为了不影响接下来代码的运行，需要异常捕获
# try:
#     # 把有可能发生异常的代码放在try后面
#     # 如可以正常运行则执行try下代码，反之运行except下代码
#     value = 8/0
#     print(value)
# except:
#     print('error')


# try:
#     value = 8/4
#     print(value)
# except:
#     print('error')
# else:
#     如果尝试运行的代码没出错，则同时执行try和else下的代码,反之则执行except下的代码
#     print('no error')


# try:
#     value = 8/4
#     print(value)
# except:
#     print('error')
# else:
#     print('no error')
# finally:
#     # 不管出没出错都会运行finally下的代码
#     print('finally')

# try:
#     value = 8/b
#     # 如要捕获特殊类型异常，则需指定异常类型
#     # 如异常类型与指定类型不符，则依然会报错
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#     # 可以同时指定多个异常类型
# except NameError:
#     print('NameError')

import traceback
# 使用python自带库traceback 记录异常
try:
    value = 8/b
except:
    # traceback.format_exc()
    # 程序会正常运行，打印的是字符串
    info = traceback.format_exc()
    print(info)
    print(type(info))
print(1)
