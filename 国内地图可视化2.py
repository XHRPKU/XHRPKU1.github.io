# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 13:28:16 2023

@author: 傲娇的淡定着
"""
'''本代码是国内gdp的续版，在这张图中，读者可以细致看到招收西藏班的内地省市
'''

from pyecharts import options as opts
from pyecharts.charts import Geo,Timeline
from pyecharts.globals import ChartType, SymbolType

#定义时间轴
Time_line=['对口援建','内地初中班','内地高中班','个人求学轨迹']

#创建时间轴
timeline = Timeline(init_opts=opts.InitOpts(width='1080px',height='720px'))

#添加对口援建相关信息
c_duikou=(
   Geo()
   .add_schema(maptype='china',itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
   .add(
        '',
        [('拉萨',10),('林芝',10),('阿里',10)],#西藏有7个地级市，但全表现在图表中影响美观，故只选取了3个
        type_=ChartType.EFFECT_SCATTER,
        color='#A0522D',
        )
   
   .add(
        '',
        [('广州',10),('福州',10),\
         ('北京',10),('南京',10),('石家庄',10),\
        ('西安',10)],
        type_=ChartType.SCATTER,
        color='white',
        )
       
    .add(
        '对口援建',
        [('广州','林芝'),('福州','林芝'),('北京','拉萨'),('南京','拉萨'),\
       ('石家庄','阿里'), ('西安','阿里')],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW,symbol_size=5,color='#7CFC00'),
        linestyle_opts=opts.LineStyleOpts(curve=-0.2,color='#7CFC00'),
        )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="对口援建")) 
)
    
timeline.add(c_duikou,time_point='对口援建')   

#添加内地初中班相关
c_junior=(
    Geo()
    .add_schema(maptype='china',itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(
         '',
         [('拉萨',10)],
         type_=ChartType.EFFECT_SCATTER,
         color='#A0522D',
         )
    .add(
         '',
         [('重庆',10),('三明',10),('中山',10),('合肥',10),('辽阳',10)],
         type_=ChartType.SCATTER,
         color='white',
         )
    .add(
         '内地初中班开设单位',#以内地初中班-汉族招生为例，以拉萨为起点为例
         [('拉萨','中山'),('拉萨','重庆'),('拉萨','辽阳'),('拉萨','合肥'),('拉萨','三明')],
         type_=ChartType.LINES,
         effect_opts=opts.EffectOpts(
             symbol=SymbolType.ARROW,symbol_size=5,color='#FFFF00'),
         linestyle_opts=opts.LineStyleOpts(curve=0.4,color='#FFFF00'),
         )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="内地初中班（汉班）")) 
    )

timeline.add(c_junior,time_point='内地初中班')   
  
#添加内地高中班相关
c_senior=(
    Geo()
    .add_schema(maptype='china',itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(
         '',
         [('拉萨',10)],
         type_=ChartType.EFFECT_SCATTER,
         color='#A0522D',
         )
    .add(
         '',
         [('上海',10),('泰安',10),('成都',10),('天津',10),('佛山',10),('太原',10),\
          ('北京',10),('咸阳',10),('湖州',10),('中山',10),('南通',10),\
         ('西安',10),('芜湖',10)],
         type_=ChartType.SCATTER,
         color='white',
         )
    .add(
         '内地高中班开设单位',#以内地初中班-汉族招生为例，以拉萨为起点为例
         [('拉萨','上海'),('拉萨','北京'),('拉萨','西安'),('拉萨','咸阳'),('拉萨','佛山'),\
          ('拉萨','中山'),('拉萨','湖州'),('拉萨','成都'),('拉萨','南通'),('拉萨','天津'),\
        ('拉萨','太原'),('拉萨','芜湖'),('拉萨','泰安')],#由于招收的地区比较多，且每年可能都有变化，所以仅选取部分地区
         type_=ChartType.LINES,
         effect_opts=opts.EffectOpts(
             symbol=SymbolType.ARROW,symbol_size=5,color='#8B008B'),
         linestyle_opts=opts.LineStyleOpts(curve=0.2,color='#8B008B'),
         )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="内地高中班（汉-藏-其他少数民族班）")) 
    )

timeline.add(c_senior,time_point='内地高中班')  

#添加个人行动轨迹
c_self=(
    Geo()
    .add_schema(maptype='china',itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(
         '',
         [('林芝',10)],
         type_=ChartType.EFFECT_SCATTER,
         color='#A0522D',
         )
    .add(
         '',
         [('上海',10),('成都',10),('中山',10),('北京',10)],
         type_=ChartType.SCATTER,
         color='white',
         )
    .add(
         '个人行动轨迹',
         [('林芝','成都'),('成都','林芝'),('林芝','中山'),('中山','上海'),('上海','北京')],
         type_=ChartType.LINES,
         effect_opts=opts.EffectOpts(
             symbol=SymbolType.ARROW,symbol_size=5,color='#000080'),
         linestyle_opts=opts.LineStyleOpts(curve=0.2,color='#000080'),
         )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="个人求学轨迹（从小学到大学")) 
    )

timeline.add(c_self,time_point='个人求学轨迹')  

#渲染最终成果
timeline.render('./output/西藏-内地相关1.html')           