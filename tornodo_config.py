

import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url


# CTRL + Y 删除一行
# CTRL + D 复制一行

# 演示响应函数

#用来响应用户请求
class IndexHandler(RequestHandler):
    # 响应以get方式发送的请求
    def get(self,*args,**kwargs):
        self.write('<a href="/python">hello python</a>')

    # 响应以post方式发送的请求
    def post(self,*args,**kwargs):
        pass

# 演示配置文件配置


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
])


# 演示服务器配置

# 创建服务器程序
server = HTTPServer(app)
# 服务器监听某个端口(建议使用10000以上的端口)
server.listen(options.port)
# 启动服务器(在当前进程中)
IOLoop.current().start()