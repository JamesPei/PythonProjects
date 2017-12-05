# -*-coding:utf-8-*-
# 扫描远程主机的端口

import argparse
import socket
import sys


def scan_ports(host, start_port, end_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, err_msg:
        print 'filed, code:'+str(err_msg[0])+'messgae:'+err_msg[1]
        sys.exit()

    # get ip of remmote host
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.error, err_msg:
        print err_msg
        sys.exit()

    # scans ports
    end_port += 1
    for port in range(start_port, end_port):
        try:
            sock.connect((remote_ip, port))
            print 'Port '+str(port)+' is open'
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host')
    parser.add_argument('--start-port')
    parser.add_argument('--end-port')
    given_args = parser.parse_args()
    host, start_port, end_port = given_args.host, given_args.start_port, given_args.end_port
    scan_ports(host, start_port, end_port)