#### [层次化索引](https://www.jianshu.com/p/efab7d81c0ab)
pandas中的层次化索引使我们能以低纬度形式处理高纬度数据
```buildoutcfg
data.unstack().stack()
```

#### [groupby的索引和迭代](https://blog.csdn.net/leonis_v/article/details/51832916)
* groupby对象是一个迭代对象，每次迭代结果是一个元组，
元组的第一个元素是还组的名称(就是groupby列的元素名称),第二个元素是该组的具体信息，是
一个dataframe，索引是以前dataframe的总索引。
```buildoutcfg

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

```
注意，这个‘|’是在引号内的，而不是将两个字符串分别引起来。’&‘在这里不能用。
