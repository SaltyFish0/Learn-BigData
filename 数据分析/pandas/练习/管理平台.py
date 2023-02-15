import pandas as pd
import datetime
import numpy as np

path1 = r"E:\work area\SaltyFish\jupyterNotebook\Pandas-file\meal_order_detail.xlsx"

data = pd.read_excel(path1)
# data = data[['order_id', 'counts', 'amounts']].groupby(by='order_id')


#
# print(data.agg('sum', 'max').sort_values(by='amounts'))
#
# 对不同列进行不同操作
# print(data.agg({'counts': ['mean', np.max], 'amounts': 'std'}))


# 支持lambda函数
# print(data.agg({'counts': lambda x: sum(x)**2}))


# pivot_table 分组聚合合二为一？
# 第一个参数分组，idnex指定索引，aggfunc聚合函数
# data = pd.pivot_table(
#     data[['order_id', 'counts', 'amounts']], index='order_id', aggfunc='sum')
# print(data)


# data = pd.pivot_table(
#     data[['order_id', 'dishes_name', 'counts']], index='order_id', columns='dishes_name', aggfunc='sum')
# 或
# data = pd.pivot_table(
#     data[['order_id', 'dishes_name', 'counts']], index='order_id', columns='dishes_name', values='counts', fill_value=0)
# print(data)


# print(pd.crosstab(index=data['order_id'], columns=data['dishes_name']))
# print(pd.crosstab(index=data['order_id'],
#   columns=data['dishes_name'], values=data['counts'], aggfunc='sum').fillna(0))
print(pd.crosstab(index=data['order_id'],
      columns=data['dishes_name']))
