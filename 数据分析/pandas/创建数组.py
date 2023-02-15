import pandas as pd
import numpy as np


dataList, list2 = [], []
for i in range(1, 82):
    list2.append(i)
    if(i % 9 == 0):
        dataList.append(list2)
        list2 = []

line = ['r'+str(i+1) for i in range(len(dataList))]
column = ['l'+str(i+1) for i in range(len(dataList))]

pList = pd.DataFrame(dataList, index=line, columns=column)

pList.loc[:, 'l10'] = None
pList.loc['r10'] = None

# print(pList['l1'].mean())
# print(pList['l1'].sum())
# print(pList['l1'].nunique())

# print(pList['l1'].agg(['sum', 'mean', 'nunique']))

# print(pList.agg({'l1': ['sum', 'mean', 'nunique'],
#       'l2': ['sum', 'mean', 'nunique']}))

# print(pList['l2'])
# print(pList['l2'].diff())

# print(pList.loc[:, 'l1'])
# try:
#     print(pList.loc[:, 'l1'].diff())
# except:
#     print()

# print(pList)
# print(pList.quantile(axis=1))

pList1 = pList
# 啊 = pd.concat([pList, pList1])

# print(啊)
啊 = pd.concat([pList, pList1], ignore_index=True, axis=1)
print(啊)
