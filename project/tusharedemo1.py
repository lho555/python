import tushare as ts
import datetime
import pandas as pd
import matplotlib.dates as dates
import matplotlib.finance as f
import matplotlib.pyplot as plt

all_df = ts.get_hist_data('601233',start='2014-01-01',end='2016-03-01')
all_df = all_df.sort_index(ascending=True)
#print(all_df)
params = [5, 10, 20, 60]
for p in params:
    all_df['ma'+str(p)] =  pd.Series(all_df['close']).rolling(window=p).mean()
#print(all_df.index)
df = all_df[pd.DatetimeIndex(all_df.index).year == 2015]
print(df)
pre = None
golden_cross = pd.DataFrame()
for index, row in df.iterrows():
    if not pre is None:
        if pre['ma5'] < pre['ma10'] and row['ma5'] > row['ma10'] \
        and pre['ma5'] < row['ma5'] and pre['ma10'] < row['ma10']:
            golden_cross = golden_cross.append(row)
            print(index)
            print('昨日MA5 = %s ，昨日MA10 = %s' % (pre['ma5'], pre['ma10'],))
            print('今日MA5 = %s ，今日MA10 = %s' % (row['ma5'], row['ma10']))
            print('----------')
    pre = row