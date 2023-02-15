# 增加多行或者多列

import numpy as np
import pandas as pd

# 增加多行
# 方法一：使用df.reindex
df = pd.DataFrame(np.random.rand(
    4, 5), columns=list('abcde'), index=list('hijk'))
new_index = df.index.tolist() + list(range(4, 8))
df = df.reindex(new_index)
print('\n增加多行：\n', df)
