from unittest import result
import pandas as pd
path = 'E:/x学习资料/python学习资料/pandas-videos-master/data/drinks.csv'


data = pd.read_csv(path)

data = pd.DataFrame(data)
# print(data)
# 国家 啤酒 精神 葡萄酒 总升纯酒精 洲
result1 = data.groupby('continent').wine_servings.describe()
# print(result1)

# result2 = data.groupby('continent').agg(
#     ['sum', 'mean', 'quantile', 'max', 'min'])

# result2 = data.groupby('continent').spirit_servings.agg(
# ['sum', 'mean', 'quantile', 'max', 'min'])

result2 = data.groupby('continent').mean()

print(result2)
