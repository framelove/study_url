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