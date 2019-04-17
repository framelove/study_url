# study_url
学习博客记录

2019-4-17 22:11 linux运行python程序
    运行脚本的时候出现”/bin/bash^M: 坏的解释器: 没有那个文件或目录\n
    原因是因为脚本文件在windows系统下编辑过。在Windows下每一行结尾是\n\r，而Linux下则是\n
