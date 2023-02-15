from turtle import clear


code = {'Li pin': 356712, 'Chen yun': 125458, 'Wen ti': 894563,
        'Lin ling': 337682, 'Ru nin': 675446, 'Tang xi': 345890}

# len() 字典长度
# print(len(code))

# print(code.pop('Li pin'))
# a = code.clear()
# print(a)

# 遍历字典
# for i in code:
#     # i为键 通过键取值
#     print(i, " | ", code[i])
# else:
#     print('End')

# iter() 遍历
# for i in iter(code):
#     print('key:   '+i)
#     print('value: '+str(code[i]))
# else:
#     print('End')

# items() 取键和值
# 第一个变量为键
# 第二个变量为值
# for (name, num) in code.items():
#     print('key:   '+name)
#     print('value: '+str(num))
# else:
#     print('End')

# keys() 取键
# for name in code.keys():
#     print('key:   '+name)
# else:
#     print('End')

# values() 取值
# for value in code.values():
#     print('value: '+str(value))
# else:
#     print('End')

# sorted() 排序
# 默认为false，为升序排序
for name in sorted(code.keys()):
    print(name)
else:
    print('End')
# 修改为true，为降序排序
# for name in sorted(code.values(), reverse=True):
#     print(name)
# else:
#     print('End')

# get() 查找字典中是否有指定的值
# print('\n', code.get('Li pin'))
# print('\n', code.get('Zong da hua'))
# if (code.get('Zong da hua')) == None:
#     print('There is no key in the dictionary:'+'Zong da hua')
# print('End')

# 类似方法has_key(),__contains__()有返回true，反之false
# a = code.__contains__('Li pin')
# print(a)

# update() 合并字典
# code1 = {
#     'SaltyFish': 999999999
# }
# code.update(code1)
# print(code)

# popitem() 删除字典中最后一个值,并将该值返回，可使用变量来接收该值
a = code.popitem()
print(code)
print(a)
