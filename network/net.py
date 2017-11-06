# -*-coding:utf-8-*-

import socket


def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print 'Host Name:', host_name
    print 'IP:', ip_address


# find service name by port
def find_service_name():
    protocolname = 'tcp'
    for port in [80,25]:
        print 'Port: %s=> service name:%s' % (port, socket.getservbyport(port, protocolname))
    print "Port: %s => service name: %s" % (53, socket.getservbyport(53, 'udp'))


# 主机字节序与网络字节序之间相互转换
def convert_integer():
    data = 1234
    # 32-bit
    print 'Original: %s => Long host byte order: %s, Network byte order: %s' % (data, socket.ntohl(data),
                                                                                socket.htonl(data))
    # 16-bit
    print 'Original: %s => Short host byte order: %s, Network byte order: %s' % (data, socket.ntohs(data),
                                                                                 socket.htons(data))


# 设定并获取默认的套接字超时时间
def socket_timeout():
    s = socket.socket(socket.AF_INET,       # 地址族
                      socket.SOCK_STREAM)   # 套接字类型
    print 'Default socket timeout: %s' % s.gettimeout()
    s.settimeout(100)
    print 'Socket timeout: %s' % s.gettimeout()

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096


# 修改socket缓冲区大小
def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)  # level, option[, buffersize]
    print 'Buffer size:', bufsize

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
        socket.SOL_SOCKET,      # level
        socket.SO_SNDBUF,       # option
        SEND_BUF_SIZE           # value
    )
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE
    )

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print 'Buffer size [After]: %d' % bufsize


# 将套接字改为阻塞或非阻塞式
def socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)    # 设为阻塞模式
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print "Trivial Server launched on socket: %s" % str(socket_address)
    while 1:
        s.listen(1)


# 重用套接字地址
def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "Old sock state: %s" % old_state

    # enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_stat = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "New sock state: %s" % new_stat

    local_part = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_part))
    srv.listen(1)

    while True:
        try:
            connection, addr = srv.accept()
            print 'Connected by %s:%s' % (addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print '%s' % (msg,)

if __name__ == '__main__':
    # print_machine_info()
    # find_service_name()
    # convert_integer()
    # socket_timeout()
    # modify_buff_size()
    # socket_modes()
    reuse_socket_addr()