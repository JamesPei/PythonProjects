#__author__ = 'James'
#-*- coding:utf-8 -*-

from asyncore import dispatcher
from asynchat import async_chat
import socket,asyncore

PORT = 5005
NAME = 'TestChat'

#处理服务器和一个用户之间连接的类
class ChatSession(async_chat):

    def __init__(self, server, sock):
        async_chat.__init__(self, sock)     #标准设置任务
        self.server = server
        self.set_terminator("\r\n")     #用于将行终止符设定为\r\n，它也是网络协议中通用的终止符
        self.data = []
        #问候用户:
        # Pushes data on to the channel’s fifo to ensure its transmission. This is all you need to do to have the channel write the data out to the network, although it is possible to use your own producers in more complex schemes to implement encryption and chunking, for example.
        self.push('welcome to %s\r\n' % self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    #如果发现了一个终止对象，也就意味着读入了一个完整的行，将其广播给每个人
    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

#接受连接并且产生单个会话的类。他还会处理到其它会话的广播
class ChatServer(dispatcher):

    def __init__(self, port, name):
        #standard setup tasks
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()       #在服务器没有正确关闭的情况下重用同一个地址
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')

    def handle_accept(self):
        conn,addr = self.accept()
        self.sessions.append(ChatSession(self,conn))

if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:asyncore.loop()
    except KeyboardInterrupt: print






