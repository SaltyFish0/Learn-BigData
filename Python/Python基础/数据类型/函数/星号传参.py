# 下面是自定义函数
# *代表元祖
def count(name, grade, *fraction):
    result = 0
    for item in fraction:
        result += item
    print('name:'+str(name), 'class:'+str(grade), 'sum:'+str(result))
    mean = int(result)/(len(fraction))
    return mean


# 下面是程序主体
count('micle', '4-4', 76, 68, 99, 84)
count('linin', '6-6', 66, 85, 77, 89, 86, 100)
a = count('micle', '4-4', 76, 68, 99, 84)
print(a)
