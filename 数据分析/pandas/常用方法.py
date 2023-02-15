import numpy as np
import pandas as pd
import os
# read_csv
# parse_dates：指定某些列为时间类型，这个参数一般搭配date_parser使用。
data = pd.read_csv(
    'E:\work area\SaltyFish\Python-a\备赛\数据分析\data_csv.csv', encoding='gbk')
data.head()

# 透视表
# pivot_table
# data_new = pd.pivot_table(data=data, values='name',
#   index='emp_id', columns='info_id')
# print(data_new)

data_new = data.groupby('info_id')['emp_id'].apply(lambda x: x).reset_index()
# print(data_new)


def clear_(x=None):  # 异常值处理
    # quantile
    QL = x.quantile(0.25)
    QU = x.quantile(0.75)
    IQR = QU-QL
    x[((x > QU+1.5*IQR) | (x < QL-1.5*IQR))] = None
    return x


# 异常值处理后
data_new.apply(clear_, axis=0)

# T.agg().T
# 最大值 最小值 均值 中位数 和 方差 偏度 峰度
feature1 = data_new.T.agg(
    ['max', 'min', 'mean', 'median', 'sum', 'var', 'skew', 'kurt'], axis=0).T

# 差分？
# diff()
feature2 = data_new.T.diff(axis=1).agg(
    ['max', 'min', 'mean', 'median', 'sum', 'var', 'skew', 'kurt'], axis=0).T
# print(feature2)

# 5%分位数
# quantile()
feature3 = data_new.quantile(0.05, axis=1)
print(feature3)

# resample()
# apply()
# groupby()
# idxmax()
# pd.concat()
