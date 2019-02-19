import pandas as pd
import datetime
import numpy as np

# time = datetime.datetime.now()
time_arry = pd.Series(['2018-06-23 23:12:45','2019-05-24 20:13:05'])
print(time_arry)
temp = pd.DatetimeIndex(time_arry)
df=pd.DataFrame({'date':temp.date,'time':temp.time})
# print(temp.date)
# print(temp.time)
print(df)
# data = pd.to_datetime(temp.time, format="%H:%M:%S")
# print(data)