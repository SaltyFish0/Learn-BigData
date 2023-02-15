import copy

list1 = ['Author', 'age', 'sex']
list2 = ['Python当打之年', [18, 99], '男']


dic1 = dict(zip(list1, list2))
dic2 = dic1
dic3 = dic1.copy()
dic4 = copy.deepcopy(dic1)

dic1['age'].remove(18)
dic1['age'] = 20


print('原字典', dic1)
print('赋值字典', dic2)
print('浅拷贝', dic3)  # dic1和dic3是两个独立的对象，但他们的子对象还是指向统一对象
print('深拷贝', dic4)  # 深拷贝完全独立
