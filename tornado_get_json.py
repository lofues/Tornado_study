"""
    获取前端提交的json字符串
"""


# tornodo读取客户端提交的访问参数演示
import json

import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url

# 演示响应函数

#用来响应用户请求
class IndexHandler(RequestHandler):
    # 响应以get方式发送的请求
    def get(self,*args,**kwargs):
        self.write('hello get')

    # 响应以post方式发送的请求
    def post(self,*args,**kwargs):
        self.write('hello post')

        # 取出json字符串
        # 二进制json字符串
        print(self.request.body)
        json_obj = json.loads(self.request.body)
        print(json_obj)
        data = json_obj.get('data')
        print(type(json.dumps(data)))
        print(data['username'],data['email'])



# 用来响应 /java 请求
class JavaHandler(RequestHandler):
    # 重写RequestHandler中的initialize方法
    # 获取路由列表中动态设置的参数(greeting,info)
    def initialize(self,greeting,info):
        self.greeting = greeting
        self.info = info

    def get(self,*args,**kwargs):
        # write方法只能接收一个字符串类型的参数
        self.write('{} {}'.format(self.greeting,self.info))


# 用来响应 /python 请求,处理如下路由的请求
# tornodo 路由列表
# /python
# /python/day1
# /python/day1/basic
class PythonHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.write('<a href={}>jump to java</a>'.format(self.reverse_url('java_url')))
        self.write('<br>')

        # 获取命名参数
        day = kwargs.get('day',None)
        title = kwargs.get('title',None)

        if day:
            self.write('day:'+day+'<br>')
        if title:
            self.write('title:'+title)





# 演示配置文件

# 定义一个变量,用来代表端口号,若配置文件中找不到port,则使用default  multiple 是否为多个元素
define('port',type=int,default=11111,multiple=False)
# 再定义一个变量,用来代表连接数据库的连接信息(用户名,密码,端口,数据库名称)
define('db',multiple=True,default=[])

# 从指定的配置文件中,读取配置文件中的内容
parse_config_file('configure')
print(options.db)
print(options.port)





# 演示路由列表

# 创建application对象,进行对若干个服务器的设置
# 例如,路由列表 静态资源路径 模板路径



app = Application([
    ('/', IndexHandler),
    # 使用反向解析   调用时在类中使用self.reverse_url()
    url('/java', JavaHandler,{'greeting': '你好','info': '家娃'},name='java_url'),
    url('/python', PythonHandler,name='python_url'),
    # 演示位置传参
    # url('/python/(\w+)', PythonHandler),
    # url('/python/(\w+)/(\w+)', PythonHandler),

    # 演示命名传参
    url('/python/(?P<day>\w+)', PythonHandler),
    url('/python/(?P<day>\w+)/(?P<title>\w+)', PythonHandler),
])





# 演示服务器配置

# 创建服务器程序
server = HTTPServer(app)
# 服务器监听某个端口(建议使用10000以上的端口)
server.listen(options.port)
# 启动服务器(在当前进程中)
IOLoop.current().start()