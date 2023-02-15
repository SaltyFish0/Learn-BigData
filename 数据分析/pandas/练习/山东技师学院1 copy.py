import pandas as pd
import datetime
import numpy as np

path1 = r"C:\Users\DELL\Desktop\数字技能学院-三年技师计算机程序设计（转段）2101班-27人.xls"

data = pd.read_excel(path1)
data.dropna(how='all', axis=1, inplace=True)
print(data.columns)


ID = '母亲身份证号'
name = '母亲姓名'

S_Birthdays = [i[6:14] for i in data[ID]]
S_Months = ['2022'+i[10:14] for i in data[ID]]

S_newData3 = pd.DataFrame(
    {name: data[name], '生日': S_Birthdays, '比较月份': S_Months, '固定姓名': data['*姓名']}).set_index(name)


S_nowDate = pd.to_datetime('2022-09-06')


S_newData3['比较天数'] = S_nowDate-pd.to_datetime(S_newData3['生日'])
S_newData3['比较月份'] = pd.to_datetime(S_newData3['比较月份'])-S_nowDate

S_newData3['岁数'] = (S_newData3['比较天数'] / np.timedelta64(1, 'D') /
                    365).astype('str')+'岁'
S_newData3['距离'] = S_newData3['比较月份'] / np.timedelta64(1, 'D')

S_newData3.drop(['比较天数'], inplace=True, axis=1)
S_newData3.drop(['比较月份'], inplace=True, axis=1)



S_newData3['距离'] = S_newData3['距离'].map(lambda x: 365+x if x < 0 else x)


S_newData3['距离'] = S_newData3['距离'].astype('int32')
print(S_newData3.sort_values(by='距离'))
