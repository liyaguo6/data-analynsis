import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#### 数据离散化####
# np.random.seed(0)
# arr=np.random.rand(200)
# arr1 = pd.DataFrame(arr,columns=['sd'])

# factor = pd.cut(arr,4)
# dist = pd.value_counts(factor)
# one_hot=pd.get_dummies(factor)
# print(pd.concat([arr1,one_hot],axis=1))
# val = list(arr)
# print(val)
# plt.hist(val,index,histtype='bar', rwidth=0.8)
# plt.legend()
# plt.show()


####数据统计描述####

# data = pd.Series(np.random.randn(500))
# data=data.describe(percentiles=[0.3,0.6,0.9])

####时间数据处理#####
from datetime import datetime
day_of_week = lambda x:datetime.strptime(x,"%Y-%m-%d %H:%M:%S").weekday()

print(day_of_week('2019-2-6 21:14:35'))

