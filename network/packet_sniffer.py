# -*-coding:utf-8-*-

import argparse
import pcap         # pcap是保存网络数据的常用的一种文件格式
from construct.protocols.ipstack import ip_stack


def print_packet(pktlen, data, timestamp):
    if not data:
        return

    stack = ip_stack.parse(data)
    payload = stack.next.next.next
    print payload


def main():
    parser = argparse.ArgumentParser(description='packet sniffer')
    parser.add_argument('--iface', action='store', dest='iface', default='eth0')
    parser.add_argument('--port', action='store', dest='port', default=80, type=int)
    given_args = parser.parse_args()
    iface,port = given_args.iface, given_args.port
    # start sniffing
    pc = pcap.pcapObject()      # 创建嗅探器实例
    pc.open_live(iface, 1600, 0, 100)
    pc.setfilter('dst port %d' % port, 0, 0)    # 设置过滤器

    try:
        while True:
            pc.dispatch(1, print_packet)
    except KeyboardInterrupt:
        print 'Packet statistics:%d packets received, %d packets dropped, %d packets droped by interface' % pc.stats()

if __name__ == '__main__':
    main()