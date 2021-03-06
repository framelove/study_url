* 清空某表的数据 且让自增的id重新从0开始
> truncate table

* distinct 后跟两个字段时，两个字段都不同才算不同
> [lianjie ](https://blog.csdn.net/djun100/article/details/10452165)

* truncate,delete和drop的区别
> [lianjie](https://www.cnblogs.com/SaraMoring/p/5607537.html)
>> 想删除部分数据行用 delete，注意带上where子句. 回滚段要足够大.  
>> 想删除表,当然用 drop  
>> 想保留表而将所有数据删除，如果和事务无关，用truncate即可  
>> 如果和事务有关,或者想触发trigger,还是用delete。  
>> 如果是整理表内部的碎片，可以用truncate跟上reuse stroage，再重新导入/插入数据。

* limit 10,4 = limit 4 offset 10

* join后有多个条件时，多余的条件可以写在where中（X)
> 把条件写到where中会有一些问题，比如说on字段为空的一些数据就显示不出来了。

* [group by聚合函数](https://www.cnblogs.com/geaozhang/p/6745147.html)


* 看表结构
```
show full columns from tablename # 查看表的字段注释
show create table tablename # 查看表的创建语句
```
* [看数据库中所有表的注释](https://www.cnblogs.com/xphdbky/p/7047878.html)
```mysql
#查询所有表的注释和字段注释
SELECT
a.table_name 表名,
a.table_comment 表说明,
b.COLUMN_NAME 字段名,
b.column_comment 字段说明,
b.column_type 字段类型,
b.column_key 约束
FROM
information_schema. TABLES a
LEFT JOIN information_schema. COLUMNS b ON a.table_name = b.TABLE_NAME
WHERE
a.table_schema = '数据库'
ORDER BY
a.table_name
```
* [多个字段的in 和 not in 及其替代写法（exists，not exists）](https://blog.csdn.net/weixin_41287692/article/details/80049631)
* [in,not in与exists,not exists的对比](https://blog.csdn.net/dingweiye123/article/details/81005470)
> exists用来判断查询到的结果是否为空，它并不返回任何值，not exists也是一样
* [not in优化](https://blog.csdn.net/pcwblover008/article/details/80015855)
* sql编写过程
> select...from...join...on...where...group by...having...order by...limit
* sql执行顺序
> from ...on...join...where...group by...having...select distinct...order by...limit


* [group_concat](https://www.cnblogs.com/rxhuiu/p/9134009.html)
```
group_concat( [distinct] 要连接的字段 [order by 排序字段 asc/desc  ] [separator '分隔符'] )
group_concat(
	concat_ws(
	'-',
	a.ftype,
	b.NAME,
	bb.NAME))
```
* [mysql远程连接后本地连接不上](https://blog.csdn.net/qq_38709999/article/details/86554619)
### 更新增量数据
### 
* 如果记录存在则更新/如果不存在则插入[INSERT ON DUPLICATE KEY UPDATE](https://cloud.tencent.com/developer/article/1375845)
```
insert into
   Shops(shopid, viewtotal)  
values(1,123456),  
(2, 234567), 
(3, 345678) 
on duplicate key update
  shopid = values(shopid), 
  viewtotal = values(viewtotal)

```
> 如果你插入的记录导致UNIQUE索引重复，那么就会认为该条记录存在，则执行update语句而不是insert语句，反之，则执行insert语句而不是更新语句。

* SQL优化，主要就是在 优化索引
> 索引：相当于书的目录  
> 索引：index是帮助MYSQL高效获取数据的数据结构。树（B树、hash树）

* 条件过滤时（where),如果用到一些值为null的字段，容易将它们过滤掉

* 存储过程

* 子查询
> 子查询是一次性视图，在select语句执行完之后就会消失。  
> SQL运行顺序：先运行子查询，再运行子查询外面的语句。  
* [关联子查询](https://zhuanlan.zhihu.com/p/93768619)
> 在细分的组内进行比较时，可以使用关联子查询。关联子查询起关键作用的是子查询语句中的where子句。

