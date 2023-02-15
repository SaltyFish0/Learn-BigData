import pandas as pd
import re
path1 = 'E:/work area/SaltyFish/jupyterNotebook/Pandas-file/meal_order_detail.xlsx'
path2 = 'E:/work area/SaltyFish/jupyterNotebook/Pandas-file/meal_order_detail1.xlsx'

data = pd.read_excel(path1, sheet_name='meal_order_detail3')


data.loc[:, 'amounts'] = data['amounts'].astype('str')+'元'

data.loc[:, 'amounts'] = data['amounts'].str.replace("元", "").astype('int32')

data['place_order_time'] = data['place_order_time'].astype('str')


def get_time(x):
    str1 = x.split(' ')
    y, m, d = str1[0].split('-')
    h, s, m = str1[1].split(':')
    return f"{y}年{m}月{d}日 {h}时{s}分{m}秒"


# print(data['place_order_time'].apply(get_time))
