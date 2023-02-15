import pandas as pd
import datetime
import numpy as np

path1 = r"C:\Users\DELL\Desktop\数字技能学院-三年技师计算机程序设计（转段）2101班-27人.xls"

data = pd.read_excel(path1)
# print(data.info())

# print(data.sort_values(by='*家庭年总收入（元）', ascending=False)
#       [['*姓名', '*家庭年总收入（元）']])

# print(data.sort_values(by='*家庭人均收入（元）', ascending=False)
#       [['*姓名', '*家庭人均收入（元）']])


# print(data['*户口性质'].value_counts())


# for i in data['父亲身份证号']:
#     print(i[6:14])

# newdata = pd.DataFrame()

# FBirthday = [i[6:14] for i in data['父亲身份证号']]
# newData1 = pd.DataFrame({'姓名': data['*姓名'], '生日': FBirthday})
# print(newData1.sort_values(by='生日', ascending=False))

# print()

# MBirthday = [i[6:14] for i in data['母亲身份证号']]
# newData2 = pd.DataFrame({'姓名': data['*姓名'], '生日': MBirthday})
# print(newData2.sort_values(by='生日', ascending=False))


S_Birthdays = [i[6:14] for i in data['母亲身份证号']]
S_Months = ['2022'+i[10:14] for i in data['母亲身份证号']]

S_newData3 = pd.DataFrame(
    {'母亲姓名': data['母亲姓名'], '生日': S_Birthdays, '比较月份': S_Months, '固定姓名': data['*姓名']}).set_index('母亲姓名')


S_nowDate = pd.to_datetime('2022-10-21')


S_newData3['比较天数'] = S_nowDate-pd.to_datetime(S_newData3['生日'])
S_newData3['比较月份'] = pd.to_datetime(S_newData3['比较月份'])-S_nowDate

S_newData3['岁数'] = (S_newData3['比较天数'] / np.timedelta64(1, 'D') /
                    365).astype('str')+'岁'
S_newData3['距离'] = S_newData3['比较月份'] / np.timedelta64(1, 'D')

S_newData3.drop(['比较天数'], inplace=True, axis=1)
S_newData3.drop(['比较月份'], inplace=True, axis=1)

# for i in range(len(S_newData3['距离'])):
#     if S_newData3['距离'][i] < 0:
#         S_newData3['距离'][i] = 365+S_newData3['距离'][i]

S_newData3['距离'] = S_newData3['距离'].map(lambda x: 365+x if x < 0 else x)


S_newData3['距离'] = S_newData3['距离'].astype('int32')
print(S_newData3.sort_values(by='距离'))
