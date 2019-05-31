#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 时间:   2019-5-31 11:30
# 作者:   ljk

import csv
import pandas as pd
f = open('C:/Users/naturade/Desktop/年度数据.csv', encoding='gbk')

data = pd.read_csv(f)
df = data.melt(id_vars=['指标'],var_name='date',value_name='value')
df['type']=''
df=df[['指标','type','date','value']]
df=df.sort_values(by='date')
df.to_csv('C:/Users/naturade/Desktop/年度数据1.csv',index=False,encoding='utf-8')