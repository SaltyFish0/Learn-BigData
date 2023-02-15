import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

path1 = r"C:\Users\DELL\Desktop\数字技能学院-三年技师计算机程序设计（转段）2101班-27人.xls"

data = pd.read_excel(path1)

S_Birthdays = [i[6:14] for i in data['*证件号码']]
S_Months = ['2022'+i[10:14] for i in data['*证件号码']]


S_newData3 = pd.DataFrame(
    {'姓名': data['*姓名'], '生日': S_Birthdays, '比较月份': S_Months}).set_index('姓名')

S_newData3.loc['杨静波'] = ['20030102', '20220102']


S_nowDate = pd.to_datetime('2022-09-23')
# print(S_newData3.loc['董文杰', '比较月份'])
# print(S_newData3.loc['杨静波', '比较月份'])

S_newData3['比较天数'] = S_nowDate-pd.to_datetime(S_newData3['生日'])
S_newData3['比较月份'] = pd.to_datetime(S_newData3['比较月份'])-S_nowDate

S_newData3['岁数'] = (S_newData3['比较天数'] / np.timedelta64(1, 'D') /
                    365).astype('str')+'岁'
S_newData3['距离'] = S_newData3['比较月份'] / np.timedelta64(1, 'D')

S_newData3.drop(['比较天数'], inplace=True, axis=1)
S_newData3.drop(['比较月份'], inplace=True, axis=1)


S_newData3['距离'] = S_newData3['距离'].map(lambda x: 365+x if x < 0 else x)


S_newData3['距离'] = S_newData3['距离'].astype('int32')
S_newData3['月份'] = [i[4:6] for i in S_newData3['生日']]


month = np.arange(1, 13)
print(S_newData3['距离'].sort_values(ascending=False))

plt.figure(figsize=(20, 10), dpi=100)
plt.plot(month, S_newData3['月份'].value_counts().sort_index(), 'ro--')
plt.show()
