x1 = x2 = x3 = x4 = x5 = 0
x = input('五位正整数')
x = int(x)
while True:
    if(x > 9999 and x <= 99999):
        break
    else:
        x = input('五位正整数')
        x = int(x)
while (x != 0):
    x5 = x % 10
    x = x//10
    x4 = x % 10
    x = x//10
    x3 = x % 10
    x = x//10
    x2 = x % 10
    x = x//10
    x1 = x % 10
    print('x1+x2+x3+x4+x5=', x1+x2+x3+x4+x5)
else:
    print('Bye-Bye!')
