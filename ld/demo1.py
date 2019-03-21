import re
import pandas as pd

raw_data=[]
clear_data=[]
def read_data(path):
    """
    note：这里主要是把原始数据家人到原始样本中，在读取数据中发现一个样本不一定在一行，所以这里利用了一下字符串拼接的知识
    :param path:
    :return:
    """
    with open(path,'r',encoding='gbk') as f:
        current_data=""
        for line in f.readlines():
            if re.match('[[|"]',line):
                raw_data.append(line.replace("\n",''))
                current_data=line.replace("\n",'')
            else:
                current_data+=line.replace("\n",'')
                raw_data.pop()
                raw_data.append(current_data)
    return raw_data

def get_name(data_dict):
    for key,val in data_dict.items():
        if re.match('^\[费用',val):
            print(val)
            ret=re.search("\s(?P<name>.{2,3}\s|.*)申請(?P<type>.*)共(?P<symbol>\w{3})(?P<cash>\d+\.\d+|\d+)",val)  #这个是重点，研究了很长时间，属于正则的分组匹配
            print(ret.groups())
        if re.match('^\"\[付款申请|\[付款申请',val):
            pass
        if re.match('^\[预算/采购|\"\[预算/采购', val):
            pass


if __name__ == '__main__':
    path='./shuju_cn.txt'
    data=read_data(path)
    raw_id_data_dict={}
    make_id=list(map(lambda x, y: raw_id_data_dict.update({x: y}), range(len(data)), data))  #把原始列表数据转化为带编号的字典格式
    # print(raw_data_dict)
    get_name(raw_id_data_dict)