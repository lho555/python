import matplotlib.dates as dates
import matplotlib.finance as f  
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import tushare as ts

ts.get_hist_data('600848') #一次性获取全部日k线数据
ts.get_hist_data('600848',start='2015-05-01',end='2015-06-18') #指定时间区间
ts.get_hist_data('600848'，ktype='W') #获取周k线数据
ts.get_hist_data('600848'，ktype='M') #获取月k线数据
ts.get_hist_data('600848'，ktype='5') #获取5分钟k线数据
ts.get_hist_data('600848'，ktype='15') #获取15分钟k线数据
ts.get_hist_data('600848'，ktype='30') #获取30分钟k线数据
ts.get_hist_data('600848'，ktype='60') #获取60分钟k线数据
ts.get_hist_data('sh'）#获取上证指数k线数据，其它参数与个股一致，下同
ts.get_hist_data('sz'）#获取深圳成指k线数据
ts.get_hist_data('hs300'）#获取沪深300指数k线数据
ts.get_hist_data('sz50'）#获取上证50指数k线数据
ts.get_hist_data('zxb'）#获取中小板指数k线数据
ts.get_hist_data('cyb'）#获取创业板指数k线数据

ts.get_today_all()#当天实时数据

df = ts.get_index()#大盘指数
ts.new_stocks()#新股数据

#基本面数据
ts.get_stock_basics()
#获取2015年第1季度的业绩报表数据
ts.get_report_data(2015,1)
#获取2015年第1季度的盈利能力数据
ts.get_profit_data(2015,1)
#获取2015年第1季度的营运能力数据
ts.get_operation_data(2015,1)
#获取2015年第1季度的成长能力数据
ts.get_growth_data(2015,1)
#获取2015年第1季度的偿债能力数据
ts.get_debtpaying_data(2015,1)
#获取2015年第1季度的现金流量数据
ts.get_cashflow_data(2015,1)

#to_csv
df = ts.get_hist_data('000875')
#直接保存
df.to_csv('c:/day/000875.csv')
#选择保存
df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])
#大文件追加
import os
filename = 'c:/day/bigfile.csv'
for code in ['000875', '600848', '000981']:
    df = ts.get_hist_data(code)
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=None)
    else:
        df.to_csv(filename)

#to_excel
df = ts.get_hist_data('000875')
#直接保存
df.to_excel('c:/day/000875.xlsx')
#设定数据位置（从第3行，第6列开始插入数据）
df.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)

#to_sql
from sqlalchemy import create_engine
import tushare as ts
df = ts.get_tick_data('600848', date='2014-12-22')
engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')
#存入数据库
df.to_sql('tick_data',engine)
#追加数据到现有表

#数据绘图
import tushare as ts
import pandas as pd
df=ts.get_hist_data('600415',start='2015-04-01',end='2015-06-18')
# 所有的结果汇图
df.plot()
# 只将stock最高值进行汇图
df.high.plot()
# 指定绘图的四个量，并指定线条颜色
with pd.plot_params.use('x_compat', True):
    df.open.plot(color='g')
    df.close.plot(color='y')
    df.high.plot(color='r')
    df.low.plot(color='b')
# 指定绘图的长宽尺度及背景网格
with pd.plot_params.use('x_compat', True):
    df.high.plot(color='r',figsize=(10,4),grid='on')
    df.low.plot(color='b',figsize=(10,4),grid='on')

#保存图片
import matplotlib
import tushare as ts
import pandas as pd
fig = matplotlib.pyplot.gcf()
df=ts.get_hist_data('600415',start='2015-04-01',end='2015-06-18')
with pd.plot_params.use('x_compat', True):
    df.high.plot(color='r',figsize=(10,4),grid='on')
    df.low.plot(color='b',figsize=(10,4),grid='on')
    fig.savefig('F:/graph.png')    