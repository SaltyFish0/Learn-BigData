from pyecharts.charts import Bar
from pyecharts.charts import Line

import pandas as pd
import numpy as np
from pyecharts import options as opts

path = r"C:\Users\DELL\Desktop\互联网商务系疫苗学生受种者.xlsx"

data = pd.read_excel(path)
data.dropna(axis=1, inplace=True)

data['院系班级'].replace('互联网商务系', '', regex=True, inplace=True)

currentYear = 2022
data['出生年份'] = [str(i)[0:4] for i in data['出生日期']]
data['年龄'] = [2022 - int(i) for i in data['出生年份']]

x = data['院系班级'].value_counts().index
y = data['院系班级'].value_counts().values

barX_1 = np.hsplit(x, 1)[0].values.tolist()
barY_1 = np.hsplit(y, 1)[0].tolist()
barY_2 = barY_1[::-1]


