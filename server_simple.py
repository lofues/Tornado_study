

import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

# CTRL + Y 删除一行
# CTRL + D 复制一行

#用来响应用户请求
class IndexHandler(RequestHandler):
    # 响应以get方式发送的请求
    def get(self,*args,**kwargs):
        self.write('my first tornodo')

    # 响应以post方式发送的请求
    def post(self,*args,**kwargs):
        pass

# 创建application对象,进行对若干个服务器的设置
# 例如,路由列表 静态资源路径 模板路径
app = Application([
    ('/', IndexHandler)
])

# 创建服务器程序
server = HTTPServer(app)
# 服务器监听某个端口(建议使用10000以上的端口)
server.listen(11111)
# 启动服务器(在当前进程中)
IOLoop.current().start()