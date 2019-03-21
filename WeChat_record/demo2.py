import jieba
import time
timeStamp= 1544511261
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
def to_hour(t):
    struct_time = time.localtime(t)#将时间戳转换为struct_time元组
    print(struct_time)
    hour = round((struct_time[3] + struct_time[4] / 60))
    return hour

print(to_hour(timeStamp))

# jieba.load_userdict("MyWords")
# sentence = '晚安么么哒亲亲抱抱'
# content= jieba.cut(sentence,cut_all=False)
# print(list(content))

print(','.join(['亲亲','抱抱','晚安']))