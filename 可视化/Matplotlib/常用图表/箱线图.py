import numpy as np
import matplotlib.pyplot as plt
data = np.load('Matplotlib-file/国民经济核算季度数据.npz', allow_pickle=True)
columns = data['columns']
values = data['values']
# 绘制箱线图
plt.figure(figsize=(6, 6))
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False

labels = ['第一产业', '第二产业', '第三产业']
plt.boxplot(values[:, 3], notch=True)
plt.show()
