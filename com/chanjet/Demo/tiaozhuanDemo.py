#_*_ coding:utf-8 _*_
'''
Created on 2014年10月13��

@author: administrator
'''
import web

urls = ("/hello/(.*)", "hello",
        "/index/(.*)","index"
        )

app = web.application(urls, globals())

class hello:
    def GET(self,name):
        raise web.seeother("/index/"+name)
class index:
    def GET(self,name):
        return 'index:=====',name

if __name__ == "__main__":
    app.run()
