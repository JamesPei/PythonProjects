#__author__ = 'James'
#-*-coding:utf-8-*-

from xmlrpclib import ServerProxy,Fault
from os.path import join,isfile,abspath
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import sys

SimpleXMLRPCServer.allow_reuse_address = 1

MAX_HISTORY_LENGTH = 6

UNHANDLED = 100
ACCESS_DENIED = 200

#表示无法处理的查询异常
class UnhandledQuery(Fault):
    def __init__(self, message="couldn't handle the query"):
        Fault.__init__(self,UNHANDLED,message)

#在用户试图访问未被授权访问的资源时引发的异常
class AccessDenied(Fault):
    def __init__(self,message="Access denied"):
        Fault.__init__(self,ACCESS_DENIED,message)

#检查给定的目录中是否有给定的文件名
def inside(dir,name):
    dir = abspath(dir)
    name = abspath(name)
    return name.startswith(join(dir,''))

#从URL中提取端口
def getPort(url):
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])

#p2p网络中的节点
class Node:
    def __init__(self,url,dirname,secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set()

    #查询文件，可能会向其它已知节点寻求帮助，将文件作为字符串返回
    def query(self,query,history=[]):
        try:
            code,data = self._handle(query)
        except UnhandledQuery:
            history = history + [self.url]
            if len(history) >= MAX_HISTORY_LENGTH:raise
            return self._broadcast(query,history)

    #用于将节点介绍给其它节点
    def hello(self,other):
        self.known.add(other)
        return 0

    #用于让节点找到文件并且下载
    def fetch(self, query, secret):
        if secret != self.secret : raise
        result = self.query(query)
        f = open(join(self.dirname,query),'w')
        f.write(result)
        f.close()
        return 0

    #内部使用，用于启动XML_RPC服务器
    def _start(self):
        s = SimpleXMLRPCServer(("",getPort(self.url)), logRequests=False)
        s.register_instance(self)
        s.serve_forever()

    #内部使用，用于处理请求
    def _handle(self,query):
        dir = self.dirname
        name = join(dir,query)
        if not isfile(name):raise UnhandledQuery
        if not inside(dir,name):raise AccessDenied
        return open(name).read()

    #内部使用，用于将查询广播到所有已知的Node
    def _broadcast(self, query, history):
        for other in self.known.copy():
            if other in history:continue
            try:
                s = ServerProxy(other)
                return s.query(query,history)
            except Fault,f:
                if f.faultCode == UNHANDLED:pass
                self.known.remove(other)
            except:
                self.known.remove(other)

        raise UnhandledQuery

def main():
    url,directory,secret = sys.argv[1:]
    n = Node(url, directory, secret)
    n._start()

if __name__=='__main__':main()

