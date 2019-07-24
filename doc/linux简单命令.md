* 查看某个应用是否安装
> rpm -qa | grep mongodb
* [linux后台运行python](https://blog.csdn.net/qq_16059847/article/details/82837788)
* [各个参数含义](https://blog.csdn.net/wufaliang003/article/details/80275055)
> nohup python -u test.py > out.log 2>&1 &
* 查看后台程序是否运行
> ps -def | grep python

### [安装mysql](https://www.cnblogs.com/gradven/p/5023734.html)
> 设置开放用户远程连接
```mysql
mysql -u root -proot
use mysql;
update user set host = '%' where user = 'root';
select host, user from user;

flush privileges; # 刷新权限，这一步十分重要！
```


