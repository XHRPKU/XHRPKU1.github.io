# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:25:11 2023

@author: 傲娇的淡定着
"""
#引入需要的库
from pyecharts import options as opts
from pyecharts.charts import WordCloud,Bar,Page
from pyecharts.globals import SymbolType
import csv


#打开上一代码统计出的词频
data_file='./output/新闻联播输出结果.csv'
data=open(data_file,'r',encoding='utf-8-sig')
reader=csv.reader(data)


#把原始数据转换为pyecharts制词云所需要的格式，即[(a,b),(c,d)....]
visual_list=[]
for i in reader:
    name = i[0]
    number = i[1]
    visual_list.append((name,number))
    
data.close()
c = (
    WordCloud()
    .add("", visual_list, word_size_range=[10, 70], mask_image='./data/蝴蝶剪影.png',shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="2023-03-01到2023-03-30新闻联播高频词词云"))
    #.render("./output/新闻联播高频词词云.html")
)
print('词云生成完毕')

#把已有数据整理成生成柱状图所需要的格式
name=[]
number=[]
num_counter=0
for i in visual_list:
    num_counter += 1
    if num_counter < 21:#用于计数，只显示前20位的数据（数据过多图表很难看）
        name.append(i[0])
        number.append(int(i[1]))
bar=(
     Bar()
     .add_xaxis(name)
     .add_yaxis('数量',number)
     .set_global_opts(#设置标题，x轴，y轴等等
         title_opts=opts.TitleOpts(title='新闻联播高频词柱状图'),
         yaxis_opts=opts.AxisOpts(name='出现次数'),
         xaxis_opts=opts.AxisOpts(name='词语名称'),
         datazoom_opts=opts.DataZoomOpts())
     .set_colors(['#9A0002'])#转化为北大红的颜色
    # .render('./output/新闻联播高频词柱状图.html')
)
print('柱状图生成完毕')

#把图表生成到一个网页中
page= Page(layout=Page.SimplePageLayout)
page.add(bar)
page.add(c)
page.render('./output/新闻联播可视化两图合一.html')

