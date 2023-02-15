import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 7, 15, 24, 30, 50, 55]

fig = plt.figure()

size2 = [0.1, 0.1, 0.8, 0.8]
size1 = [0.1, 0.8, 0.2, 0.2]
size3 = [0.1, 0.6, 0.2, 0.2]

def createline(flag,size, x, y, labels=[],c='white', **patterns):
    name = fig.add_axes(size)
    name.patch.set_facecolor(c)  # 背景颜色
    if(flag == 1):
        name.plot(x, y, patterns['pattern'])
        name.patch.set_alpha(patterns['transparence'])  # 透明度
    if(flag == 2):
        plt.rcParams['font.sans-serif'] = 'SimHei'
        labels = labels
        name.pie(x, explode=y, labels=labels, autopct='%1.1f%%')
        name.patch.set_alpha(patterns['transparence'])  # 透明度
    if (flag == 3):
        # bar(left, height, width=0.8, bottom=None, **kwargs)
        # 颜色
        # fc 设置全部字体颜色
        # color 一次性设置多个颜色
        # 描边
        # ec 描边颜色;ls 线性;lw 长度
        # 填充样式
        # hatch 填充样式 / , \ , | , - , + , x , o , O , . , *
        # 轴体名称
        # tick_label
        # 堆叠柱状图
        # 并列柱状图
        # 条形图
        # 正负柱状图
        print(patterns['bottom'])
        name.bar(x,height=y,width=patterns['width'],bottom=patterns['bottom'],color=patterns['color'])
    if (flag == 4):
        pass
    print(patterns)


createline(1,size2, x, y,  pattern='ro--', transparence=1)

pieHundred = [33,33,34]
pieType = [0.01, 0.01, 0.01]
pieLabls =['第一产业', '第二产业', '第三产业']
createline(2,size3,pieHundred,pieType,labels=pieLabls,transparence=1)

barColor = ['r', 'g', 'b','r', 'g', 'b','r']
barBottom = [i for i in range(7)]
createline(3,size1,x,y,width=0.6,bottom=barBottom,color=barColor)
# createline(4,list3,x,y)

plt.show()
