# study_url
学习博客记录

2019-4-17 22:11 linux运行python程序  
<br/>运行脚本的时候出现”/bin/bash^M: 坏的解释器: 没有那个文件或目录\n  
    原因是因为脚本文件在windows系统下编辑过。在Windows下每一行结尾是\n\r，而Linux下则是\n


2019-4-18 23：16 linux的文件权限  
文件权限是系统最底层安全设定方法之一，它保证文件可以被可用的用户做相应操作  
r  

      对文件：是否可以查看文件中的内容   --->cat  file
      对目录：是否可以查看目录中有什么子文件或者子目录 --->ls dir
w   
      对文件：是否可以改变文件里面记录的字符
      对目录：是否可以对目录中有什么子文件或者子目录的元数据进行更改
x     
      对文件：是否可以通过文件名称调用文件内记录的的程序
      对目录：是否可以进入目录
