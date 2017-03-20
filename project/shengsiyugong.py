import tushare as ts
import pandas as pd
import os
import csv
'''
def download(code, name, index=False):
    filename = './'+code+'-'+name+str('.csv')
    if os.path.exists(filename):
        os.remove(filename)
        print('%s已存在，删除源文件' % filename)
    df = ts.get_h_data(code, start='2000-01-01', end='2017-01-01', index=index)
    df = df.sort_index(ascending=True).reset_index()
    df.to_csv(filename, mode='a', index=False)
download('000001','上证指数',index=True)
'''
code='000001'
df = ts.get_h_data(code, start='2000-01-01', end='2017-01-01', index=True)
df = df.sort_index(ascending=True).reset_index()

#df = open('000001-上证指数.csv', 'r')
pd.set_option('display.float_format', lambda x: '%.02f' % x)
df.describe().transpose()
ax = df.boxplot(column=['close','high','low','open'],return_type='axes')
print(ax)

df['price_change'] = df['close'] - df['open']
df['price_change_p'] = df['price_change'] / df['open']
fig,ax = plt.subplots(figsize=(16,6))
ax.bar(df.index,df['price_change_p'])
plt.show()
