import numpy as np
import matplotlib.pylab as plt
x = np.arange(0, 1, 0.1)
print(x)
plt.figure()  # 1-创建画布
# 2-绘制图形；设置信息
plt.xlim(0, 1)  # 设置x和y的取值区间
plt.ylim(0, 1)
plt.title("title")
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, x**2)
plt.plot(x, x**4)
plt.legend(['y=x^2', 'y=x^4'])
# 显示之前保存文件
plt.savefig('Matplotlib-file//s.jpg')
plt.show()  # 3-显示图形
