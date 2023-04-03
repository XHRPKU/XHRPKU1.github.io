# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:34:07 2023

@author: 傲娇的淡定着
"""
'''笔者曾选过城市与环境学院的两门必修课程，在学习过程中认识到了水环境质量检测的各种指标
水环境质量是指水体环境中的各项物理、化学和生物特性，反应了水质的好坏。
溶解氧指水中溶解的氧气分子含量，含量多少与水生生物是否能生存密切相关
高锰酸盐是反应水体氧化物含量的指标，指标越高，说明水体氧化物质越多，污染程度越高
氨氮指水体中溶解态和游离态的综合，主要来自于生活、工业和农业，是一种重要的水污染物
总磷是水体中所有磷元素形式的总和，是水生生物的营养物质，但是含量过高将会导致水体的富营养化。
本题中，笔者以上海市的母亲河——苏州河为例，对其2021年各项污染指标进行可视化衡量
'''
#引入需要的模块
from pyecharts import options as opts
from pyecharts.charts import Bar, Line

#建立x轴
x_data=["{}月".format(i) for i in range(1,13)]

#列出相关数据
y1=[7.2, 8.2, 11.5, 16.4, 22.1, 27.0, 30.2, 28.6, 24.3, 19.1, 13.1, 8.5]#水温
y2=[8.7, 8.6, 9.2, 9.5, 8.8, 8.5, 8.2, 8.0, 8.6, 8.9, 9.1, 9.0]#溶解氧
y3=[2.0, 2.2, 2.6, 2.4, 2.0, 2.1, 2.3, 2.1, 2.5, 2.7, 2.6, 2.4]#高锰酸盐
y4=[0.14, 0.16, 0.17, 0.19, 0.21, 0.23, 0.25, 0.26, 0.25, 0.22, 0.20, 0.18]#氨氮
y5=[0.032, 0.035, 0.040, 0.044, 0.048, 0.053, 0.057, 0.060, 0.056, 0.051, 0.046, 0.042]#总磷

#绘制柱状图
bar=(
     Bar(init_opts=opts.InitOpts(width="1920px", height="720px"))#由于涵盖的数据较多，因而特别设置了生成图片的长和宽
     .add_xaxis(x_data)
     .add_yaxis('溶解氧（mg/l）', y2,yaxis_index=1,color="#8ECFC9",z=10)#调整z的优先级，使得折线图在柱状图之上
     .add_yaxis("高锰酸盐（mg/l）", y3,yaxis_index=2,color='#FFBE7A',z=10)
     .add_yaxis("氨氮（mg/l）", y4,yaxis_index=3,color='#FA7F6F',z=10)
     .add_yaxis("总磷（μg/l）", y5,yaxis_index=4,color="#82B0D2",z=10)
     .extend_axis(#从这一步开始都是添加新的y轴，每条y轴对应不同的量纲
         yaxis=opts.AxisOpts(
             name="溶解氧",
             type_="value",
             min_=7,
             max_=10,
             position="left",#由于柱状图数据较多，所以左边两个右边两个
             offset=50,#设置新的y轴与原始图像之间的距离
             axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(color="#8ECFC9")
             ),
             axislabel_opts=opts.LabelOpts(formatter="{value} "),#通过该式确保对应y轴刻度与柱状图相一致
         )
     )
     .extend_axis(
         yaxis=opts.AxisOpts(
             name="高锰酸盐",
             type_="value",
             min_=1.5,
             max_=3,
             position="left",
             offset=100,
             axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(color="#FFBE7A")
             ),
             axislabel_opts=opts.LabelOpts(formatter="{value} "),
         )
     )
     .extend_axis(
         yaxis=opts.AxisOpts(
             name="氨氮",
             type_="value",
             min_=0.1,
             max_=0.3,
             position="right",
             offset=50,
             axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(color="#FA7F6F")
             ),
             axislabel_opts=opts.LabelOpts(formatter="{value} "),
         )
     )
     .extend_axis(
         yaxis=opts.AxisOpts(
             name="总磷",
             type_="value",
             min_=0.03,
             max_=0.065,
             position="right",
             offset=100,
             axisline_opts=opts.AxisLineOpts(
                 linestyle_opts=opts.LineStyleOpts(color="#82B0D2")
             ),
             axislabel_opts=opts.LabelOpts(formatter="{value} "),
         )
     )

     .set_series_opts(label_opts=opts.LabelOpts(is_show=True))#由于生成图像较大，因此这些数据显示不会特别影响观感
     .set_global_opts(title_opts=opts.TitleOpts("苏州河2021水质指标可视化"),
                      yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}℃')))#初始化最原始的y轴
     )

#生成水温折线图
line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis("平均水温", y1,z=11)
)

#把生成的折线图叠加在柱状图上
bar.overlap(line)

#对生成的结果进行渲染
bar.render('./output/苏州河2021水质检测可视化.html')



