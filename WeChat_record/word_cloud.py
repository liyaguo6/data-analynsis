import matplotlib.pyplot as plt
import re
import numpy as np
import sqlite3
import pandas as pd
from scipy.misc import imread
import jieba
from wordcloud import WordCloud
import jieba.analyse
from wordcloud import ImageColorGenerator
from os import path
import time
jieba.load_userdict("MyWords")
import seaborn as sns
from matplotlib.font_manager import *#如果想在图上显示中文，需导入这个包
# with sqlite3.connect(r'D:\Documents\55ffa04cf64891d73995ff76af01f250\DB\MM.sqlite') as con:
#     df1 = pd.read_sql_query('select * from Chat_94cc46ba8a509971a6fd9d8970731224',con)
# #
# #
# df1.to_csv(path_or_buf='chat.csv',encoding='utf-8')
chat = pd.read_csv('chat.csv', sep=',', usecols=[4,5,6],encoding='utf-8')
# chat.to_csv('SaveMsg.csv')
# print(chat)
all_chat_time = []
all_chat_content = []
li_chat_time = []
gzz_chat_time=[]
li_chat_content=[]
gzz_chat_content=[]
# f = open('lyg.txt','a+',encoding='utf-8')
# h = open('gzz.txt','a+',encoding='utf-8')
w = open('all.txt','a+',encoding='utf-8')

for i in range(len(chat)-1):
    content = chat[i:i+1]
    if len(content['Message'].values[0]) <=30:
        t = content['CreateTime'].values[0]#除以1000用以剔除后三位0
        c = content['Message'].values[0]
        timeArray = time.localtime(t)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        all_chat_content.append(c)
        all_chat_time.append(otherStyleTime)
        w.write('%s\t%s\n'%(otherStyleTime,c))
        # if content['Status'].values[0] == 4:
        #     gzz_chat_time.append(t)
        #     gzz_chat_content.append(c)
        #     # f.write('%s\t%s\n'%(t,c))
        # elif content['Status'].values[0] == 2:
        #     li_chat_time.append(t)
        #     li_chat_content.append(c)
        #     h.write('%s\t%s\n' % (t, c))
# f.close()
# h.close()
# def to_hour(t):
#     struct_time = time.localtime(t)#将时间戳转换为struct_time元组
#     hour = round((struct_time[3] + struct_time[4] / 60))
#     return hour

# hour_set = [to_hour(i) for i in all_chat_time]
# print(hour_set)
#
# myfont = FontProperties(fname=r'C:\Windows\Fonts\MSYH.TTC',size=22)#标题字体样式
# myfont2 = FontProperties(fname=r'C:\Windows\Fonts\MSYH.TTC',size=18)#横纵坐标字体样式
# sns.set_style('darkgrid')#设置图片为深色背景且有网格线
# sns.distplot(hour_set, 24, color='lightcoral')
# plt.xticks(np.arange(0, 25, 1.0), fontsize=15)
# plt.yticks(fontsize=15)
# plt.title('聊天时间分布', fontproperties=myfont)
# plt.xlabel('时间段', fontproperties=myfont2)
# plt.ylabel('聊天时间分布', fontproperties=myfont2)
# fig = plt.gcf()
# fig.set_size_inches(15,8)
# fig.savefig('chat_time.png',dpi=100)
# plt.show()

