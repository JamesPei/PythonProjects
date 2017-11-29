# -*-coding:utf-8-*-
# socketpair实例

import socket
import os

BUFSIZE = 1024


def test_socketpair():
    """ test unix socketpair """
    parent, child = socket.socketpair() # 返回两个相连的套接字对象
    pid = os.fork()                     # 派生出另一个进程
    try:
        if pid:
            print "@Parent, sending message..."
            child.close()
            parent.sendall("Hello from parent! ")
            response = parent.recv(BUFSIZE)
            print 'Response from child:', response
            parent.close()
        else:
            print "@Child, waiting for message from parent"
            parent.close()
            message = child.recv(BUFSIZE)
            print 'message from parent:', message
            child.sendall("Hello from child!")
            child.close()
    except Exception, err:
        print "Error: %s" % err


if __name__ == '__main__':
    test_socketpair()