# -*-coding:utf-8-*-

import socket
import select
import argparse

SERVER_HOST = 'localhost'

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

SERVER_RESPONSE = b""" """


class EpollServer(object):

    def __init__(self, host=SERVER_HOST, port=0):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.sock.setblocking(0)    # 套接字设定为非阻塞式
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # TCP_NODELAY使服务器无需缓冲即可直接交换数据
        print "Started Epoll Server"
        self.epoll = select.epoll()
        self.epoll.regietser(self.sock.fileno(), select.EPOLLIN)

    def run(self):
        """
        Execute epoll server operation
        """
        try:
            connections = {}
            requests = {}
            response = {}
            while True:
                events = self.epoll.poll(1)
                for fileno, event in events:
                    if fileno == self.sock.fileno():
                        connection, address = self.sock.accept()
                        connection.setblocking(0)
                        self.epoll.regietser(connection.fileno(), select.EPOLLIN)
                        connections[connection.fileno()] = connection
                        requests[connection.fileno()] = b''
                        response[connection.fileno()] = SERVER_RESPONSE
                    elif event & select.EPOLLIN:    # EPOLLIN套接字读事件
                        requests[fileno] += connections[fileno].recv(1024)
                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            self.epoll.modify(fileno, select.EPOLLOUT)      # EPOLLOUT套接字写事件
                            print '-'*40 + '\n' + requests[fileno].decode()[:-2]
                    elif event & select.EPOLLOUT:
                        byteswritten = connections[fileno].send(response[fileno])
                        response[fileno] = response[fileno][byteswritten:]
                        if len(response[fileno]) == 0:
                            self.epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:       # EPOLLOUT异常关闭信号
                        self.epoll.unregister(fileno)
                        connections[fileno].close()
                        del connections[fileno]
        finally:
            self.epoll.unregister(self.sock.fileno())
            self.epoll.close()
            self.sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example with Epoll')
    parser.add_argument('--port', action="store", dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    server = EpollServer(host=SERVER_HOST, port=port)
    server.run()