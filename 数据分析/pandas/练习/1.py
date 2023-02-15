import pandas as pd
import numpy as np
import datetime


path = r'C:\Users\DELL\Desktop\互联网商务系疫苗学生受种者.xlsx'

data = pd.read_excel(path)

S_Birthdays = [i[6:14] for i in data['身份证号']]
S_Months = ['2022'+i[10:14] for i in data['身份证号']]

S_newData3 = pd.DataFrame(
    {'姓名': data['受种者姓名'], '生日': S_Birthdays, '比较月份': S_Months}).set_index('姓名')

# print(S_newData3['生日'])
# print(pd.to_datetime(S_newData3['生日']))
S_newData3['生日'] = pd.Series(S_newData3['生日'], dtype='datetime64')
print(type(S_newData3['生日'][0]))
