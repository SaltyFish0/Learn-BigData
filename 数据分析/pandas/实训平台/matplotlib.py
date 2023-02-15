import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
x = np.arange(1, 11)
y = ['a' + str(i) for i in x]
zero = np.zeros(10)
zero[1] = 0.2
fig = plt.figure()
height = np.random.rand(10)*100
print(zero)

ax1 = fig.add_subplot(1, 1, 1)
plt.pie(height, labels=x, explode=zero, autopct='%0.1f', labeldistance=1.2, pctdistance=0.9, shadow=True, radius=1.2, startangle=90)

plt.show()