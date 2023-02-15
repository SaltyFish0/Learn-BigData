import pandas as pd
import re
path1 = 'E:/work area/SaltyFish/jupyterNotebook/Pandas-file/meal_order_detail.xlsx'
path2 = 'E:/work area/SaltyFish/jupyterNotebook/Pandas-file/meal_order_detail1.xlsx'

data = pd.read_excel(path1, sheet_name='meal_order_detail3')


total_row = data.shape[0]
user_names = ['a' + str(i+1) for i in range(6)]


print('总份数', total_row)
print('人数', user_names)
mealPep = total_row // len(user_names)
print('每人做多少份', mealPep)

if(total_row % len(user_names) != 0):
    mealPep += 1
print('每人做多少份后', mealPep)

# enumerate
df_subs = []
for idx, user_name in enumerate(user_names):
    begin = idx*mealPep
    end = begin+mealPep

    df_sub = data.iloc[begin:end]
    df_subs.append((idx, user_name, df_sub))
    print(idx, user_name, df_sub)


for idx, user_name, df_sub in df_subs:
    file_name = f"{idx}-{user_name}.xlsx"
    df_sub.to_excel(file_name, index=False)
