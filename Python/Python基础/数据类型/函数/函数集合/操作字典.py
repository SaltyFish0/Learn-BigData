# 下面是定义的函数
def person(first_name, last_name):
    per = {'first': first_name, 'last': last_name}  # 把传递过来的参数封装成一个字典
    return per  # 把字典返回给调用者


# 下面是编写的程序
while True:
    f_name = str(input('Tell me your first_name:'))  # 输入第1个参数
    l_name = str(input('Tell me your last_name:'))  # 输入第2个参数
    result = person(f_name, l_name)  # 调用函数person()，把字典返回给变量result
    print(result)
    print('Your full name is:', end=' ')
    for val in result.values():  # 通过循环，组装成全名
        print(val.title(), end=' ')
    print('\n')
    x = str(input("1--quit ;other--continue!"))
    if x == '1':
        print('Bye-bye!')
        break
