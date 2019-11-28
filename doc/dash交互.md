###[dash](https://www.jianshu.com/p/0aaafaa33bb1)

####1.dash应用布局

> layout 由 html.Div与 dcc.Graph这样的组件树组成
> 

####2.dash交互性组件
```python
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
    dcc.Input(id='my-id', value='初始值', type='text'),
    html.Div(id='my-div')
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return '你输入了 "{}"'.format(input_value)
```
> app.callback装饰器通过声明描述应用界面的“输入”与“输出”项  
> Dash应用的输入、输出项是指定组件的特性。本例中，输入项是ID名为my-id 组件的value特性。 输出项是ID名为my-div 组件的children特性。  
> Dash提供了输入项特性改变时，能够自动调用callback装饰器打包的函数。输入项特性的值更新后，可以作为输入项参数，然后返回该函数的输入内容  
> component_id 与 component_property 关键字是可选的，这些对象只有两个参数。本例中为了便于理解，列出了这两个关键字，正常情况下，为了让代码简明、易读，可以省略这两个关键字  
> 不要混淆dash.dependencies.Input 与dash_core_components.Input对象。前者只在回调函数中使用，后者才是真正的组件  

####3.dash交互式数据图
> dash组件通过响应式方法描述属性，回调函数可以更新各个属性，有些属性还可以通过用户交互进行更新。比如点选dcc.Dropdown 组件的选项，该组件的value 特性就会改变  
> 

####4.dash与Flask相结合支持显示多个页面
* 如果需要展示的内容很多，或者需要分类展示时，就需要提供多个界面以及在各个界面间跳转。Flask是一个使用 Python 编写的轻量级 Web 应用框架，Dash的Web框架就是调用它实现的，在程序中结合二者，即可以显示一网页，还能实现Dash画图功能，还能相互调用。
```python
import numpy as np
import pandas as pd

from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html

server = Flask(__name__)
app1 = dash.Dash(__name__, server=server, url_base_pathname='/dash/')
app1.layout = html.Div([
    html.Div(
        children=[html.H1(children='趋势 1'),]
    )    
    ])

@server.route('/test')
def do_test():
    return "aaaaaaaaaaaaaaaaa"

@server.route('/')
def do_main():
    return "main"

if __name__ == '__main__':
    server.run(debug=True, port=8501, host="0.0.0.0")
```