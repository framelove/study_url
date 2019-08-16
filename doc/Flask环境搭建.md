### 1. 搭建独立虚拟开发环境
> windows下虚拟环境安装
```
pip3 install virtualenv
virtualenv flask_env
cd flask_env
cd Scripts
activate
pip install flask
```

> linux 下虚拟环境
```
source bin/activate
```

### 2.flask-SQLAlchemy的使用
> 是对应于SQLAlchemy的flask扩展包，也就是对象关系映射包，或者ORMs，ORM可以使用类，对象，方法来代替表和sql语句，ORM的工作就是将更高层次的操作翻译成数据库操作命令，说白了就是在数据库操作上一层再封装一层，且封装成我们熟悉的类，对象，让我们更方便的操作

```
from app import db
from app.models import User, Post
db.drop_all()
db.create_all()
```

### 3.flask-login
> pip install 报错  
>> 使用'pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org 库名' 解决
