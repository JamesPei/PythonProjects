#__author__ = 'James'
#-*- coding:utf-8 -*-

from asyncore import dispatcher
import socket,asyncore

class ChatServer(dispatcher):

    def handle_accept(self):
        conn,addr = self.accept() #允许客户连接：返回一个连接（针对客户端的具体套接字）和一个地址（有关所连接计算机的信息）
        print 'Connection attempt from',addr[0]

s = ChatServer()
s.create_socket(socket.AF_INET,socket.SOCK_STREAM)  #服务器初始化过程中会调用此方法，使用两个参数指定所需套接字的类型
s.bind(('',5005))   #把服务器绑定到具体的地址上
s.listen(5) #告诉服务器要监听的连接，并且指定5个连接的代办事务
asyncore.loop() #启动服务器，循环监听