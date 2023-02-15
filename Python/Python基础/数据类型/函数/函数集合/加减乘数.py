# 定义4个函数
def add(x, y):
    print('Adding %d + %d' % (x, y))
    return x+y


def sub(x, y):
    print('Subtract %d - %d' % (x, y))
    return x-y


def mult(x, y):
    print('Multiply %d * %d' % (x, y))
    return x*y


def div(x, y):
    print('Divide %d / %d' % (x, y))
    return x/y
# 程序主体为：


numA = int(input('Enter first integer:'))
numB = int(input('Enter second integer:'))
print('1--addition', end=' ')
print('2--subtraction')
print('3--multiplication', end=' ')
print('4--division')
i = int(input('What do you want to do?'))
if i == 1:
    result = add(numA, numB)
elif i == 2:
    result = sub(numA, numB)
elif i == 3:
    result = mult(numA, numB)
elif i == 4:
    result = div(numA, numB)
print('The calculation result is =', result)
print('End')
