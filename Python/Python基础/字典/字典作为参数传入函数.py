# # -*- coding:utf-8 -*-


# def name_age(**kwargs):
#     file = {}
#     for key, value in kwargs.items():
#         file[key] = value
#     return file


# a = name_age(zhangsan=12, lisi=13, wangwu=15)
# print(a)


# def gedit_name_age(zhangsan=12, lisi=13, wangwu=15, maliu=16):
#     print("zhangsan's name", zhangsan)
#     print("lisi's name", lisi)
#     print("wangwu's name", wangwu)
#     print("maliu's name", maliu)
#     print('\n')


# # (1)第一种改法
# re_age = {'lisi': '23', 'maliu': 26}
# gedit_name_age(**re_age)

# # (2)第二种改法
# gedit_name_age(lisi=36, maliu=36)

def sf(**dict1):
    for k, v in dict1.items():
        print(k, v)


dict1 = {'咸鱼': 1, 'ykk': 2}
# 传入映射，而不是字典 sf(dict1)
# sf(dict1)

sf(咸鱼=1, ykk=2)
