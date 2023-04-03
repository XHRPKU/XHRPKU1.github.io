# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:04:09 2023

@author: 傲娇的淡定着
"""
'''丝绸之路分为陆路丝绸之路和海上丝绸之路两条，其中陆路丝绸之路起源于我国西汉时期，彼时汉武帝派遣张骞等人从
长安出发，经过甘肃，新疆，抵达中亚，西亚，和欧洲；而海上丝绸之路则在秦汉时期便有史料可循，在唐宋时期达到了顶峰
两条丝绸之路是中国对外交流，促进世界文明发展的重要历史标志。因此笔者想在这次作业中记录下两条丝绸之路关键的城市
并简单地复刻丝绸之路的主要线路
'''
#引入所需要的模块
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

#生成基础的画面，并限定生成的大小
geo = Geo(init_opts=opts.InitOpts(width='1920px',height='1080px'))


#路上丝绸之路主要城市
geo.add_coordinate(name="Xi-an",longitude=108.94, latitude=34.34)
geo.add_coordinate(name="lanzhou",longitude=103.83, latitude=36.96)
geo.add_coordinate(name="Urumqi",longitude=87.62, latitude=43.83)
geo.add_coordinate(name="Khorgas",longitude=80.43, latitude=44.00)
geo.add_coordinate(name="Bishkek",longitude=74.58, latitude=42.87)
geo.add_coordinate(name="Dushanbe",longitude=68.78, latitude=38.56)
geo.add_coordinate(name="Samarkand",longitude=66.97, latitude=39.63)
geo.add_coordinate(name="Tehran",longitude=51.39, latitude=35.69)
geo.add_coordinate(name="Istanbul",longitude=28.98, latitude=41.01)
geo.add_coordinate(name="Moscow",longitude=37.61, latitude=55.76)
geo.add_coordinate(name="Duisburg",longitude=6.77, latitude=51.43)

#给出绘制的地图样式
geo.add_schema(maptype='world')
#添加丝绸之路起点和重点到地图上
geo.add('',[("Xi-an",50),('Duisburg',50)],type_=ChartType.EFFECT_SCATTER,color='GREEN',
        symbol_size=20,
        label_opts=opts.LabelOpts(formatter='{b}',is_show=True)
        )

#添加途径城市
geo.add('',[("lanzhou",10),('Urumqi',10),("Khorgas",10),("Bishkek",10),("Dushanbe",10),\
         ("Samarkand",10),("Tehran",10),("Istanbul",10),("Moscow",10)],type_=ChartType.SCATTER,
        symbol_size=18,
        label_opts=opts.LabelOpts(formatter='{b}',is_show=True),
        color='#808000')

#添加对应线路
geo.add(
        '陆上丝绸之路',
        [('Xi-an','lanzhou'),('lanzhou','Urumqi'),('Urumqi','Khorgas'),\
         ('Khorgas','Bishkek'),('Bishkek','Dushanbe'),('Dushanbe','Samarkand'),\
         ('Samarkand','Tehran'),('Tehran','Istanbul'),('Istanbul','Moscow'),('Moscow','Duisburg')],
        type_=GeoType.LINES,
        color='#DAA520',
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=5,
                                    color='#DAA520'),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False)
        )

#海上丝绸之路主要城市
geo.add_coordinate(name="Fuzhou",longitude=119.3, latitude=26.08)
geo.add_coordinate(name="Guangzhou",longitude=113.23, latitude=23.16)
geo.add_coordinate(name="Hanoi",longitude=105.55, latitude=21.03)
geo.add_coordinate(name="Kuala Lumpur",longitude=101.7, latitude=3.13)
geo.add_coordinate(name="Jakarta",longitude=106.49, latitude=-6.09)
geo.add_coordinate(name="Kolkata",longitude=88.22, latitude=22.34)
geo.add_coordinate(name="Colombo",longitude=79.85, latitude=6.93)
geo.add_coordinate(name="Nairobi",longitude=36.82, latitude=-1.28)
geo.add_coordinate(name="Athens",longitude=23.73, latitude=37.98)
geo.add_coordinate(name="Venice",longitude=12.34, latitude=45.44)
geo.add_coordinate(name="Rotterdam",longitude=4.48, latitude=51.92)

#添加起点和终点
geo.add('',[("Fuzhou",50),('Rotterdam',50)],type_=ChartType.EFFECT_SCATTER,color='blue',
        symbol_size=20,
        label_opts=opts.LabelOpts(formatter='{b}',is_show=True)
        )

#添加其他港口
geo.add('',
        [("Guangzhou",10),('Hanoi',10),("Kuala Lumpur",10),("Jakarta",10),("Kolkata",10),\
         ("Colombo",10),("Nairobi",10),("Athens",10),("Venice",10)],
        type_=ChartType.SCATTER,color='#00FFFF',
        label_opts=opts.LabelOpts(formatter='{b}',is_show=True),
        symbol_size=18)

#添加路线
geo.add(
        '海上丝绸之路',
        [('Fuzhou','Guangzhou'),('Guangzhou','Hanoi'),('Hanoi','Kuala Lumpur'),('Kuala Lumpur','Jakarta'),('Jakarta','Kolkata'),\
         ('Kolkata','Colombo'),('Colombo','Nairobi'),('Nairobi','Athens'),('Athens','Venice'),('Venice','Rotterdam'),\
         ('Kolkata','Nairobi'),('Kuala Lumpur','Colombo')],
        type_=GeoType.LINES,
        color='#48D1CC',
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=5),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False)
        )

#渲染最终成果
geo.render('./output/国际地图可视化-丝绸之路.html')

