import pandas as pd
import numpy as np
import datetime


nowDate = pd.to_datetime('2022-09-06')
birthday = pd.to_datetime('20220922')
print((birthday-nowDate) / np.timedelta64(1, 'D'))
print(365-125)
