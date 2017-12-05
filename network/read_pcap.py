# -*-coding:utf-8-*-
# 读取保存的pcap文件以重放流量
import argparse

from scapy.layers.inet import IP, send, PcapReader, sys
from scapy.plist import PacketList


def send_packet(recvd_pkt, src_ip, dst_ip, count):
    """ send modified packets """
    pkt_cnt = 0
    p_out = []
    for p in recvd_pkt:
        pkt_cnt += 1
        new_pkt = p.payload
        new_pkt[IP].dst = dst_ip
        new_pkt[IP].src = src_ip
        del new_pkt[IP].chksum
        p_out.append(new_pkt)
        if pkt_cnt % count == 0:
            send(PacketList(p_out))
            p_out = []

    # send rest of packet
    send(PacketList(p_out))
    print "Total packet sent: %d"%pkt_cnt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', action='store', dest='infile')
    parser.add_argument('--src-ip',action='store', dest='src_ip')
    parser.add_argument('--dst-ip',action='store', dest='dst_ip')
    parser.add_argument('--count', action='store', dest='count')
    given_args = parser.parse_args()
    infile, src_ip, dst_ip, count = given_args.infile, given_args.src_ip, given_args.dst_ip, given_args.count
    try:
        pkt_reader = PcapReader(infile)
        send_packet(pkt_reader, src_ip, dst_ip, count)
    except IOError:
        print "Failed reading file"
        sys.exit(1)