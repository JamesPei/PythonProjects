#__author__ = 'James'
#-*-coding:utf-8-*-

from xmlrpclib import ServerProxy
from os.path import join,isfile
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import sys

MAX_HISTORY_LENGTH = 6

OK = 1
FAIL = 2
EMPTY = ''

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
        code,data = self._handle(query)
        if code == OK:
            return code,data
        else:
            history = history + [self.url]
            if len(history) >= MAX_HISTORY_LENGTH:
                return FAIL,EMPTY
            return self._broadcast(query,history)

    #用于将节点介绍给其它节点
    def hello(self,other):
        self.known.add(other)
        return OK

    #用于让节点找到文件并且下载
    def fetch(self, query, secret):
        if secret != self.secret : return FAIL
        code,data = self.query(query)
        if code == OK:
            f = open(join(self.dirname, query),'w')
            f.write(data)
            f.close()
            return OK
        else:
            return FAIL

    #内部使用，用于启动XML_RPC服务器
    def _start(self):
        s = SimpleXMLRPCServer(("",getPort(self.url)), logRequests=False)
        s.register_instance(self)
        s.serve_forever()

    #内部使用，用于处理请求
    def _handle(self,query):
        dir = self.dirname
        name = 'F:\\'+join(dir,query)
        print '....the file path:',name
        if not isfile(name):return FAIL,EMPTY
        return OK,open(name).read()

    #内部使用，用于将查询广播到所有已知的Node
    def _broadcast(self, query, history):
        for other in self.known.copy():
            if other in history:continue
            try:
                s = ServerProxy(other)
                code,data = s.query(query,history)
                if code==OK:
                    return  code,data
            except:
                self.known.remove(other)
        return FAIL,EMPTY

def main():
    url,directory,secret = sys.argv[1:]    #用来获取命令行参数，sys.argv[0]表示代码本身文件路径，所以参数从1开始
    n = Node(url, directory, secret)
    n._start()

if __name__=='__main__':main()


