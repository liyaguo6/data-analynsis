import pandas as  pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
def type_converters(s):
    it = {'医疗': 0, '其它': 1}
    return it[s]

df = pd.read_csv(r'C:\Users\10755\Desktop\test215.csv',header=0 \
                 ,encoding='gbk',converters={3:type_converters},index_col='index',usecols=['answer','classes','index','value'],error_bad_lines=True).dropna()

# print(df.head())
# x_train, x_test, y_train, y_test = train_test_split(df.iloc[:,:1], df.iloc[:,1:2], test_size=0.3, random_state=1)
# print(x_train)
# print(y_train)
ss = StandardScaler()
x = ss.fit_transform(df['value'].values.reshape(-1,1).astype('float64'))
print(x)