import pandas as pd
import numpy as np
import re
path = r'./data1.csv'
df1 = pd.read_csv(path,low_memory=False,encoding='gbk',index_col='行')
# print(df1.iloc[:,[2,3]])  #通过位置获取
# print(df1.loc[0:5,['问题','病情分析/意见']]) #通过标签获取
# print(df1[0:5][['问题','病情分析/意见']]) #通过标签获取
iters=df1[['问题','病情分析/意见']].dropna()
# data=np.array(iters.loc[:,['问题','病情分析/意见']].values)
# print(data.shape)

# print(iters)
# print(iters[:100])

def sub1(str):
    pattern1 = re.compile(
        '(\u3000|\u30005|\u30001|\u30002\u30003|\u30004)|(朋友|您好|你好|谢谢)(。|、|\？|,|，|\?|：|:|！|!|;|；)|^[^\u4e00-\u9fff]{1,}|(朋友|您好|你好|谢谢)|(病情分析|指导意见|心理分析)(。|、|\？|,|，|\?|：|:|！|!|;|；)')
    return  re.sub(pattern1,'',str)





def sub2(str):
    pattern2 = re.compile('。{2,}')
    return  re.sub(pattern2,"。",str)



# print(ret2)
def clean_data(iters):
    ret1 = list(map(sub1, iters))
    ret2 = list(map(sub2,ret1))
    return ret2


# print(iters)
# print(clean_data(iters['问题']))
# print(clean_data(iters['病情分析/意见']))

data_list=[]
l=[]
def get_data_list(data):
    q_data=clean_data(data['问题'])
    a_data=clean_data(data['病情分析/意见'])
    for i in range(len(q_data)):
        if q_data[i] not in l:
            data_list.append([q_data[i],a_data[i]])
            l.append(q_data[i])
# #
    return data_list
#

def load_json_file(file,result):
    data_dict = dict(conversations=result)
    with open(file, 'w') as f:
        import json
        f.write(json.dumps(data_dict))


# def clean_data_list():
#     pass
if __name__ == '__main__':
    result = get_data_list(iters)
    file='test.json'
    load_json_file(file, result)
