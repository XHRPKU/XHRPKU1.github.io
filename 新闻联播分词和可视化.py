# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:43:13 2023

@author: 傲娇的淡定着
"""
'''本代码主要目的是对已有的txt文件进行分词处理，并对分词的结果进行统计，方便后续的可视化
'''
#引入需要使用的模块
import jieba
import re

#相关文件的汇总与打开
news_report_file='./data/新闻联播.txt'
news_outcome_file='./output/新闻联播输出结果.csv'
HIT_stop_file='./data/哈工大停用词表.txt'

#打开原始数据文件
news_report=open(news_report_file,'r',encoding='utf-8')
news=news_report.read()
news_report.close()

#打开停用词表
HIT_stop=open(HIT_stop_file,'r',encoding='utf-8')
stopwords=HIT_stop.readlines()
stopwords_2=[]
#去除读取文件中的换行符
for i in stopwords:
    i=i.strip('\n')
    stopwords_2.append(i)
#作为国家级电视台，新闻联播普遍使用中文，英文（或其他外语）的使用非常之少）因而分词的统计很难有实际的研究价值
#与此同时，新闻中播报的数据在脱离了文本后也没有任何意义，因而此处需要对文本进行预处理，即除去没有研究价值的数
#字，英文，符号等等，而仅仅保留中文。代码利用正则表达式对news进行检索，根据中文字符的编码规则，该正则表达式表
#示匹配多个非汉字字符，而把他们都替换为''
news = re.sub(r'[^\u4e00-\u9fa5]+', '', news)

news_list=jieba.lcut(news,cut_all=False)

news_dict={}
for i in news_list:
    if i not in stopwords_2 and len(i)>=2:#根据停用词表去除无意义字符，且有相当部分的单字很难单独表意，故一并去除，若后续研究有相关需要，也可以快速复原
        if i in news_dict.keys():
            news_dict[i] += 1
        else:
            news_dict[i] = 1

HIT_stop.close()
#对字典按照数值大小降序排列
sort_news_dict=sorted(news_dict.items(), key=lambda x:x[1],reverse= True)

#打开输出结果的表格
news_outcome=open(news_outcome_file,'w',encoding='utf-8-sig')

#设立计数器，由于最终分词结果过于庞大，因此仅选取前X部分的词语进行可视化（x可变）
num_count=0
for word, number in sort_news_dict:
    if num_count <100:
        num_count += 1
        if number <=1:
            pass
        else: 
            news_outcome.write(word+','+str(number)+'\n')
news_outcome.close()

     
