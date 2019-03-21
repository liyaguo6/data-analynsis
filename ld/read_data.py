# import numpy as np
#
# data = np.loadtxt(("./iris.data.txt"),
#            dtype={
#                'names': ('sepal length', 'sepal width', 'petal length','petal width', 'label'),
#                'formats': ( 'f4',  'f4',  'f4',  'f4', 'S30')},
#                    delimiter=',')
# #
# print(data)
# import pandas as pd
# data = pd.read_table('./iris.data.txt',header=None,encoding='utf-8',sep=',',
#                      names=['sepal length', 'sepal width', 'petal length','petal width', 'label'])
# #
# print(data.describe())

import pandas as pd
data = pd.read_excel('./yinzi.xlsx',header=0,encoding='utf-8',sheet_name='Sheet1',index=False)
#
print(data)
