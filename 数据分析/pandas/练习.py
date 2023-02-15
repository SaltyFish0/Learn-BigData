import pandas as pd
import numpy as np

# 列表创建Series
arr = [i for i in range(0, 5)]
# Series
df = pd.Series(arr)
# print(df)

# 字典创建Series
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
df = pd.Series(dict)
# print(df)

# NumPy数组创建DataFrame
dates = pd.date_range('today', periods=6)  # 定义时间序列作为 index
num_arr = np.random.randn(6, 4)  # 传入 numpy 随机数组
columns = ['A', 'B', 'C', 'D']  # 将列表作为列名
df1 = pd.DataFrame(num_arr, index=dates, columns=columns)
# print(df1)

# 从字典对象data创建DataFrame，设置索引为labels
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)
# print(df)

# 显示DataFrame的基础信息，包括行的数量；列名；每一列值的数量、类型
# print(df.info())
# 方法二
# print(df.describe())

# 展示df的前3行
# print(df[:3])
# print(df.iloc[:3])
# print(df.head(3))

# 取出df的animal和age列
# print(df.loc[:, ['animal', 'age']])
# print()
# print(df[['animal', 'age']])

# 取出索引为[3, 4, 8]行的animal和age列
# print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])

# print(df[df['age'] > 3])
# print(df[df['age'].isnull()])

# 计算visits的总和
# print(df['visits'].sum())

# 计算每个不同种类animal的age的平均数/计算age中相同名称的平均数
# print(df)
# print()
# print(df.groupby('animal')['age'].mean())

# df.loc['k'] = [5.5, 'dog', 'no', 2]
# df = df.drop('k')
# print(df)

# 计算df中每个种类animal的数量
# print(df.iloc[:1].value_counts())

# 按age降序排列 True为升序排序
# print(df.sort_values(by=['age'], ascending=[False]))


# 将priority列中的yes, no替换为布尔值True, False
# df['priority']=df['priority'].map({'yes':True,'no':False})
# print(df)

# 对每种animal的每种不同数量visits，计算平均age，即，返回一个表格，行是aniaml种类，列是visits数量，表格值是行动物种类列访客数量的平均年龄
# print(df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean'))
