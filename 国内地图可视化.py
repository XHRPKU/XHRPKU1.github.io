# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 19:49:40 2023

@author: 傲娇的淡定着
"""
'''国内地图可视化，笔者想做一个2020-2022年的全国各省gdp变化图（不包括港澳台），在这张图上，读者可以清楚看到
各省份的gdp差异，以及gdp在这三年来的变化。而根据马克思主义经济学视角来看，经济基础决定上层建筑
经济发达的地区教育事业发展也相对较好。笔者来自西藏，教育资源相对落后，1985年起，在国家教育部牵头
下，西藏自治区教育厅与全国内陆经济发达省份教育厅展开合作，创办内地西藏初中、高中、中专班等，把西
藏学生送到内地经济、教育更发达的地方求学。笔者正是这一政策的受益者，因而在已有地图的基础上，笔者
还希望对展开西藏-内地合作的地区进行可视化，并且标注出自己的求学之路。读者也可以在这张图中看到西藏
与其他省份之间经济的差距，并感受到这一政策的必要性
'''
#引入需要使用的库
from pyecharts import options as opts
from pyecharts.charts import Map,Timeline
import csv

#打开数据文件
gdp_data_file='./data/2020-2022各省GDP.csv'
gdp_data=open(gdp_data_file,'r',encoding='utf-8')
reader=csv.reader(gdp_data)

#跳过第一行-标题
next(reader)

#建立相关的数据集
gdp_2020=[]
gdp_2021=[]
gdp_2022=[]
for i in reader:
    gdp_2020.append((i[0],int(i[1])))
    gdp_2021.append((i[0],int(i[2])))
    gdp_2022.append((i[0],int(i[3])))



#定义时间轴
time_line=['2020','2021','2022']

#创建时间轴
timeline = Timeline(init_opts=opts.InitOpts(width='1080px',height='720px')) 

#把数据整理到可视化图表中
#笔者此处是想通过循环来完成的，但是尝试了一些方法后（例如
#for i in time_line:
#    ··· f'gdp_{i}'后并不能很好的实现，所以只能用最原始的方法进行整理了...

c_2020=(
       Map()
       .add("总GDP",gdp_2020,'china')
       .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
       .set_global_opts(
           title_opts=opts.TitleOpts(title='2020-2022全国gdp'),
           visualmap_opts=opts.VisualMapOpts(max_=129200),
        )
       )
timeline.add(c_2020,time_point='2020')

c_2021=(
       Map()
       .add("总GDP",gdp_2021,'china')
       .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
       .set_global_opts(
           title_opts=opts.TitleOpts(title='2020-2022全国gdp'),
           visualmap_opts=opts.VisualMapOpts(max_=129200),
        )
       )
timeline.add(c_2021,time_point='2021')

c_2022=(
       Map()
       .add("总GDP",gdp_2022,'china')
       .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
       .set_global_opts(
           title_opts=opts.TitleOpts(title='2020-2022全国gdp'),
           visualmap_opts=opts.VisualMapOpts(max_=129200),
        )
       )
timeline.add(c_2022,time_point='2022')

#渲染最终成果
timeline.render('./output/2020-2022全国各省gdp汇总.html')

