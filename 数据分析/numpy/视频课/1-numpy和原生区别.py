from time import time
from timeit import timeit
import numpy as np
print(np.__version__)
a = [i**2 for i in range(10)]
b = [i**3 for i in range(10)]
ad_sum = []
# 原生相加
for i in range(10):
    ad_sum.append(a[i]+b[i])
print(a)
print(b)
print(ad_sum)

# numpy相加
# arange
a = np.arange(10)**2
b = np.arange(10)**3
print(a+b)
