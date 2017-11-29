# -*-coding:utf-8-*-
# 找出设备中某个接口的IP地址（Linux专用），使用fnctl模块在设备中查询IP地址

import argparse
import sys
import socket
import fcntl
import struct
import array


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # inet_ntoa:将二进制数据转换为点分格式
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python networking utils')
    parser.add_argument('--ifname', action='store', dest='ifname', required=True)
    given_args = parser.parse_args()
    ifname = given_args.ifname
    print "Interface [%s] --> IP:%s" % (ifname, get_ip_address(ifname))