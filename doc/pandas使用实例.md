#### [层次化索引](https://www.jianshu.com/p/efab7d81c0ab)
pandas中的层次化索引使我们能以低纬度形式处理高纬度数据
```buildoutcfg
data.unstack().stack()
```
#### [数据重塑](https://blog.csdn.net/wj1066/article/details/82261458)
> df.pivot() # 将列数据转化为多维数据
```angular2
# 调用pivot方法前需要保证数据集中不存在重复条目
df.pivot(index='列名',columns='列名',values='列名')# 不写values怎会返回层次化索引的全部

# pivot_table()
df.pivot_table(index='列名',columns='列名',values='列名',aggfunc='')#aggfunc参数用于指明转换时所需的汇总函数
```
> df.melt() # 与pivot()相反，将高纬度数据转化为列数据
```angular2
df.melt(id_vars=['保留的列名'],value_vars=['变为值的列名'],var_name='变为值的列后的列名',value_name=)
```

#### [groupby的索引和迭代](https://blog.csdn.net/leonis_v/article/details/51832916)
* groupby对象是一个迭代对象，每次迭代结果是一个元组，
元组的第一个元素是还组的名称(就是groupby列的元素名称),第二个元素是该组的具体信息，是
一个dataframe，索引是以前dataframe的总索引。
```buildoutcfg

```

#### [数据的合并merge,concat,join](https://blog.csdn.net/weixin_38168620/article/details/80663892)
```angular2
pd.concat([a,b],axis=1)# 纵向连接，以index来合并
```
#### [数据合并merge](https://blog.csdn.net/brucewong0516/article/details/82707492)
```angular2
pd.merge(left, right, left_on='key', right_index=True, how='left', sort=False)
```
#### [apply函数](https://blog.csdn.net/qq_19528953/article/details/79348929)
* apply函数是`pandas`里面所有函数中自由度最高的函数。该函数如下：
```buildoutcfg
DataFrame.apply(func, axis=0, broadcast=False, raw=False, reduce=None, args=(), **kwds
```
#### [pandas数据筛选](https://www.jianshu.com/p/805f20ac6e06)
* 如果要选择某列等于多个数值或者字符串时，要用到.isin()， 我们把df修改了一下（isin()括号里面应该是个list）
```buildoutcfg
df[(df['a']>20) | (df['b']>100)]
# 使用 &（且） 和 |（或） 时每个条件都要用小括号括起来

df[['a','b']][df['c']>100]
df.loc[df['c']>100,(['a','b'])]

# isin()括号里面应该是个list
df[df['z'].isin(list)]

# 平时使用最多的筛选应该是字符串的模糊筛选，在SQL语句里用的是like，在pandas里我们可以用.str.contains()来实现
df.loc[df['a'].str.contains('华东')]

# 也可以使用 '|'来进行多个条件的筛选
df.loc[df['a'].str.contains('华东|华')]

# 排除含有特定值的行或列
data1 = data[(data['客户等级']!=0)]
data2 = data[~data['客户等级'].isin([0])]
```
注意，这个‘|’是在引号内的，而不是将两个字符串分别引起来。’&‘在这里不能用。


#### [pandas处理时间](https://blog.csdn.net/qq_22238533/article/details/77110626)
```angular2

```

#### [pandas去重](https://blog.csdn.net/qq_28811329/article/details/79962511)
```angular2
data.drop_duplicates(subset=['A','B'],keep='first',inplace=True)
```
> subset对应的值是列名，表示只考虑这两列，将这两列对应值相同的行进行去重。默认值为subset=None表示考虑所有列  
> keep='first'表示保留第一次出现的重复行，是默认值。keep另外两个取值为"last"和False，分别表示保留最后一次出现的重复行和去除所有重复行。  
> inplace=True表示直接在原来的DataFrame上删除重复项，而默认值False表示生成一个副本
