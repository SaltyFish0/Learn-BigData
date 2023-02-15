# 下面是自定义函数
def count(name, n1, n2, n3):
    print('score:', n1, n2, n3)
    total = n1+n2+n3
    mean = total/3
    print('total:', total, 'mean:%.2f' % mean)


# 下面是程序主体
number = [78, 99, 65]
count('Tom', *number)
