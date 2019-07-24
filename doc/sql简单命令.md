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

* join后有多个条件时，多余的条件可以写在where中

* [group by聚合函数](https://www.cnblogs.com/geaozhang/p/6745147.html)


* 看表结构
```angular2
show full columns from tablename # 查看表的字段注释
show create table tablename # 查看表的创建语句
```

* [多个字段的in 和 not in 及其替代写法（exists，not exists）](https://blog.csdn.net/weixin_41287692/article/details/80049631)
* sql编写过程
> select...from...join...on...where...group by...having...order by...limit
* sql执行顺序
> from ...on...join...where...group by...having...select distinct...order by...limit

* SQL优化，主要就是在 优化索引
> 索引：相当于书的目录  
> 索引：index是帮助MYSQL高效获取数据的数据结构。树（B树、hash树）