# import datetime
# print('\n..........\n开始字符统计\n............\n')
# start = datetime.datetime.now()
# pattern_love = '.*?(爱你).*?'
# pattern_memeda = '.*?(么么哒).*?'
# pattern_night = '.*?(晚安).*?'
# pattern_miss = '.*?(想你).*?'
# pattern_kiss = '.*?(亲亲).*?'
# pattern_hug = '.*?(抱抱).*?'
# pattern_ugly = '.*?(嫌弃).*?'
# pattern_set = [pattern_love, pattern_memeda, pattern_night, pattern_miss,pattern_kiss,pattern_hug,pattern_ugly ]
# statistic = [0,0,0,0,0,0,0]
# for i in range(len(all_chat_content)):
#     for j in range(len(pattern_set)):
#         length = len(re.findall(pattern_set[j], str(all_chat_content[i])))
#         statistic[j] += length
# result = {
#         '爱你': statistic[0],
#         '么么哒': statistic[1],
#         '晚安': statistic[2],
#         '想你': statistic[3],
#         '亲亲': statistic[4],
#         '抱抱': statistic[5],
#         '嫌弃': statistic[6],
#
#         }
#
# for key,item in result.items():
#     print('这两个月%s说了%s'%(key,item))
# end = datetime.datetime.now()
# print('\n..........\n字符统计结束,用时: {}\n............\n'.format(end-start))






# def make_stopdict():
#     stopdict = set()
#     f = open("stop_words.txt","r",encoding='utf-8') #网上下载来的停止词文本，近2000个，可以自己往里面添加
#     lines = f.readlines()
#     for l in lines:
#         stopdict.add(l.strip())
#     f.close()
#     return stopdict
# stopdict = make_stopdict()
# #
# #
# def get_clean_content(data):
#     zhongwen_pat = re.compile(r'^[\u4e00-\u9fa5a-zA-Z]+$')
#     all_content = []
#     for t in data: #tweets是从数据库中取出来的待制作词云图的文本源
#         cut_list = [c for c in jieba.cut(t) if zhongwen_pat.search(c)]
#         cut_set = set(cut_list)
#         res_set = cut_set - stopdict
#         res_list = list(res_set)
#         all_content.extend(res_list)
#     return all_content

# print(text)
#
# def get_top_keywords(file): #这里的file即上一步生成的“weibo.txt”
#     top_word_lists = [] # 关键词列表，待填充
#     with open(file,'r',encoding='utf-8') as f:
#         texts = f.read() # 读取整个文件作为一个字符串
#         result = jieba.analyse.textrank(texts,topK=400,withWeight=True) #保留最高频的400个词
#         print(result)
#         for r in result:
#             top_word_lists.append(r[0])
#     return top_word_lists
#
#
#
#
#
# def draw_wordcloud(txt):
#     #读入一个txt文件,基于此文本知错词云图
#     d = path.dirname(__file__) #当前文件文件夹所在目录
#     color_mask = imread("pic.bmp") #读取背景图片，
#     cloud = WordCloud(
#         #设置字体，不指定就会出现乱码，文件名不支持中文
#         font_path=r'C:\Windows\Fonts\simhei.ttf',
#         #font_path=path.join(d,'simsun.ttc'),
#         #设置背景色，默认为黑，可根据需要自定义为颜色
#         background_color='white',
#         #词云形状，
#         mask=color_mask,
#         #允许最大词汇
#         max_words=400,
#         #最大号字体，如果不指定则为图像高度
#         max_font_size=100,
#         #画布宽度和高度，如果设置了msak则不会生效
#         width=600,
#         height = 400,
#         margin = 2,
#         #词语水平摆放的频率，默认为0.9.即竖直摆放的频率为0.1
#         prefer_horizontal = 0.8
#     )
#     wc = cloud.generate(txt) #产生词云
#     #wc = cloud.fit_words(txt) 跟以上是同一意思
#     wc.to_file("pic4.jpg") #保存图片
#     #显示词云图片
#     plt.imshow(wc)
#     #不现实坐标轴
#     plt.axis('off')
#     #绘制词云
#     #plt.figure(dpi = 600)
#     image_colors = ImageColorGenerator(color_mask)
#     #plt.imshow(wc.recolor(color_func=image_colors)) 重新上色，
#     plt.show()
# if __name__ == '__main__':
#     content = get_clean_content(li_chat_content)
#     text = u','.join(content)
#     draw_wordcloud(text)