import pandas as pd


# 查看数据
data = pd.read_csv(
    'E:\work area\SaltyFish\Python-a\备赛\数据分析\data_csv.csv', encoding='gbk')

# 写入数据
# to_csv
# data.to_csv()

# describe()
# 给出行数和列数
# print(data.describe())

# head()
# 查看数据前三行
# print(data.head(3))

# tail()
# 打印数据后三行
# print(data.tail(3))

# loc[]
# 打印第八行
# print(data.loc[8])
# 打印第八行名为phone的列
# print(data.loc[8, 'phone'])
# 打印第五行列名为info_id的数据
# print(data.loc[5]['info_id'])
# 一到四行 （左闭右开 闭代表取值取到那个数，开代表取值取不到那个数。
# print(data.loc[range(1, 5)])

# 更新指定数据
# data.loc[8, 'name'] = '陈海旺'
# print(data.loc[8, 'name'])

# 改变多行的值
# ?????

# 基本判断使用 &and ~not |or
# print(data.head(5))
# print(data.loc[5]['info_id'] != 381)
# print(data['phone'] == 18688880231)
# print((data['phone'] == 18688880231) & (data['name'] == '张大鹏'))

# 基本绘图
# plot()
# matplotlib包可以直接在pandas中使用

# data['number_consumers'].plot()
# print(data['number_consumers'].plot())

# 中级函数
# value_counts
# 统计列中每项出现的次数
# print(data['emp_id'].value_counts())
# print(data['name'].value_counts())

# 在所有的行，列或者全数据上进行操作
# map()
# len() 函数被应用在了「name」列中的每一个元素上
# print(data['name'].map(len))

# apply()
# apply()会给一个列应用一个函数。
# applymap()
# applymap()会给表 (DataFrame) 中的所有单元应用一个函数。
# print(data['name'].apply(lambda x: x))
# print(data.applymap(lambda x: x))

# pandas 中的高级操作
# The SQL 关联
# merge()
# data.merge(data1, on=['name', 'phone', 'emp_id'])

# 分组
# reset_index()
# reset_index() 会将数据重构成一个表。
# print(data.groupby('name')['emp_id'].apply(lambda x: x).reset_index())

# 行迭代
