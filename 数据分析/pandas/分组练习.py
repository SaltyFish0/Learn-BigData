import pandas as pd
import numpy as np
data = {'Name': ['John', 'Helen', 'Sona', 'Ella'],
        'score': [82, 98, 91, 87],
        'option_course': ['C#', 'Python', 'Java', 'C']}

df = pd.DataFrame(data)
# print(df)
# print()

# groups
# 使用groups查看分组后的数据
# 单个列标签
# print()

# 多个列
# print(df.groupby(['Name', 'score']).groups)


# get_group()
grouped = df.groupby('score')

# 通过 get_group() 方法可以选择组内的具体数据项：
# print(grouped.get_group(91))
# print(grouped.groups)


# 遍历
# for i in grouped:
# print(i)

# 应用单个聚合函数
# print(grouped['score'].agg(np.mean))

# 应用多个聚合函数
# print(grouped['score'].agg([np.mean, np.max, np.size]))


# 组的转换操作
df = pd.DataFrame({'种类': ['水果', '水果', '水果', '蔬菜', '蔬菜', '肉类', '肉类'],
                   '产地': ['朝鲜', '中国', '缅甸', '中国', '菲律宾', '韩国', '中国'],
                   '水果': ['橘子', '苹果', '哈密瓜', '番茄', '椰子', '鱼肉', '牛肉'],
                   '数量': [3, 5, 5, 3, 2, 15, 9],
                   '价格': [2, 5, 12, 3, 4, 18, 20]})
# 分组求均值，水果、蔬菜、肉类
# 对可执行计算的数值列求均值

print(df.groupby('种类').transform(np.mean))
# transform()直接应用demean，实现去均值操作
def demean(arr): return arr-arr.mean()


# print(df.groupby('种类').transform(demean))
# 自定义函数
# 返回分组的前n行数据


def get_rows(df, n):
    # 从1到n行的所有列
    return df.iloc[:n, :]


# 分组后的组名作为行索引
# print(df.groupby('种类').apply(get_rows, n=1))
