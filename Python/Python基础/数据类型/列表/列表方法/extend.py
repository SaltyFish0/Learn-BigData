month = ['January', 'February', 'March', 'April', 'May', 'June', 'July']  # 原列表
others = ['August', 'September', 'October', 'November', 'December']  # 新列表
month.extend(others)  # 调用方法extend()
i = 1  # 控制一行输出7个列表元素
for x in month:
    print(x+'  ', end=' |')
    i += 1
    if i == 7:
        i = 1
        print('\n')
    else:
        continue
print('\nEnd')
