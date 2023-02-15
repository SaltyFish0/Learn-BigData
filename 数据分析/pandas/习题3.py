import pandas as pd
path1 = 'E:/work area/SaltyFish/jupyterNotebook/Pandas-file/meal_order_detail.xlsx'
data = pd.read_excel(path1, sheet_name='meal_order_detail3')


data = data[['order_id', 'dishes_name']]
data_group = data.groupby('order_id')

for i, j in data_group:
    print(i)
    print('*' * 100)
    print(j)
