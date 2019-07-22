###0.[配置静态ip](https://blog.51cto.com/mrxiong2017/2084560)
> 为了能够使用静态IP，这里不要勾选”使用本地DHCP服务将IP分配给虚拟机“这个选项。然后是配置子网ip，子网IP与宿主机的ip一定不能处在同一地址范围里，否则就算虚拟机能上网，网络既慢，还不稳定。我主机的ip段是192.168.115.xxx，所以我配了192.168.10.xxx来避开主机的ip段，反正ip的第三个数字在0到254并且不是115就行。Nat模式相当于配置了一个子路由器，有设置过多级路由的朋友对此应该有所体会。各位结合自己机器的IP来合理配置一个子网ip吧
###1. 修改主机名

```
# 查看主机名
vim /etc/hostname
hostnamectl
# 修改主机名
hostnamectl set-hostname xxx
# 手动更新/etc/hosts/
vim /etc/hosts	
# 重启
reboot -f 
```
###2. [关闭防火墙](https://blog.csdn.net/ViJayThresh/article/details/81284007)
```
# 执行关闭防火墙命令： 
systemctl stop firewalld.service
# 查看防火墙命令：
systemctl status firewalld.service
```

###3. [完全分布式集群(单点）](https://www.cnblogs.com/frankdeng/p/9047698.html)

> [（舍弃）（安装hadoop及配置文件](https://segmentfault.com/a/1190000011832566)
>> Namenode和ResourceManger如果不是同一台机器，不能在NameNode上启动 yarn，应该在ResouceManager所在的机器上启动yarn
```

```
