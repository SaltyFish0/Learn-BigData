import pandas as pd

path = 'E:/x学习资料/python学习资料/pandas-videos-master/data/chipotle.tsv'

data = pd.read_csv(path, sep='\t')

# print(data.head(10))

# 数据中有多少列
# print(data.shape[1])

# 全部列名称
# print(data.columns)

# 索引是怎样的
# print(data.index)

# 被下单数最多商品(item)是什么?
# groupby()
# agg()
# sort_values()
c = data[['item_name', 'quantity']].groupby(
    ['item_name'], as_index=False).agg({'quantity': sum})
c.sort_values(['quantity'], ascending=False, inplace=True)
# print(c.head())

# 在item_name这一列中，一共有多少种商品被下单？
# nunique()
# print(data['item_name'].nunique())

#  在choice_description中，下单次数最多的商品是什么？
# value_counts()
# print(data['choice_description'].value_counts().head())

# 一共有多少商品被下单
# sum()
total_items_orders = data['quantity'].sum()
# print(total_items_orders)

# 将item_price转换为浮点数
# apply()


def dollarizer(x): return float(x[1:-1])


data['item_price'] = data['item_price'].apply(dollarizer)
# print(data['item_price'])

# 在该数据集对应的时期内，收入(revenue)是多少
# round()
data['sub_total'] = round(data['item_price']*data['quantity'], 2)
# print(data['sub_total'])
# print(data['sub_total'].sum())

# 在该数据集对应的时期内，一共有多少订单？
# nunique()
# print(data['order_id'].nunique())

# 每一单(order)对应的平均总价是多少？
# mean()
# print(data[['order_id', 'sub_total']].groupby(by=['order_id']
                                            #   ).agg({'sub_total': 'sum'})['sub_total'].mean())

#  一共有多少种不同的商品被售出？
# nunique()
print(data['item_name'].nunique())