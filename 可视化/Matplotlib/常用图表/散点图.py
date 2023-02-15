import numpy as np
import matplotlib
import matplotlib.pyplot as plt
data = np.load('Matplotlib-file/国民经济核算季度数据.npz', allow_pickle=True)
columns = data['columns']
values = data['values']

# 绘制散点图
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']  # 设置默认字体为楷体，不然会报错
plt.figure(figsize=(8, 6))  # 尺寸
plt.scatter(values[:, 1], values[:, 3], marker="o")  # 散点图数据集1
plt.scatter(values[:, 1], values[:, 4], marker="*")  # 散点图数据集2
plt.scatter(values[:, 1], values[:, 5], marker="D")  # 散点图数据集3


plt.xticks(values[range(0, 70, 4), 1], values[range(
    0, 70, 4), 1], rotation=45)  # 设置x轴刻度，字体旋转
plt.legend(['第一产业生产总值', '第二产业生产总值', '第三产业生产总值'])  # 图例
plt.title("2000-2017年各产业生产总值散点图")  # 标题
plt.ylabel("产生产总值（亿元）")  # y轴信息
plt.savefig('Matplotlib-file/2000-2017年各产业生产总值散点图.jpg')
plt.show()
