import pandas as pd
import numpy as np

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)

d = [{'one' : 1,'two':1},{'one' : 2,'two' : 2},{'one' : 3,'two' : 3},{'two' : 4}]
df = pd.DataFrame(d,index=['a','b','c','d'],columns=['one','two'])
df.index.name='index'
#两种不同建立dataframe的方式

#转换其他类型
df.to_dict(outtype='dict') #type=dict,list,series,records
#查看数据head和tail方法可以显示DataFrame前N条和后N条记录，N为对应的参数，默认值为5
df.head()

#index（行）和columns（列）属性，可以获得DataFrame的行和列的标签
df.index
df.columns

#decribe方法可以计算各个列的基本描述统计值。包含计数，平均数，标准差，最大值，最小值及4分位差。
df.describe

#排序sort_index可以以轴的标签进行排序。axis是指用于排序的轴，可选的值有0和1，默认为0即行标签（Y轴），1为按照列标签排序。 ascending是排序方式，默认为True即降序排列。

df.sort_index(axis=1, ascending=False)
df.sort(columns='two')
df.sort(columns=['one','two'],ascending=[0,1])

#读写数据
df = pd.read_csv('foo.csv')
df.to_csv('foo.csv')

xls = ExcelFile('foo.xlsx')
xls.parse('sheet1', index_col=None, na_values=['NA'])
df.to_excel('foo.xlsx', sheet_name='sheet1')

#数据切片
df['one']
df.one  #两句等效 都是返回df名称为one列的数据，返回的为一个Series。

df[0:3]
df[0]
#下标索引选取的是DataFrame的记录，与List相同DataFrame的下标也是从0开始，区间索引的话，为一个左闭右开的区间，即[0：3]选取的为1-3三条记录。

df.loc[行标签,列标签]
df.loc['a':'b']#选取ab两行数据
df.loc[:,'one']#选取one列的数据
#df.loc的第一个参数是行标签，第二个参数为列标签（可选参数，默认为所有列标签），两个参数既可以是列表也可以是单个字符，如果两个参数都为列表则返回的是DataFrame，否则，则为Series。

df.iloc[行位置,列位置]
df.iloc[1,1]#选取第二行，第二列的值，返回的为单个值
df.iloc[0,2],:]#选取第一行及第三行的数据
df.iloc[0:2,:]#选取第一行到第三行（不包含）的数据
df.iloc[:,1]#选取所有记录的第一列的值，返回的为一个Series
df.iloc[1,:]#选取第一行数据，返回的为一个Series

df.ix[1,1]
df.ix['a':'b']
#更广义的切片方式是使用.ix,自动根据索引类型判断使用位置还是标签

df[逻辑条件]
df[df.one >= 2]#单个逻辑条件
df[(df.one >=1 ) & (df.one < 3) ]#多个逻辑条件组合
#通过逻辑指针进行数据切片

df.mean()#计算列的平均值，参数为轴，可选值为0或1.默认为0，即按照列运算
df.sum(1)#计算行的和
df.apply(lambda x: x.max() - x.min())#将一个函数应用到DataFrame的每一列，这里使用的是匿名lambda函数，与R中apply函数类似
#基本运算

df.set_index('one')
#设置索引

df.rename(columns=(u'one':'1'), inplace=True)
#重命名列

df.dtypes
#查看每个列的数据类型

pd.Series.max()
pd.Series.idxmax()
#最大/小值

#重设索引
df.reset_index(inplace=True)
#改变数据类型
df['A'].astype(float)
#计算Series每个值的频率
df['A'].value_counts()

#字符串方法
s.str.lower()
s.str.len()
s.str.contains(pattern)

#DataFrame的合并
#Contact：

ds = [{'one' : 4,'two':2},{'one' : 5,'two' : 3},{'one' : 6,'two' : 4},{'two' : 7,'three':10}]
dfs = pd.DataFrame(ds,index=['e','f','g','h'])
##构建一个新的DataFrame，dfs
df_t=pd.concat([df,dfs])#合并两个DataFrame

#Merge（类似SQL中的Join操作）：

left = pd.DataFrame({'key': ['foo1', 'foo2'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo1', 'foo2'], 'rval': [4, 5]})
#构建了两个DataFrame
pd.merge(left, right, on='key')#按照key列将两个DataFrame join在一起

#DataFrame中的Group by：

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
                    'C' :randn(8), 'D' : randn(8)});
df.groupby('A').sum()#按照A列的值分组求和
df.groupby(['A','B']).sum()##按照A、B两列的值分组求和

#在实际应用中，先定义groups，然后再对不同的指标指定不同计算方式。

groups = df.groupby('A')#按照A列的值分组求和
groups['B'].sum()##按照A列的值分组求B组和
groups['B'].count()##按照A列的值分组B组计数
#默认会以groupby的值作为索引，如果不将这些值作为索引，则需要使用as_index=False

df.groupby(['A','B'], as_index=False).sum()

#构建透视表
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,'B' : ['A', 'B', 'C'] * 4, 
                'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2, 
                'D' : np.random.randn(12), 'E' : np.random.randn(12)})
pd.pivot_table(df, values = 'D', rows = ['A', 'B'], cols = ['C'])#以A、B为行标签，以C为列标签将D列的值汇总求和
pd.crosstab(rows = ['A', 'B'], cols = ['C'], values = 'D')#以A、B为行标签，以C为列标签将D列的值汇总求和

#时间序列分析
#时间序列也是Pandas的一个特色。时间序列在Pandas中就是以Timestamp为索引的Series。

#pandas提供to_datetime方法将代表时间的字符转化为Timestamp对象：

s = '2013-09-16 21:00:00'
ts = pd.to_datetime(s)
#有时我们需要处理时区问题：

ts=pd.to_datetime(s,utc=True).tz_convert('Asia/Shanghai')
#构建一个时间序列：

rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(randn(len(rng)), index=rng)
#Pandas提供resample方法对时间序列的时间粒度进行调整：

ts_h=ts.resample('H', how='count')#M,5Min,1s

