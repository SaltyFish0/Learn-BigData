# index自动对齐
# s1 = pd.Series([1, 2, 3], index=list("abc"))
# s2 = pd.Series([4, 5, 6], index=list("bcd"))

# print(s1+s2)
from itertools import count
from tokenize import group
import pandas as pd
import numpy as np
import matplotlib as plt

df1 = pd.DataFrame(
    np.arange(24).reshape(3, 8), columns=list("abcdefgh")
)
df2 = pd.DataFrame(
    np.arange(24, 48).reshape(3, 8), columns=list("abcdigkl")
)

# # inner 两个表都有相同的列数据才会合并保留
# # print(pd.concat([df1, df2], join='inner', axis=1, ignore_index=True))
# se1 = df1.apply(lambda x: x[0].astype('str')+"_GG", axis=0)
# se2 = df1.apply(lambda x: x[0].astype('str')+"_MM", axis=0)

# # 合并两个Series成为DataFrame
# # print(pd.concat([se1, se2], axis=1))

# # 合并Series和DataFrame
# # print(pd.concat([df1, se1, se2], axis=1, ignore_index=True))

# print(df1)
# print(se1)


# df1.loc[4] = se1
# print(df1)
# # print(df1.append(df2))
# df2['a'] = [0, 8, 16]
# print(pd.merge(left=df1, right=df2, on="a", how='left'))
# print(pd.merge(left=df1, right=df2, on="a", how='right'))
# print(pd.merge(left=df1, right=df2, on="a", how='outer'))
# print(pd.merge(left=df1, right=df2, on="a", how='inner'))

df1.loc[0, 'a':'c'] = np.nan

# df1.loc[3, :] = [40, 41,  42, 43, 44, 45, 46, 47]


for i in range(3):
    j = i+3
    df1.loc[j, :] = [40, 41,  42, 43, 44, 45, 46, 47]
# print(df1.drop_duplicates())

# print(df1.dropna(axis=0, how='all', subset=['a', 'd']))
for i in range(1):
    j = i+6
    df1.loc[j, :] = [4066, 6666,  4266, 4366, 6666, 4566, 6666, 4766]


def replace(x):
    QU = x.quantile(0.75)  # 上四分位
    QL = x.quantile(0.25)  # 下四分位
    IQR = QU-QL  # 四分位距
    x[(x > QU+1.5*IQR) | (x < QL-1.5*IQR)] = np.nan  # 判断
    return x


# df1 = df1.apply(replace)
df2 = df1.loc[[5, 6], :]


# df3 = df2.stack()
# print(type(df3))
# print(df3.index)
# print(df3)
# print(df1.size)
# print(df1.groupby('a').groups)
# print(df1.groupby('a').get_group(8.0))

# print(list('fbaaaadfaaasaaaaaaaaabndf').count('a'))
# print('fbaaaadfaaasaaaaaaaaabndf'.count('a'))
df3 = df1.append(df2, ignore_index=True)
print(df3)
print(df3.drop_duplicates(keep=False))
