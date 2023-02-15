# 定义一个名为name的函数
def name(first_name, last_name):
    full = first_name+' '+last_name
    return full.title()


while True:
    sur1 = str(input('Enter surname:'))
    print(sur1)
    sur2 = str(input('Enter name:'))
    print(sur2)
    x = name(sur1, sur2)
    print('Full name is: ', x)
    print('1--continue; 2--not')
    y = int(input('Please choice!'))
    if y == 1:
        continue
    else:
        break
print('End')
