# -*-coding:utf-8-*-
# 自定义数据包IP地址

import sys
import re
from random import randint

from scapy.layers.inet import IP, TCP, UDP, send


def send_packet(protocol, src_ip, src_port, flags, dst_ip, dst_port, iface):
    """ Modify and send an IP packet """
    if protocol=='tcp':
        packet = IP(src=src_ip, dst=dst_ip)/TCP(flags=flags, sport=src_port, dport=dst_port)
    elif protocol=='udp':
        if flags: raise Exception(" Flags are not supported for udp")
        packet = IP(src=src_ip, dst=dst_ip)/UDP(sport=src_port, dport=dst_port)
    else:
        raise Exception("Unknown protocol")

    send(packet, iface=iface)