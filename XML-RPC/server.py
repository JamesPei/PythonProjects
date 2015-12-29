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

#��ʾ�޷�����Ĳ�ѯ�쳣
class UnhandledQuery(Fault):
    def __init__(self, message="couldn't handle the query"):
        Fault.__init__(self,UNHANDLED,message)

#���û���ͼ����δ����Ȩ���ʵ���Դʱ�������쳣
class AccessDenied(Fault):
    def __init__(self,message="Access denied"):
        Fault.__init__(self,ACCESS_DENIED,message)

#��������Ŀ¼���Ƿ��и������ļ���
def inside(dir,name):
    dir = abspath(dir)
    name = abspath(name)
    return name.startswith(join(dir,''))

#��URL����ȡ�˿�
def getPort(url):
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])

#p2p�����еĽڵ�
class Node:
    def __init__(self,url,dirname,secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set()

    #��ѯ�ļ������ܻ���������֪�ڵ�Ѱ����������ļ���Ϊ�ַ�������
    def query(self,query,history=[]):
        try:
            code,data = self._handle(query)
        except UnhandledQuery:
            history = history + [self.url]
            if len(history) >= MAX_HISTORY_LENGTH:raise
            return self._broadcast(query,history)

    #���ڽ��ڵ���ܸ������ڵ�
    def hello(self,other):
        self.known.add(other)
        return 0

    #�����ýڵ��ҵ��ļ���������
    def fetch(self, query, secret):
        if secret != self.secret : raise
        result = self.query(query)
        f = open(join(self.dirname,query),'w')
        f.write(result)
        f.close()
        return 0

    #�ڲ�ʹ�ã���������XML_RPC������
    def _start(self):
        s = SimpleXMLRPCServer(("",getPort(self.url)), logRequests=False)
        s.register_instance(self)
        s.serve_forever()

    #�ڲ�ʹ�ã����ڴ�������
    def _handle(self,query):
        dir = self.dirname
        name = join(dir,query)
        if not isfile(name):raise UnhandledQuery
        if not inside(dir,name):raise AccessDenied
        return open(name).read()

    #�ڲ�ʹ�ã����ڽ���ѯ�㲥��������֪��Node
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

