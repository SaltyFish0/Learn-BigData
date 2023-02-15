import pandas as pd
import numpy as np

path = r'C:\Users\DELL\Desktop\1_技师程序2101（转段）.xlsx'

data = pd.read_excel(path, header=6)


data.dropna(axis=1, how='all', inplace=True)

columns = ['index', '学号', '姓名', '体育与健康5', '新概念英语2',
           'Vue高级开发', '数据结构基础(Java版)', '大数据导论', '总学分', '总成绩', '平均成绩', '学分绩点', '平均分绩点']


data.columns = columns

# 异常值处理
data1 = data.loc[:, '姓名':'大数据导论'].replace({'0[缺考]': 0})
data1.loc[:, '体育与健康5':'大数据导论'] = data1.loc[:,
                                           '体育与健康5':'大数据导论'].astype('float64')


# 总成绩
data1['sum'] = data1.loc[:, '体育与健康5':'大数据导论'].apply(lambda x: x.sum(), axis=1)


'''
单科成绩最高分,最低分和差值
'''
max = data1.loc[:, '体育与健康5':'大数据导论'].apply(lambda x: x.max(), axis=0)
min = data1.loc[:, '体育与健康5':'大数据导论'].apply(lambda x: x.min(), axis=0)

# print(max)
# for max, min, j in zip(max, min, data.loc[:, '体育与健康5':'大数据导论']):
#     print(j+'最高分是 ' + data1['姓名'][data1.loc[:, j] == max]+f'为{max}分')
#     print(j+'最低分是 ' + data1['姓名'][data1.loc[:, j] == min]+f'为{min}分')
#     print(f'最高分和最低分相差{(max)-(min)}分')
#     print()
new_data1 = data1.set_index('姓名')
new_data2 = data1.set_index('姓名')
print(new_data1.idxmax(axis=0))
print(new_data1.idxmin(axis=0))

print(new_data1.loc[:, '体育与健康5':'大数据导论'].idxmax(axis=1),
      new_data1.loc[:, '体育与健康5':'大数据导论'].max(axis=1))


# # 单个学生最高分，返回学生姓名，最高分科目，最高分分数
# stuMax = data1.loc[:, '体育与健康5':'大数据导论'].max(axis=1)
# for subjects, i in zip(data1.loc[:, '体育与健康5':'大数据导论'].iterrows(), stuMax):
#     # print(i)
#     nes_s = pd.Series(subjects)
#     print(nes_s[nes_s].index)
print(new_data1.info())
print()
print(new_data1.dtypes)
